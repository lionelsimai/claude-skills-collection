# Lionel GTM + Community Plugins — 120 Plugins

120 callable plugins for go-to-market and community management.
One shared MCP server. One shared REST server. No dependencies.

Built by Lionel Sim, Founder The AI Capitol + OpenBuilder
(8,000+ builders, 80+ events, ~15,000 signups), Singapore.
LinkedIn: https://sg.linkedin.com/in/lionelshen — MIT licensed.

## Recommended path first
- Install once via MCP (below). Your agent gets all 120 tools.
- Use REST only if your stack cannot run MCP.
- Full list: [CATALOG.md](CATALOG.md) / [catalog.json](catalog.json)

## What this is
- **Skills teach. Plugins do.** This is the plugin layer for GTM and
  community work: scoring, triage, checklists, gap audits, calculators,
  rankers, planners and draft builders — each a real, distinct tool.
- Deterministic where the job is deterministic. Honest where it drafts:
  supplied facts only, placeholders marked, never invented proof.
- Extends, and does not duplicate, the 6 GTM Skills Collection skills
  and the Auto-GTM Agent.

## Quickstart — MCP clients (Claude Code, Codex, Cursor)
Claude Code:
```text
/plugin marketplace add lionelsimai/gtm-community-plugins
/plugin install gtm-community-plugins@lionel-sim-skills
```
Any MCP client — add to its MCP config:
```json
{"mcpServers": {"gtm-community-plugins": {"command": "python3", "args": ["/path/to/gtm-community-plugins/mcp_server.py"]}}}
```

## Quickstart — REST / GPT Actions
```bash
python3 rest_server.py --port 8787
curl http://localhost:8787/health
curl -X POST http://localhost:8787/tools/nps_calculator -H 'Content-Type: application/json' -d '{"counts": {"promoters": 60, "passives": 25, "detractors": 15, "total_responses": 100}}'
```
- Spec: `openapi.json` (121 paths) — point a GPT Action at it
- Manifest: `ai-plugin.json`

## Category index (20 categories, 6 plugins each)
- **GTM — ICP & Market Research** (6): ICP Fit Scorer, Account Segmentation Planner, Competitor Teardown Checklist, Market Signal Classifier, TAM SAM SOM Calculator, Buyer Persona Gap Audit
- **GTM — Lead Generation** (6): Lead List Deduper, Lead Source Scorer, Lookalike Seed Planner, Event Lead Capture Checklist, Referral Ask Template, Inbound Lead Triage
- **GTM — Lead Scoring & Enrichment** (6): Lead Score Calculator, Enrichment Completeness Audit, Intent Signal Scorer, Lead Priority Ranker, Data Decay Reporter, Champion Tracker Template
- **GTM — Outreach & Sequences** (6): Cold Email Draft Builder, Sequence Cadence Planner, Subject Line Scorer, Follow-up Bump Drafter, LinkedIn Touch Drafter, Outreach Personalisation Audit
- **GTM — Reply & Meeting** (6): Reply Intent Classifier, Objection Response Drafter, Meeting Booking Checklist, No-show Recovery Drafter, Reply SLA Tracker, Meeting Notes Extractor
- **GTM — Sponsors & Partners** (6): Sponsor Fit Scorer, Partner Tier Designer, Sponsor Proposal Audit, Partner Outreach Drafter, Sponsor Deliverable Tracker, Co-marketing Planner
- **GTM — Proposals & Pricing** (6): Proposal Structure Builder, Pricing Page Audit, Discount Guardrail Checker, Quote Follow-up Drafter, ROI Calculator, Proposal Win/Loss Classifier
- **GTM — Pipeline & CRM** (6): Deal Health Scorer, Pipeline Coverage Calculator, Stale Deal Detector, CRM Field Hygiene Audit, Forecast Risk Ranker, Handoff Notes Template
- **GTM — Content & Thought Leadership** (6): Content Idea Scorer, LinkedIn Post Drafter, Case Study Audit, Content Repurposing Planner, Newsletter Section Builder, Speaking Pitch Drafter
- **GTM — Analytics & Learning** (6): Campaign Metrics Reporter, A/B Test Verdict Tool, Segment Learning Logger, Funnel Leak Detector, Weekly GTM Review Builder, Experiment Priority Ranker
- **Community — Member Onboarding** (6): Welcome Message Drafter, Onboarding Checklist Builder, New Member Intro Classifier, Onboarding Drop-off Reporter, Buddy Match Scorer, First-week Plan Builder
- **Community — Events** (6): Event Run Sheet Checklist, Event Idea Scorer, RSVP Conversion Reporter, Speaker Brief Template, Post-event Follow-up Drafter, Waitlist Priority Ranker
- **Community — Engagement** (6): Engagement Health Scorer, Discussion Prompt Drafter, Quiet Member Reactivation Drafter, Engagement Campaign Planner, Top Contributor Spotlight Template, Channel Activity Reporter
- **Community — Retention & Churn** (6): Churn Risk Scorer, Retention Campaign Planner, Exit Feedback Classifier, Member Health Checklist, Win-back Drafter, Cohort Retention Reporter
- **Community — Moderation & Safety** (6): Post Moderation Classifier, Code of Conduct Audit, Spam Signal Scorer, Moderator Escalation Template, Community Guidelines Checklist, Conflict De-escalation Drafter
- **Community — Speakers & Sponsors** (6): Speaker Fit Scorer (Community), Sponsor Activation Checklist, Speaker Outreach Drafter, Sponsor Satisfaction Reporter, Panel Composition Audit, Thank-you Note Drafter
- **Community — Feedback & NPS** (6): NPS Calculator, Feedback Theme Classifier, Survey Design Audit, Feedback Response Drafter, Detractor Recovery Checklist, Feedback Priority Ranker
- **Community — Ambassadors** (6): Ambassador Fit Scorer, Ambassador Onboarding Planner, Ambassador Activity Reporter, Ambassador Brief Template, Ambassador Recognition Drafter, Ambassador Programme Audit
- **Community — Community Analytics** (6): Community Health Reporter, Growth Funnel Reporter, Content Performance Scorer, Member Segment Analyser, Monthly Report Builder, Benchmark Gap Audit
- **Community — Monetisation** (6): Membership Tier Scorer, Sponsored Slot Pricing Calculator, Monetisation Idea Ranker, Paid Event Break-even Calculator, Sponsor Package Builder, Revenue Mix Reporter

## How it works
- `core/registry.py` loads every `plugins/<slug>/plugin.json` + `handler.py`
- `core/engines.py` runs 8 deterministic engines: score, classify, checklist, audit, template, analyze, prioritize, plan
- Each plugin's distinct config (its own criteria, labels, items or sections) drives the engine — no renamed copies
- Add a plugin folder and it registers automatically. No server changes.

## Guardrails — on every tool, every result
- No fabrication: supplied facts only, missing facts marked `[missing: ...]`
- Drafts only: no auto-send, no auto-post, no auto-remove, anywhere
- Human approval required before any draft, plan or classification is acted on
- Audience, sponsor and case-study numbers must be supplied by the user — tools never invent them
- Sample data in this repo is fictional. No real people or client data.

## Test
```bash
python3 tests/test_suite.py
```
- Verifies count, unique slugs, valid folders, all 120 tools callable, MCP handshake, REST smoke test

## Licence
- MIT — see `LICENSE`. Author: Lionel Sim.
