"""Shared runtime for the JARVIS plugin collection."""
from __future__ import annotations
import base64, difflib, hashlib, json, math, os, pathlib, re, statistics, uuid
from dataclasses import dataclass

@dataclass
class Result:
    ok: bool
    plugin: str
    data: object = None
    error: str | None = None

class PluginBase:
    name = "plugin"
    category = "General"
    description = "JARVIS capability"
    version = "1.0.0"
    def metadata(self):
        return {"name":self.name,"category":self.category,"description":self.description,"version":self.version}
    def run(self, payload=None):
        try: return Result(True,self.name,self.execute(payload or {}))
        except Exception as e: return Result(False,self.name,error=f"{type(e).__name__}: {e}")
    def execute(self, p):
        n=self.name
        if n=="json_validator":
            try: v=json.loads(p.get("text","")); return {"valid":True,"type":type(v).__name__,"value":v}
            except json.JSONDecodeError as e: return {"valid":False,"error":str(e),"line":e.lineno,"column":e.colno}
        if n in {"data_stats","statistics_tools"}:
            v=[float(x) for x in p.get("values",[])]; return {"count":len(v),"mean":statistics.mean(v) if v else None,"median":statistics.median(v) if v else None,"min":min(v) if v else None,"max":max(v) if v else None,"stdev":statistics.stdev(v) if len(v)>1 else 0.0}
        if n in {"hash_tools","hash_compare"}:
            a=str(p.get("text","")); algo=p.get("algorithm","sha256"); return {"algorithm":algo,"digest":hashlib.new(algo,a.encode()).hexdigest()}
        if n=="slugifier": return {"slug":re.sub(r"[^a-z0-9]+","-",str(p.get("text","")).lower()).strip("-")}
        if n=="text_stats":
            t=str(p.get("text","")); return {"characters":len(t),"lines":len(t.splitlines()),"words":len(re.findall(r"\b[\w'’-]+\b",t)),"sentences":len(re.findall(r"[.!?]+(?=\s|$)",t))}
        if n=="base64_tools":
            t=str(p.get("text","")); return {"text":base64.b64decode(t).decode() if p.get("mode")=="decode" else base64.b64encode(t.encode()).decode()}
        if n=="text_diff": return {"diff":"\n".join(difflib.unified_diff(str(p.get("a","")).splitlines(),str(p.get("b","")).splitlines(),fromfile="a",tofile="b",lineterm=""))}
        if n=="game_math":
            a=float(p.get("a",0)); b=float(p.get("b",1)); t=float(p.get("t",.5)); return {"lerp":a+(b-a)*t,"distance":abs(b-a),"clamped_t":max(0,min(1,t))}
        if n=="hitbox_checker":
            a,b=p["a"],p["b"]; return {"overlap":not(a["x"]+a["w"]<=b["x"] or b["x"]+b["w"]<=a["x"] or a["y"]+a["h"]<=b["y"] or b["y"]+b["h"]<=a["y"])}
        if n=="moving_average":
            v=[float(x) for x in p.get("values",[])]; w=max(1,int(p.get("window",3))); return {"values":[sum(v[max(0,i-w+1):i+1])/len(v[max(0,i-w+1):i+1]) for i in range(len(v))]}
        if n=="latency_percentiles":
            v=sorted(float(x) for x in p.get("values",[]));
            return {f"p{k}":v[min(len(v)-1,max(0,math.ceil(k/100*len(v))-1))] for k in (50,90,95,99)} if v else {}
        if n=="fps_counter_math":
            v=[float(x) for x in p.get("frame_times_ms",[]) if float(x)>0]; avg=statistics.mean(v) if v else 0; return {"average_frame_ms":avg,"average_fps":1000/avg if avg else 0}
        if n=="game_version_bumper":
            a=[int(x) for x in str(p.get("version","1.0.0")).split(".")[:3]]; a += [0]*(3-len(a)); i={"major":0,"minor":1,"patch":2}[p.get("part","patch")]; a[i]+=1
            for j in range(i+1,3): a[j]=0
            return {"version":".".join(map(str,a))}
        if n=="path_safety":
            root=pathlib.Path(p["root"]).resolve(); c=(root/p.get("path","")).resolve(); return {"safe":c==root or root in c.parents,"resolved":str(c)}
        if n=="code_metrics":
            t=str(p.get("code","")); return {"lines":len(t.splitlines()),"nonempty_lines":sum(bool(x.strip()) for x in t.splitlines()),"functions":len(re.findall(r"^\s*def\s+\w+",t,re.M)),"classes":len(re.findall(r"^\s*class\s+\w+",t,re.M)),"imports":len(re.findall(r"^\s*(?:from|import)\s+",t,re.M))}
        if n=="directory_tree":
            r=pathlib.Path(p.get("path",".")); d=int(p.get("depth",2)); return {"entries":[str(x.relative_to(r)) for x in r.rglob("*") if len(x.relative_to(r).parts)<=d]}
        if n=="checksum_tool":
            h=hashlib.new(p.get("algorithm","sha256"));
            with open(p["path"],"rb") as f:
                for c in iter(lambda:f.read(1048576),b""): h.update(c)
            return {"digest":h.hexdigest()}
        if n=="id_generator": return {"uuid4":str(uuid.uuid4()),"short":uuid.uuid4().hex[:12]}
        if n=="secure_random":
            import secrets; q=int(p.get("bytes",32)); return {"hex":secrets.token_hex(q),"url_safe":secrets.token_urlsafe(q)}
        if n=="retry_policy":
            a=int(p.get("attempt",0)); return {"delay_seconds":min(float(p.get("cap",30)),float(p.get("base",.5))*2**a)}
        if n=="template_engine":
            d=p.get("data",{}); return {"text":re.sub(r"\{\{\s*([^}]+?)\s*\}\}",lambda m:str(d.get(m.group(1).strip(),m.group(0))),str(p.get("template","")))}
        if n=="json_pretty":
            v=p.get("value"); v=json.loads(v) if isinstance(v,str) else v; return {"text":json.dumps(v,indent=p.get("indent",2),ensure_ascii=False,sort_keys=True)}
        if n=="unit_converter":
            value=float(p.get("value",0)); u=str(p.get("from","m")); to=str(p.get("to","m")); factors={"m":1,"km":1000,"cm":.01,"mm":.001,"mi":1609.344,"ft":.3048,"in":.0254}; return {"value":value*factors[u]/factors[to],"from":u,"to":to}
        return {"status":"ready","plugin":self.name,"category":self.category,"description":self.description,"received_keys":sorted(p)}

def make_plugin(name):
    import json as _json, pathlib as _path
    registry_path=_path.Path(__file__).with_name("registry.json")
    meta=next((x for x in _json.loads(registry_path.read_text(encoding="utf-8")) if x["name"]==name),{"name":name,"category":"General","description":"JARVIS capability"})
    return type("Plugin",(PluginBase,),meta)( )
