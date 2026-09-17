import importlib
import json
from pathlib import Path

ROOT = Path(__file__).parents[1]
REGISTRY = json.loads((ROOT / "plugins" / "registry.json").read_text(encoding="utf-8"))

def test_registry_has_unique_names():
    names = [x["name"] for x in REGISTRY]
    assert len(names) == len(set(names))
    assert len(names) >= 200

def test_every_plugin_module_imports():
    for item in REGISTRY:
        mod = importlib.import_module(f"plugins.{item['name']}")
        assert hasattr(mod, "Plugin")
        assert callable(getattr(mod.Plugin, "run", None))
        result = mod.Plugin.run({})
        assert hasattr(result, "ok")
        assert result.plugin == item["name"]

def test_core_tools():
    from plugins.json_validator import Plugin as JsonValidator
    from plugins.game_math import Plugin as GameMath
    from plugins.hitbox_checker import Plugin as Hitbox
    from plugins.unit_converter import Plugin as Converter
    assert JsonValidator.run({"text": '{"ok": true}'}).data["valid"] is True
    assert GameMath.run({"a": 0, "b": 10, "t": .5}).data["lerp"] == 5
    assert Hitbox.run({"a": {"x":0,"y":0,"w":2,"h":2}, "b": {"x":1,"y":1,"w":2,"h":2}}).data["overlap"] is True
    assert Converter.run({"value": 1, "from": "km", "to": "m"}).data["value"] == 1000

def test_error_boundary():
    from plugins.hitbox_checker import Plugin as Hitbox
    result = Hitbox.run({})
    assert result.ok is False
    assert result.error
