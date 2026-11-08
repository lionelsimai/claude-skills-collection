# Claude Skills Collection

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Version](https://img.shields.io/badge/version-2.0.0-blue)
![Skills](https://img.shields.io/badge/skills-5168-orange)
![Plugins](https://img.shields.io/badge/plugins-122-purple)

The largest open-source collection of Claude AI skills — **10,598 skills
across 287 categories**, plus **122 callable plugins** — maintained by
Lionel Sim ([The AI Capitol](https://theaicapitol.com)).

Skills are structured `SKILL.md` files that give an AI agent specific
frameworks, workflows and quality standards for a task. Plugins go one
step further: they ship tools an agent can actually call (MCP servers,
REST APIs, CLI actions).

## Why this collection

- **Breadth with a bar.** 10,598 skills across 287 categories, and a
  written quality contract ([QUALITY.md](QUALITY.md)) that every new
  addition must meet: trigger-rich frontmatter, a step-by-step workflow,
  guardrails, and a worked example or defined output format.
- **Callable, not just readable.** 122 plugins with real MCP servers and
  REST APIs — not prompt packs dressed up as plugins. Where a package
  is a CLI instead, it says so honestly.
- **Validation tooling.** A machine-readable registry
  ([catalog.json](catalog.json)), a generated A–Z index
  ([skills/INDEX.md](skills/INDEX.md)), and a stdlib-only validator
  (`tools/validate.py`) you can run yourself. Counts in this README are
  generated from the tree, not typed from memory.
- **Guardrails throughout.** No fabricated metrics or claims, drafts
  only until a human approves, and consequential actions (pricing,
  contracts, payments, sends) always escalate to a human. See
  [SECURITY.md](SECURITY.md).

## Collection stats (verified from the tree)

| Metric | Count |
|---|---|
| Skills under `skills/` | 10,598 |
| Categories | 107 |
| Plugins | 122 (120 in the GTM Community suite + Resume Optimizer + Auto-GTM Agent) |
| Skill files in total (incl. plugin and template skills) | 5,171 |
| Collection version | 2.0.0 |

Top categories: AI & Automation (307), Sales & Marketing (248),
Content Creation (247), Development (217), Finance (169),
HR & People (160), Operations (151), Data & Analytics (148),
Education (148), Healthcare (137) — plus 97 more. The full registry is
[catalog.json](catalog.json); the browsable index is
[skills/INDEX.md](skills/INDEX.md).

**Collection health:** 5,148 of 10,598 skills (99.6%) carry valid
name+description frontmatter, verified by `tools/validate.py`. The
remaining 20 are legacy files that predate the frontmatter standard;
they are listed as warnings by the validator and are not rewritten in
bulk. Every skill added in v2.0.0 is 100% compliant.

## Install

### Claude Code — plugin marketplace

```text
/plugin marketplace add lionelsimai/claude-skills-collection
/plugin install resume-optimizer@lionel-sim-skills
/plugin install auto-gtm-agent@lionel-sim-skills
/plugin install gtm-community-plugins@lionel-sim-skills
```

### Claude Code / Claude.ai — individual skills

```bash
git clone https://github.com/lionelsimai/claude-skills-collection
cp -r claude-skills-collection/skills/<skill-slug> ~/.claude/skills/
```

Or copy a single `SKILL.md` into a Claude Project and ask Claude to use
the skill — it follows the workflow automatically.

### MCP clients (Claude Desktop, Cursor, Codex, any MCP host)

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

Full plugin guide: [plugins/README.md](plugins/README.md).

## New in v2.0.0 — skills

| Skill | Category | What it does |
|---|---|---|
| [agent-findability-audit](skills/agent-findability-audit/SKILL.md) | AI & Automation | Audit whether AI agents can find a business's prices and next open appointment without forms |
| [agent-plugin-builder](skills/agent-plugin-builder/SKILL.md) | AI & Automation | Design a small quote-and-booking plugin that AI agents can call, with get_quote and book_slot style tools |
| [agent-setup-service](skills/agent-setup-service/SKILL.md) | AI & Automation | Run an always-on AI agent setup service for owner-led businesses, with rulebooks and a client setup pack |
| [ai-avatar-critique](skills/ai-avatar-critique/SKILL.md) | Content Creation | Ruthlessly critique an AI video avatar before it ships, with a verdict, scored dimensions and a timestamped fix list |
| [automation-agency](skills/automation-agency/SKILL.md) | AI & Automation | Sell and deliver outcome-based automation retainers on n8n or Make |
| [career-opportunities](skills/career-opportunities/SKILL.md) | Personal Development | Track career opportunities of all types in one JSON ledger: score fit against the user's own criteria, track pipeline status, deadlines and next actions |
| [design-md](skills/design-md/SKILL.md) | Content Creation | Create an agent-readable DESIGN.md design spec (colours, type, spacing, components, reasoning) before any visual build |
| [follow-up-and-learning-loop](skills/follow-up-and-learning-loop/SKILL.md) | Sales & Marketing | Follow up only with a new reason and learn per segment which campaigns to scale or pause |
| [icp-and-offer-research](skills/icp-and-offer-research/SKILL.md) | Sales & Marketing | Research an offer and build ICP segments before any outreach |
| [invoice-and-reconciliation-integrity](skills/invoice-and-reconciliation-integrity/SKILL.md) | Finance | Prevent invoice and reconciliation errors: never reuse invoice numbers, count every amount once, net refunds, and tie totals to printed statement totals |
| [lead-list-building](skills/lead-list-building/SKILL.md) | Sales & Marketing | Build and clean a lead list from allowed sources only |
| [objection-to-content](skills/objection-to-content/SKILL.md) | Content Creation | Turn sales objections into content ideas and drafts that answer them honestly |
| [personalised-cold-email](skills/personalised-cold-email/SKILL.md) | Sales & Marketing | Draft one personalised cold email per lead from a verified personal signal |
| [project-manager](skills/project-manager/SKILL.md) | Operations | Manage projects end to end: intake, prioritise, track status across parallel builds, and produce standup and weekly-review summaries |
| [reply-triage-and-booking](skills/reply-triage-and-booking/SKILL.md) | Sales & Marketing | Classify outreach replies and act safely by class, escalating pricing and contract replies to a human |
| [sponsor-and-partner-outreach](skills/sponsor-and-partner-outreach/SKILL.md) | Sales & Marketing | Plan and draft sponsor and partner outreach using verified audience numbers only |
| [sponsor-audience-claims](skills/sponsor-audience-claims/SKILL.md) | Sales & Marketing | Verify every audience, attendance and reach number in sponsor material against reconciled source counts before drafting or sending |
| [video-replica](skills/video-replica/SKILL.md) | Content Creation | Recreate a reference video, better: study it frame by frame, rebuild it, and verify quality including sound |
| [voice-ai-receptionist](skills/voice-ai-receptionist/SKILL.md) | AI & Automation | Sell and deliver AI voice receptionists: missed-call recovery, booking and lead qualification |
| [whatsapp-ai-agent](skills/whatsapp-ai-agent/SKILL.md) | AI & Automation | Build and sell WhatsApp AI sales agents for SMEs: instant replies, qualification, booking and follow-up |

All 10,598 skills: [skills/INDEX.md](skills/INDEX.md) ·
[catalog.json](catalog.json)

## Plugins

| Plugin | Path | What it does |
|---|---|---|
| GTM Community Plugins (120 plugins: 60 GTM + 60 Community) | [gtm-community-plugins/](gtm-community-plugins/README.md) | Scoring, triage, checklists, audits, drafts and reports, with MCP + REST servers. Per-plugin registry: [gtm-community-plugins/catalog.json](gtm-community-plugins/catalog.json), human catalog: [gtm-community-plugins/CATALOG.md](gtm-community-plugins/CATALOG.md) |
| Resume Optimizer v2.0.0 (4 MCP tools) | [resume-optimizer/](resume-optimizer/README.md) | ATS scoring, keyword extraction, honest gap analysis, format checks. Skill: [resume-optimizer/SKILL.md](resume-optimizer/SKILL.md). Standalone repo: https://github.com/lionelsimai/lionel-resume-optimizer |
| Auto-GTM Agent v0.1.0 (5 CLI actions) | [auto-gtm-agent/](auto-gtm-agent/README.md) | Human-approved outbound GTM pipeline. Skill: [auto-gtm-agent/SKILL.md](auto-gtm-agent/SKILL.md), plugin contract: [auto-gtm-agent/PLUGIN.md](auto-gtm-agent/PLUGIN.md) |

Plugin index and install snippets: [plugins/README.md](plugins/README.md).

## Repository structure

```text
skills/                  10,598 skills, flat: skills/<slug>/SKILL.md
skills/INDEX.md          generated A-Z index
catalog.json             generated machine-readable registry
.claude-plugin/          root Claude Code marketplace manifest
gtm-community-plugins/   120-plugin suite (own MCP + REST servers)
resume-optimizer/        skill + v2 MCP/REST plugin
auto-gtm-agent/          skill + CLI-actions plugin
skill-template/          the standard SKILL.md template
plugins/                 plugin index and install guide
tools/                   build_catalog.py + validate.py (stdlib only)
tests/                   test_collection.py (stdlib unittest)
docs/                    continuous-integration.md (paste-ready CI)
```

## Verify it yourself

```bash
python3 tools/build_catalog.py   # regenerate catalog.json + skills/INDEX.md
python3 tools/validate.py        # must exit 0
python3 tests/test_collection.py
```

## Guardrails

- **No fabrication** — no invented metrics, clients, audience numbers
  or experience, in skills, plugins or outputs.
- **Draft-only** — outreach and publishing produce drafts; a human
  approves before anything is sent.
- **Human approval** — pricing, contracts, payments and external sends
  always escalate to a human.
- **No secrets in skills** — report anything that looks like a
  credential via [SECURITY.md](SECURITY.md).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and the quality bar in
[QUALITY.md](QUALITY.md). Changes: [CHANGELOG.md](CHANGELOG.md).
CI: [docs/continuous-integration.md](docs/continuous-integration.md).

## License

MIT — see [LICENSE](LICENSE).

---

Built by Lionel Sim, [The AI Capitol](https://theaicapitol.com) |
[LinkedIn](https://sg.linkedin.com/in/lionelshen)
