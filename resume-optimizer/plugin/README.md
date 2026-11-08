# Lionel Resume Optimizer — Plugin

The **skill** teaches an agent how to tailor a resume. This **plugin**
gives an agent tools it can actually call to do the deterministic work.

Same honesty rule as the skill: **no fabricated employers, titles, dates,
tools or metrics — ever.** The tools report gaps; they never fill them.

## The 4 tools

| Tool | Input | Returns |
|---|---|---|
| `score_resume` | resume + job | ATS score 0–100, keyword coverage, must-have coverage, sections, format flags |
| `extract_keywords` | job | Ranked keywords/skills the posting actually names |
| `gap_analysis` | resume + job | Matched vs missing keywords + missing must-haves, with the three-bucket honesty rule |
| `check_format` | resume | Section presence, word count, format red flags |

## Use it 3 ways

### 1. MCP — Claude Code, Codex, Cursor, any MCP client

Claude Code, from this repo (plugin manifest already wires the server):

```text
/plugin marketplace add lionelsimai/lionel-resume-optimizer
/plugin install resume-optimizer@lionel-sim-skills
```

Any other MCP client — add this to its MCP config:

```json
{
  "mcpServers": {
    "resume-optimizer": {
      "command": "python3",
      "args": ["/path/to/lionel-resume-optimizer/plugin/mcp_server.py"]
    }
  }
}
```

### 2. REST — GPT Actions, LangChain, your own agent, curl

```bash
python3 plugin/rest_server.py --port 8787
curl -X POST http://localhost:8787/score \
  -H 'Content-Type: application/json' \
  -d '{"resume_text": "...", "job_text": "..."}'
```

Endpoints: `POST /score`, `POST /keywords`, `POST /gap-analysis`,
`POST /check-format`, plus `GET /health`, `GET /openapi.json` and
`GET /.well-known/ai-plugin.json`. Point a GPT Action at `/openapi.json`.
Local by default — put your own auth/TLS in front before exposing it
publicly. Resumes are personal data.

### 3. Direct call — no server

```python
import sys; sys.path.insert(0, "plugin")
from mcp_server import call_tool
result = call_tool("score_resume", {"resume_text": resume, "job_text": job})
```

## How plugin + skill work together

1. Agent calls `extract_keywords` + `score_resume` — the "before" picture
2. Agent calls `gap_analysis`, sorts gaps into the skill's three buckets
3. Agent rewrites following `SKILL.md` (only buckets 1–2 get written in)
4. Agent calls `score_resume` again — the "before / after" proof

## Files

| Path | What it is |
|---|---|
| `mcp_server.py` | MCP server over stdio, stdlib only |
| `rest_server.py` | REST server, stdlib only, same tools |
| `openapi.json` | OpenAPI 3.1 spec for the REST API |
| `ai-plugin.json` | Plugin manifest (served at `/.well-known/ai-plugin.json`) |
| `.mcp.json` | Ready-made MCP client config for this folder |
| `resume_optimizer_core.py` | Vendored scorer copy, so this folder works standalone |
| `tests/test_plugin.py` | Smoke tests: direct calls, MCP handshake, REST routes |

## Test

```bash
python3 plugin/tests/test_plugin.py
```

MIT licensed — see the repo `LICENSE`. Built by Lionel Sim
(The AI Capitol), https://www.linkedin.com/in/lionelshen
