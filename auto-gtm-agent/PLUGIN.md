# Auto-GTM Agent — Plugin Contract

Auto-GTM Agent is **not** an MCP server. It is a Python 3 (stdlib-only) CLI
package plus an actions manifest (`plugin.json` in this folder). This file
documents that contract so any agent host can wire the actions up honestly —
do not register a non-existent MCP server for it.

## Actions (from plugin.json)

| Action | Command template | What it does |
|---|---|---|
| `learn_offer` | `python3 -m autogtm --config {config_path} validate` | Load and validate a business config: sender, offer ladder, segments, banned words, allowed proof points and booking link. Call first, before scoring or drafting. |
| `score_icp` | `python3 -m autogtm --config {config_path} score --leads {leads_csv}` | Score a leads CSV against the ICP segments. Returns fit 0 to 100, tier A/B/C and auditable reasons per lead. Dedupes and drops invalid or suppressed emails. |
| `draft_emails` | `python3 -m autogtm --config {config_path} draft --leads {leads_csv} --out {out_path}` | Draft one personal email per tier A/B lead that has a checkable personal signal. Every draft is status draft_needs_approval. Leads without a signal are blocked, never blasted generically. Nothing is sent. |
| `triage_reply` | `python3 -m autogtm --config {config_path} triage --text {reply_text}` | Classify a reply as hot, hot_escalate, negative, out_of_office or warm_unclear, with the safe next action. Pricing and contract replies always escalate to a human. |
| `learn_results` | `python3 -m autogtm --config {config_path} learn --results {results_csv}` | From campaign results (segment, sent, hot leads), compute cost per hot lead and return scale, pause or keep_testing per segment. |

## Rules

- Every drafted email carries status `draft_needs_approval`. Nothing is sent
  by this plugin; a human approves before any sending step exists.
- Leads without a checkable personal signal are blocked, never blasted
  generically.
- Pricing, contract, legal, procurement and security replies always escalate
  to a human.

## Claude Code

The `.claude-plugin/plugin.json` in this folder is a metadata-only Claude
Code plugin manifest (no `mcpServers` entry, because the package provides
none). The skill in `SKILL.md` drives the CLI in `src/`.
