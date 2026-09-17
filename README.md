# JARVIS Mark 54 — Extreme Plugin Library

**257 separate Python plugins** for JARVIS, organized by capability. Every plugin has its own `plugins/<name>.py` module and is described in `plugins/registry.json`.

## Languages / Språk

- **Python** — implementation language for every plugin.
- **English** — primary technical descriptions.
- **Svenska** — each entry below has a Swedish purpose/description.

## Plugin directory / Pluginlista

| # | Plugin | Category | What it does / why | Svenska – vad och varför |
|---:|---|---|---|---|
1 | `code_formatter` | Coding | Format Python/JSON/YAML/text with deterministic fallback formatting. | Formaterar Python/JSON/YAML/text så JARVIS kan hålla kod konsekvent. |
2 | `code_linter` | Coding | Run lightweight static checks on Python source. | Kör lätta statiska kontroller av Python-kod. |
3 | `code_metrics` | Coding | Calculate lines, functions, classes, imports, and complexity hints. | Räknar kodrader, funktioner, klasser och importer för snabb kodanalys. |
4 | `dependency_auditor` | Coding | Inspect Python dependencies for version/pin issues. | Kontrollerar Python-beroenden och versionsproblem. |
5 | `project_scaffold` | Coding | Generate clean project directory structures. | Skapar rena projektstrukturer automatiskt. |
6 | `python_runner` | Coding | Run Python snippets in a controlled subprocess. | Kör Python-kod i en separat process. |
7 | `test_generator` | Coding | Generate pytest-style test skeletons from function definitions. | Skapar testmallar från Python-funktioner. |
8 | `docstring_generator` | Coding | Generate docstring templates from Python signatures. | Skapar docstring-mallar från funktionssignaturer. |
9 | `regex_builder` | Coding | Build and test regular expressions against supplied samples. | Bygger och testar reguljära uttryck. |
10 | `json_validator` | Coding | Validate and inspect JSON documents. | Validerar och inspekterar JSON. |
11 | `yaml_validator` | Coding | Validate YAML when PyYAML is available. | Validerar YAML när PyYAML finns. |
12 | `toml_validator` | Coding | Validate TOML using the standard library. | Validerar TOML med standardbiblioteket. |
13 | `csv_inspector` | Coding | Inspect CSV headers, rows, and type hints. | Inspekterar CSV-kolumner, rader och datatyper. |
14 | `diff_analyzer` | Coding | Summarize unified diffs and changed files. | Sammanfattar kodskillnader och ändrade filer. |
15 | `gitignore_generator` | Coding | Generate practical .gitignore templates. | Skapar praktiska .gitignore-mallar. |
16 | `readme_builder` | Coding | Create README structure and project metadata. | Skapar README-struktur och projektmetadata. |
17 | `api_contract_checker` | Coding | Check simple REST endpoint contract definitions. | Kontrollerar enkla REST-kontrakt. |
18 | `sql_query_helper` | Coding | Analyze SQL text and flag common portability issues. | Analyserar SQL och hittar vanliga kompatibilitetsproblem. |
19 | `html_validator` | Coding | Perform basic HTML structure checks. | Kontrollerar grundläggande HTML-struktur. |
20 | `css_analyzer` | Coding | Analyze CSS selectors, declarations, and duplicate rules. | Analyserar CSS-selektorer och dubbla regler. |
21 | `js_analyzer` | Coding | Perform lightweight JavaScript syntax heuristics. | Gör lätta syntaxkontroller av JavaScript. |
22 | `typescript_helper` | Coding | Inspect TypeScript interfaces and type declarations. | Inspekterar TypeScript-typer och gränssnitt. |
23 | `shell_script_checker` | Coding | Check shell scripts for common portability hazards. | Kontrollerar portabilitetsproblem i shell-script. |
24 | `log_parser` | Coding | Parse common timestamped application log lines. | Tolkar vanliga tidsstämplade loggrader. |
25 | `stacktrace_analyzer` | Coding | Extract exceptions and likely source locations. | Hittar undantag och möjliga källkodsrader i stacktraces. |
26 | `error_classifier` | Coding | Classify error text into actionable categories. | Klassificerar fel till användbara kategorier. |
27 | `benchmark_runner` | Coding | Benchmark a callable or command repeatedly. | Mäter prestanda genom upprepade körningar. |
28 | `code_search` | Coding | Search source trees with regex and file filters. | Söker i källkod med regex och filfilter. |
29 | `symbol_indexer` | Coding | Index Python classes, functions, and imports. | Indexerar Python-klasser, funktioner och importer. |
30 | `license_scanner` | Coding | Scan source headers for common license markers. | Söker efter licensmarkeringar i källkod. |
31 | `secret_scanner` | Coding | Detect likely credentials and tokens using patterns. | Hittar möjliga lösenord, tokens och nycklar i text. |
32 | `game_project_scaffold` | GameDev | Create a generic game project layout. | Skapar en grundstruktur för spelprojekt. |
33 | `game_asset_catalog` | GameDev | Catalog image/audio/model assets by extension. | Katalogiserar grafik-, ljud- och modellfiler. |
34 | `sprite_sheet_analyzer` | GameDev | Inspect sprite-sheet dimensions and frame counts. | Analyserar spritesheets och antal frames. |
35 | `tilemap_helper` | GameDev | Validate simple tilemap grids and dimensions. | Validerar tilemaps och deras dimensioner. |
36 | `level_generator` | GameDev | Generate deterministic grid-based test levels. | Skapar reproducerbara testbanor. |
37 | `loot_table_generator` | GameDev | Generate weighted loot tables. | Skapar viktade loot-tabeller. |
38 | `dialogue_manager` | GameDev | Validate dialogue trees and detect dead ends. | Kontrollerar dialogträd och återvändsgränder. |
39 | `quest_generator` | GameDev | Generate structured quest templates. | Skapar strukturerade quest-mallar. |
40 | `npc_behavior_planner` | GameDev | Build simple state-machine NPC behavior plans. | Planerar NPC-beteenden som state machines. |
41 | `enemy_wave_generator` | GameDev | Generate scalable enemy wave definitions. | Skapar skalbara fiendevågor. |
42 | `game_balance_analyzer` | GameDev | Compare damage, health, and economy parameters. | Jämför skade-, hälso- och ekonomivärden. |
43 | `xp_curve_generator` | GameDev | Generate progression curves. | Skapar XP- och progressionkurvor. |
44 | `skill_tree_generator` | GameDev | Generate connected skill-tree graphs. | Skapar sammankopplade skill trees. |
45 | `crafting_system` | GameDev | Validate recipes and resource costs. | Kontrollerar crafting-recept och resurskostnader. |
46 | `inventory_system` | GameDev | Provide stack-aware inventory calculations. | Hanterar stackar och inventarieberäkningar. |
47 | `savegame_validator` | GameDev | Validate JSON-style save-game structures. | Validerar sparfiler och deras struktur. |
48 | `checkpoint_manager` | GameDev | Manage deterministic checkpoint metadata. | Hanterar checkpoint-data på ett reproducerbart sätt. |
49 | `dialogue_localizer` | GameDev | Check localization keys across languages. | Kontrollerar dialognycklar mellan språk. |
50 | `localization_checker` | GameDev | Find missing and extra translation keys. | Hittar saknade och extra översättningsnycklar. |
51 | `game_config_validator` | GameDev | Validate common game configuration structures. | Validerar spelkonfigurationer. |
52 | `input_map_generator` | GameDev | Generate keyboard/controller action maps. | Skapar tangentbords- och kontrollmappningar. |
53 | `game_event_bus` | GameDev | Provide a small event registration and dispatch model. | Ger spel ett enkelt event-system. |
54 | `achievement_generator` | GameDev | Generate achievement definitions from goals. | Skapar achievements från mål. |
55 | `daily_challenge_generator` | GameDev | Generate deterministic daily challenge seeds. | Skapar reproducerbara dagliga challenge-seeds. |
56 | `procedural_name_generator` | GameDev | Generate deterministic fantasy/game names. | Skapar reproducerbara namn för spelvärldar. |
57 | `map_seed_generator` | GameDev | Generate reproducible world seeds. | Skapar reproducerbara world seeds. |
58 | `gameplay_timer` | GameDev | Calculate frame/time budgets and cooldown schedules. | Beräknar tidsbudgetar och cooldowns. |
59 | `hitbox_checker` | GameDev | Check rectangular hitbox overlap. | Kontrollerar kollision mellan rektangulära hitboxar. |
60 | `pathfinding_astar` | GameDev | Run A* on a small grid. | Kör A*-pathfinding på grid-banor. |
61 | `game_math` | GameDev | Provide interpolation, clamp, distance, and angle helpers. | Ger matematiska hjälpfunktioner för spel. |
62 | `camera_controller_math` | GameDev | Calculate camera follow positions. | Beräknar kamerans följpositioner. |
63 | `game_state_machine` | GameDev | Implement a simple finite state machine. | Implementerar state machines för spel. |
64 | `replay_data_validator` | GameDev | Validate compact replay event streams. | Validerar replay-data. |
65 | `mod_manifest_builder` | GameDev | Build mod manifest dictionaries. | Skapar metadata för mods. |
66 | `mod_dependency_checker` | GameDev | Resolve simple mod dependency graphs. | Kontrollerar mod-beroenden. |
67 | `shader_parameter_validator` | GameDev | Validate shader parameter metadata. | Validerar shader-parametrar. |
68 | `particle_config_generator` | GameDev | Generate configurable particle presets. | Skapar particle-effektkonfigurationer. |
69 | `audio_event_catalog` | GameDev | Catalog sound events and missing files. | Katalogiserar ljudhändelser och saknade ljudfiler. |
70 | `game_build_manifest` | GameDev | Create reproducible build manifests. | Skapar reproducerbara build-manifest. |
71 | `game_version_bumper` | GameDev | Bump semantic game versions. | Höjer spelets semantiska version. |
72 | `game_patch_notes` | GameDev | Generate patch-note structures from change lists. | Skapar strukturerade patch notes. |
73 | `game_test_case_generator` | GameDev | Generate gameplay test-case matrices. | Skapar testmatriser för gameplay. |
74 | `game_telemetry_schema` | GameDev | Validate event telemetry schemas. | Validerar telemetry-format för spelhändelser. |
75 | `game_performance_budget` | GameDev | Check CPU/GPU/memory budget targets. | Kontrollerar CPU-, GPU- och minnesbudgetar. |
76 | `game_ai_director` | GameDev | Generate adaptive encounter intensity plans. | Skapar planer för adaptiv spelintensitet. |
77 | `game_economy_simulator` | GameDev | Simulate simple buy/sell economy loops. | Simulerar köp-, sälj- och ekonomiflöden. |
78 | `game_probability_tool` | GameDev | Calculate drop and event probabilities. | Beräknar drop- och event-sannolikheter. |
79 | `game_leaderboard_validator` | GameDev | Validate leaderboard records and sorting. | Validerar leaderboard-data och sortering. |
80 | `game_replay_checksum` | GameDev | Create deterministic replay checksums. | Skapar checksummor för replay-integritet. |
81 | `game_content_hash` | GameDev | Hash game assets for integrity checks. | Hashar spelresurser för integritetskontroll. |
82 | `game_data_migrator` | GameDev | Migrate versioned JSON-like game data. | Migrerar versionshanterad speldata. |
83 | `game_config_diff` | GameDev | Diff two game configurations. | Jämför två spelkonfigurationer. |
84 | `game_mod_template` | GameDev | Generate a generic mod package layout. | Skapar grundstruktur för spelmods. |
85 | `game_release_checker` | GameDev | Run release readiness checks on a project. | Kontrollerar om ett spelprojekt är redo för release. |
86 | `fps_counter_math` | Optimization | Calculate FPS, frame time, and percentile metrics. | Beräknar FPS, frametid och percentiler. |
87 | `frame_time_analyzer` | Optimization | Analyze frame-time samples. | Analyserar frametidsmätningar. |
88 | `cpu_benchmark` | Optimization | Measure local CPU-bound Python workloads. | Mäter CPU-prestanda för lokala arbetslaster. |
89 | `memory_profiler_basic` | Optimization | Measure Python object sizes and process snapshots. | Mäter Python-minne och processdata. |
90 | `cache_strategy` | Optimization | Provide LRU-style cache utilities. | Ger LRU-liknande cachefunktioner. |
91 | `batch_optimizer` | Optimization | Group work into efficient batches. | Grupperar arbete i effektiva batchar. |
92 | `parallel_task_planner` | Optimization | Plan parallel work across available CPUs. | Planerar parallellt arbete över CPU-kärnor. |
93 | `thread_pool_helper` | Optimization | Run independent callables in a thread pool. | Kör oberoende uppgifter i thread pool. |
94 | `process_pool_helper` | Optimization | Run CPU-bound callables in a process pool. | Kör CPU-tunga uppgifter i process pool. |
95 | `file_hash_cache` | Optimization | Cache file hashes by metadata. | Cachar filhashar med metadata. |
96 | `duplicate_file_finder` | Optimization | Find duplicate files by size and hash. | Hittar dubbla filer med storlek och hash. |
97 | `large_file_finder` | Optimization | Find large files under a directory. | Hittar stora filer i kataloger. |
98 | `startup_profiler` | Optimization | Measure import/startup timing for Python modules. | Mäter import- och starttider för Python. |
99 | `json_speed_test` | Optimization | Benchmark JSON serialization approaches. | Jämför JSON-serialiseringsprestanda. |
100 | `regex_performance` | Optimization | Benchmark regex patterns on sample text. | Mäter regex-prestanda på testdata. |
101 | `algorithm_timer` | Optimization | Time arbitrary Python callables. | Tidsmäter Python-funktioner. |
102 | `memory_growth_detector` | Optimization | Compare memory snapshots between phases. | Hittar minnestillväxt mellan körningsfaser. |
103 | `io_batcher` | Optimization | Batch file operations to reduce overhead. | Samlar filoperationer i batchar. |
104 | `directory_stats` | Optimization | Summarize directory size and file counts. | Sammanfattar katalogstorlek och filantal. |
105 | `asset_size_optimizer` | Optimization | Report oversized game assets by extension. | Hittar för stora spelresurser. |
106 | `texture_budget_checker` | Optimization | Check texture dimensions against budgets. | Kontrollerar texturstorlekar mot budget. |
107 | `audio_budget_checker` | Optimization | Check audio file sizes against budgets. | Kontrollerar ljudstorlek mot budget. |
108 | `model_budget_checker` | Optimization | Check model/asset counts and rough budgets. | Kontrollerar modellantal och resursbudgetar. |
109 | `network_latency_tool` | Optimization | Measure TCP connection latency to a host. | Mäter nätverkslatens mot en host. |
110 | `http_cache_headers` | Optimization | Inspect HTTP cache-control headers. | Inspekterar HTTP-cacheheaders. |
111 | `compression_benchmark` | Optimization | Compare gzip compression ratios and speed. | Jämför komprimeringsgrad och hastighet. |
112 | `serialization_benchmark` | Optimization | Compare serialization payload sizes. | Jämför storlek på serialiserad data. |
113 | `database_index_advisor` | Optimization | Suggest indexes from simple SQL query patterns. | Identifierar möjliga databasindex från SQL. |
114 | `sql_plan_notes` | Optimization | Explain common SQL performance patterns. | Förklarar vanliga SQL-prestandamönster. |
115 | `load_test_planner` | Optimization | Generate load-test stages and targets. | Skapar steg och mål för lasttester. |
116 | `rate_limit_calculator` | Optimization | Calculate request rates and burst capacity. | Beräknar request-rate och burstkapacitet. |
117 | `queue_throughput` | Optimization | Calculate queue throughput and utilization. | Beräknar kögenomströmning och belastning. |
118 | `latency_percentiles` | Optimization | Calculate p50/p90/p95/p99 latency. | Beräknar latenspercentiler. |
119 | `resource_budget` | Optimization | Compare resource usage against configured budgets. | Jämför resursanvändning mot budgetar. |
120 | `performance_report` | Optimization | Aggregate benchmark results into a report. | Samlar benchmarkresultat i en rapport. |
121 | `project_health` | Optimization | Score factual project health metrics without subjective ranking. | Sammanställer mätbara projektmått utan subjektiv ranking. |
122 | `system_info` | System | Collect cross-platform Python/runtime information. | Samlar system- och Python-information. |
123 | `disk_space` | System | Report disk usage for a path. | Rapporterar diskutrymme. |
124 | `process_list` | System | List local processes where supported. | Listar lokala processer när systemet stöder det. |
125 | `environment_inspector` | System | Inspect selected environment variable names safely. | Inspekterar valda miljövariabler utan att visa hemliga värden. |
126 | `port_checker` | System | Check whether a TCP port is reachable locally. | Kontrollerar TCP-portar. |
127 | `hostname_resolver` | System | Resolve hostnames to addresses. | Slår upp hostnames till IP-adresser. |
128 | `network_interfaces` | System | List local network interfaces where available. | Listar nätverksgränssnitt. |
129 | `time_sync_info` | System | Report local timezone and clock information. | Rapporterar tidszon och klockinformation. |
130 | `file_watcher` | System | Watch a directory for changes with polling. | Bevakar kataloger efter ändringar. |
131 | `file_organizer` | System | Plan file organization by extension. | Planerar filorganisation efter filtyp. |
132 | `backup_planner` | System | Generate incremental backup plans. | Skapar planer för inkrementella backuper. |
133 | `archive_manager` | System | Create/list/extract ZIP archives. | Skapar, listar och packar upp ZIP-arkiv. |
134 | `checksum_tool` | System | Hash files using SHA-256 and other algorithms. | Hashar filer med SHA-256 och andra algoritmer. |
135 | `text_search` | System | Search files recursively with regex. | Söker rekursivt i filer med regex. |
136 | `safe_delete_planner` | System | Generate a reviewable deletion plan without deleting. | Skapar granskningsbara raderingsplaner utan att radera. |
137 | `directory_tree` | System | Render a compact directory tree. | Visar ett kompakt katalogträd. |
138 | `file_metadata` | System | Inspect file timestamps and sizes. | Inspekterar filstorlek och tidsstämplar. |
139 | `temp_file_manager` | System | Create and clean temporary working directories. | Hanterar temporära arbetskataloger. |
140 | `clipboard_helper` | System | Provide optional clipboard integration if installed. | Ger valfri clipboard-integration. |
141 | `notification_helper` | System | Provide optional desktop notifications if installed. | Ger valfria skrivbordsnotiser. |
142 | `screen_resolution` | System | Report screen information when a GUI backend is available. | Rapporterar skärminformation när GUI stöds. |
143 | `cpu_info` | System | Report CPU count and Python architecture. | Rapporterar CPU-antal och arkitektur. |
144 | `memory_info` | System | Report system memory when psutil is available. | Rapporterar systemminne när psutil finns. |
145 | `battery_info` | System | Report battery state when psutil is available. | Rapporterar batteristatus när psutil finns. |
146 | `os_info` | System | Report OS/platform details. | Rapporterar operativsystem och plattform. |
147 | `service_probe` | System | Probe a local HTTP service health endpoint. | Kontrollerar hälsostatus för lokala HTTP-tjänster. |
148 | `config_manager` | System | Load and validate JSON configuration. | Läser och validerar JSON-konfiguration. |
149 | `plugin_registry` | System | Discover Python plugins in a directory. | Upptäcker Python-plugins i en katalog. |
150 | `plugin_healthcheck` | System | Import-check plugin modules. | Kontrollerar att plugins kan importeras. |
151 | `plugin_manifest` | System | Generate plugin metadata manifests. | Skapar plugin-manifest med metadata. |
152 | `plugin_dependency_graph` | System | Build a dependency graph from manifests. | Bygger ett beroendegraf för plugins. |
153 | `plugin_loader` | System | Dynamically load plugin classes/functions. | Laddar plugin-klasser och funktioner dynamiskt. |
154 | `plugin_search` | System | Search plugin metadata by capability. | Söker plugins efter förmåga. |
155 | `plugin_router` | System | Route an intent to the best capability match without ranking output. | Dirigerar en intent till relevant förmåga. |
156 | `task_queue` | System | Provide a persistent-ish in-memory task queue. | Ger JARVIS en enkel uppgiftskö i minnet. |
157 | `scheduler_core` | System | Schedule delayed callable execution. | Schemalägger fördröjda uppgifter. |
158 | `event_logger` | System | Write structured JSONL events. | Loggar strukturerade JSONL-händelser. |
159 | `audit_logger` | System | Write local audit records. | Skriver lokala granskningsloggar. |
160 | `config_watcher` | System | Detect configuration file changes. | Upptäcker ändringar i konfigurationsfiler. |
161 | `health_endpoint` | System | Expose health information as a dictionary. | Exponerar hälsodata som strukturerad information. |
162 | `metrics_collector` | System | Collect counters and timing metrics. | Samlar räknare och tidsmått. |
163 | `retry_policy` | System | Calculate bounded retry delays. | Beräknar begränsade retry-fördröjningar. |
164 | `circuit_breaker` | System | Implement a simple circuit-breaker state model. | Implementerar circuit-breaker-logik. |
165 | `rate_limiter` | System | Implement token-bucket rate limiting. | Implementerar token-bucket rate limiting. |
166 | `id_generator` | System | Generate UUID and short IDs. | Skapar UUID och korta ID:n. |
167 | `data_redactor` | System | Redact common secrets from text. | Döljer vanliga hemligheter i text. |
168 | `schema_validator` | System | Validate basic dict schemas. | Validerar grundläggande datascheman. |
169 | `jsonl_reader` | System | Read JSON Lines safely. | Läser JSON Lines säkert. |
170 | `jsonl_writer` | System | Write JSON Lines records. | Skriver JSON Lines-poster. |
171 | `config_diff` | System | Diff two JSON-compatible configs. | Jämför två konfigurationer. |
172 | `template_engine` | System | Render simple {{variable}} templates. | Renderar enkla variabelmallar. |
173 | `feature_flags` | System | Evaluate local feature flags. | Hanterar lokala feature flags. |
174 | `cache_store` | System | Provide TTL key-value caching. | Ger TTL-baserad key-value-cache. |
175 | `secure_random` | System | Generate cryptographically secure random values. | Skapar kryptografiskt säkra slumpvärden. |
176 | `password_generator` | Security | Generate strong random passwords locally. | Skapar starka slumpmässiga lösenord lokalt. |
177 | `hash_password` | Security | Hash passwords with PBKDF2 using the standard library. | Hashar lösenord med PBKDF2. |
178 | `token_generator` | Security | Generate URL-safe random tokens. | Skapar URL-säkra tokens. |
179 | `secret_redactor` | Security | Redact credential-like strings. | Döljer strängar som ser ut som hemligheter. |
180 | `file_integrity` | Security | Create and verify file integrity manifests. | Skapar och verifierar integritetsmanifest. |
181 | `permission_audit` | Security | Inspect file permission bits. | Inspekterar filrättigheter. |
182 | `security_headers_checker` | Security | Check common HTTP security headers. | Kontrollerar vanliga HTTP-säkerhetsheaders. |
183 | `url_safety_parser` | Security | Parse URLs and identify risky schemes. | Tolkar URL:er och identifierar riskfyllda scheman. |
184 | `path_safety` | Security | Normalize and validate paths against a root. | Validerar sökvägar mot en tillåten rot. |
185 | `input_sanitizer` | Security | Normalize potentially unsafe text input. | Normaliserar potentiellt osäker text. |
186 | `archive_safety` | Security | Detect ZIP path traversal entries. | Upptäcker path-traversal i ZIP-arkiv. |
187 | `dependency_name_checker` | Security | Flag suspicious dependency naming patterns. | Markerar misstänkta beroendenamn. |
188 | `dev_server_guard` | Security | Generate safe local-only server settings. | Skapar säkra lokala serverinställningar. |
189 | `api_key_scanner` | Security | Scan text for common API-key patterns. | Söker efter vanliga API-nyckelmönster. |
190 | `config_secret_checker` | Security | Detect secrets in configuration dictionaries. | Hittar hemligheter i konfigurationer. |
191 | `hash_compare` | Security | Constant-time compare for byte/string values. | Jämför hemliga värden med konstant tidsbeteende. |
192 | `security_report` | Security | Aggregate deterministic security checks. | Samlar säkerhetskontroller i en rapport. |
193 | `web_fetcher` | Web | Fetch HTTP(S) resources with standard-library tooling. | Hämtar HTTP(S)-resurser med standardbiblioteket. |
194 | `url_parser` | Web | Parse and normalize URLs. | Tolkar och normaliserar URL:er. |
195 | `query_builder` | Web | Build encoded query strings. | Bygger URL-kodade query strings. |
196 | `http_status_explainer` | Web | Explain HTTP status classes. | Förklarar HTTP-statuskoder. |
197 | `robots_parser` | Web | Parse robots.txt directives. | Tolkar robots.txt-regler. |
198 | `sitemap_parser` | Web | Parse simple sitemap XML. | Tolkar sitemap-XML. |
199 | `html_link_extractor` | Web | Extract links from HTML. | Extraherar länkar ur HTML. |
200 | `rss_parser` | Web | Parse RSS/Atom feeds. | Tolkar RSS- och Atom-flöden. |
201 | `json_api_client` | Web | Call JSON APIs with standard-library HTTP. | Anropar JSON-API:er med standardbiblioteket. |
202 | `webhook_sender` | Web | Send JSON webhook requests. | Skickar JSON-webhooks. |
203 | `webhook_validator` | Web | Validate webhook payload shape. | Validerar webhook-payloads. |
204 | `http_retry` | Web | Perform bounded HTTP retries. | Gör begränsade HTTP-retries. |
205 | `url_health_checker` | Web | Check URL reachability and response metadata. | Kontrollerar URL-tillgänglighet och svar. |
206 | `content_type_detector` | Web | Infer content type from URL/file extension. | Identifierar innehållstyp från URL eller filändelse. |
207 | `http_header_parser` | Web | Parse HTTP header blocks. | Tolkar HTTP-headerblock. |
208 | `query_cache` | Web | Cache URL query results in memory. | Cachar query-resultat i minnet. |
209 | `api_pagination_helper` | Web | Generate page/offset pagination plans. | Skapar pagineringsplaner för API:er. |
210 | `api_rate_plan` | Web | Calculate client-side request pacing. | Beräknar lämplig request-takt. |
211 | `web_response_summarizer` | Web | Extract title, headings, and metadata from HTML. | Extraherar titel, rubriker och metadata ur HTML. |
212 | `cookie_parser` | Web | Parse HTTP cookie headers. | Tolkar HTTP-cookieheaders. |
213 | `form_encoder` | Web | Encode HTML form data. | Kodar HTML-formulärdata. |
214 | `url_joiner` | Web | Safely join URL path components. | Slår ihop URL-delar säkert. |
215 | `download_planner` | Web | Plan downloads without executing them. | Planerar nedladdningar utan att köra dem. |
216 | `content_hash_checker` | Web | Verify downloaded content against hashes. | Verifierar innehåll mot hashvärden. |
217 | `data_csv_tools` | Data | Read and summarize CSV data. | Läser och sammanfattar CSV-data. |
218 | `data_json_tools` | Data | Flatten simple JSON records. | Plattar ut enkla JSON-poster. |
219 | `data_stats` | Data | Calculate mean, median, min, max, and stdev. | Beräknar grundläggande statistik. |
220 | `data_cleaner` | Data | Normalize whitespace, nulls, and basic types. | Rensar whitespace, nullvärden och enkla datatyper. |
221 | `data_sampler` | Data | Deterministically sample records. | Tar reproducerbara stickprov. |
222 | `data_filter` | Data | Filter records using simple expressions. | Filtrerar dataposter. |
223 | `data_sorter` | Data | Stable-sort records by fields. | Sorterar dataposter stabilt efter fält. |
224 | `data_groupby` | Data | Group records by a field. | Grupperar poster efter ett fält. |
225 | `data_joiner` | Data | Join two record lists by a key. | Kopplar ihop två dataset med en nyckel. |
226 | `data_deduplicator` | Data | Deduplicate records by selected fields. | Tar bort dubbletter efter valda fält. |
227 | `data_profiler` | Data | Profile columns and missingness. | Profilerar kolumner och saknade värden. |
228 | `data_schema_infer` | Data | Infer basic field types. | Identifierar grundläggande datatyper. |
229 | `data_exporter` | Data | Export records to CSV/JSON. | Exporterar poster till CSV/JSON. |
230 | `data_chart_spec` | Data | Generate chart specifications for external renderers. | Skapar diagram-specifikationer för andra renderare. |
231 | `data_report` | Data | Create compact dataset reports. | Skapar kompakta datasetrapporter. |
232 | `time_series_stats` | Data | Analyze simple numeric time series. | Analyserar numeriska tidsserier. |
233 | `moving_average` | Data | Calculate moving averages. | Beräknar glidande medelvärden. |
234 | `outlier_detector` | Data | Detect IQR-based outliers. | Hittar IQR-baserade avvikare. |
235 | `correlation_helper` | Data | Calculate Pearson correlation. | Beräknar Pearson-korrelation. |
236 | `random_dataset` | Data | Generate reproducible synthetic datasets. | Skapar reproducerbara syntetiska dataset. |
237 | `unit_converter` | Utilities | Convert common length, mass, time, and data units. | Konverterar vanliga längd-, massa-, tids- och dataenheter. |
238 | `color_tools` | Utilities | Convert and validate hex/RGB colors. | Konverterar och validerar färger. |
239 | `uuid_tools` | Utilities | Validate and transform UUID strings. | Validerar och omvandlar UUID-strängar. |
240 | `slugifier` | Utilities | Create URL-safe slugs. | Skapar URL-säkra slugs. |
241 | `text_stats` | Utilities | Count words, lines, characters, and sentences. | Räknar ord, rader, tecken och meningar. |
242 | `text_chunker` | Utilities | Split text into bounded chunks. | Delar text i begränsade delar. |
243 | `markdown_tools` | Utilities | Extract headings and links from Markdown. | Extraherar rubriker och länkar från Markdown. |
244 | `timestamp_tools` | Utilities | Convert Unix timestamps to ISO timestamps. | Konverterar Unix-tidsstämplar till ISO-tid. |
245 | `date_math` | Utilities | Add/subtract durations from ISO dates. | Räknar fram datum med tidsintervall. |
246 | `number_tools` | Utilities | Provide numeric formatting and rounding helpers. | Ger verktyg för talformattering och avrundning. |
247 | `base64_tools` | Utilities | Encode/decode Base64 safely. | Kodar och avkodar Base64. |
248 | `url_encode_tools` | Utilities | Encode/decode URL components. | Kodar och avkodar URL-delar. |
249 | `hash_tools` | Utilities | Hash arbitrary text with standard algorithms. | Hashar text med standardalgoritmer. |
250 | `random_tools` | Utilities | Generate reproducible random sequences. | Skapar reproducerbara slumpsekvenser. |
251 | `math_tools` | Utilities | Provide common math helpers. | Ger vanliga matematiska hjälpfunktioner. |
252 | `statistics_tools` | Utilities | Provide descriptive statistics. | Ger beskrivande statistik. |
253 | `json_pretty` | Utilities | Pretty-print JSON deterministically. | Formaterar JSON på ett deterministiskt sätt. |
254 | `text_diff` | Utilities | Produce simple line-level text diffs. | Skapar radbaserade textskillnader. |
255 | `markdown_table` | Utilities | Create Markdown tables from records. | Skapar Markdown-tabeller från dataposter. |
256 | `template_data` | Utilities | Validate data required by templates. | Validerar data som mallar behöver. |
257 | `health_math` | Utilities | Calculate generic wellness-independent numeric metrics. | Beräknar generella numeriska mått. |

## Architecture

Each plugin exposes a standard `Plugin` entry point. The shared `plugins/runtime.py` provides metadata and structured `run(payload)` results, while `plugins/registry.json` is the discovery source.

## Running

```bash
python -c "from plugins.json_validator import Plugin; print(Plugin().run({'text':'{\"ok\":true}'}))"
```

The plugin library is designed to be extended: add a module, register its metadata, and JARVIS can discover the capability.