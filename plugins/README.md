# Plugins in this collection

Skills teach an agent how to work. Plugins give an agent tools it can
actually call. This collection ships plugins through three routes —
pick the one your host supports.

## The three routes

### 1. Claude Code marketplace

The root [marketplace manifest](../.claude-plugin/marketplace.json)
lists the installable plugins in this repo:

```text
/plugin marketplace add lionelsimai/claude-skills-collection
/plugin install resume-optimizer@lionel-sim-skills
/plugin install auto-gtm-agent@lionel-sim-skills
/plugin install gtm-community-plugins@lionel-sim-skills
```

### 2. MCP servers

Two packages ship real MCP servers (Python 3, standard library only):

- `resume-optimizer/plugin/mcp_server.py` — 4 tools: `score_resume`,
  `extract_keywords`, `gap_analysis`, `check_format`.
- `gtm-community-plugins/mcp_server.py` — one tool per plugin in the
  120-plugin suite.

Claude Desktop (`claude_desktop_config.json`) or any `.mcp.json`:

```json
{
  "mcpServers": {
    "resume-optimizer": {
      "command": "python3",
      "args": ["/path/to/claude-skills-collection/resume-optimizer/plugin/mcp_server.py"]
    },
    "gtm-community-plugins": {
      "command": "python3",
      "args": ["/path/to/claude-skills-collection/gtm-community-plugins/mcp_server.py"]
    }
  }
}
```

### 3. REST / OpenAI-style plugins

The same packages ship REST servers plus `ai-plugin.json` and
`openapi.json` manifests, for GPT Actions, LangChain or your own agent:

```bash
python3 resume-optimizer/plugin/rest_server.py --port 8787
python3 gtm-community-plugins/rest_server.py --port 8788
```

Auto-GTM Agent is deliberately **not** in routes 2–3: it is a Python
CLI with an actions manifest (`auto-gtm-agent/plugin.json`). Its
contract is documented in [auto-gtm-agent/PLUGIN.md](../auto-gtm-agent/PLUGIN.md).
Nothing here fabricates a transport a package does not provide.

## All plugins

| Plugin | Route(s) | Count | What it does |
|---|---|---|---|
| [GTM Community Plugins](../gtm-community-plugins/README.md) | Marketplace, MCP, REST | 120 plugins (60 GTM + 60 Community) | Scoring, triage, checklists, audits, drafts and reports across 20 categories of 6. Full registry: [its catalog.json](../gtm-community-plugins/catalog.json) and [CATALOG.md](../gtm-community-plugins/CATALOG.md) |
| [Resume Optimizer](../resume-optimizer/README.md) | Marketplace, MCP, REST | 1 plugin, 4 tools | ATS scoring, keyword extraction, honest gap analysis and format checks for a resume against a job posting. Standalone repo: https://github.com/lionelsimai/lionel-resume-optimizer |
| [Auto-GTM Agent](../auto-gtm-agent/README.md) | Marketplace (metadata), CLI actions | 1 plugin, 5 actions | Learn an offer, score leads, draft personal emails for approval, triage replies, learn which segments to scale or pause. Nothing auto-sends |

**Total: 122 plugins** (120 in the GTM suite + Resume Optimizer +
Auto-GTM Agent).

## Rules every plugin here follows

- Draft-only: no plugin sends, publishes or pays on its own.
- Pricing, contract and legal matters always escalate to a human.
- No fabricated metrics, clients or results — in outputs or in docs.
- Local-first servers: bind locally, add your own auth/TLS before
  exposing anything publicly.
