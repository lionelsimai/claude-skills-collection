# Auto-GTM Agent

An open-source, human-approved outbound GTM agent for personal AI agents.
Built by Lionel Sim (The AI Capitol) as the own-your-stack alternative to
hosted auto-GTM tools like Explee.

Give it your offer, it helps you:

1. **Learn what you sell** — from a config you control, with an allow-list of proof points it may use. It cannot invent claims.
2. **Figure out who buys it** — ICP segments with transparent scoring (role, company, region, size, signal). Every score comes with reasons.
3. **Find those exact people** — from leads *you* supply (CSV import, dedupe, validation, suppression). No scraped proprietary database, no attendee PII hoarding.
4. **Write each a personal email** — one draft per lead, built around one true, checkable personal signal. No signal = no draft. Every draft needs human approval.
5. **Handle replies** — triage into hot / escalate / negative / out-of-office. Pricing and contract replies always go to a human, never auto-answered.
6. **Learn and double down** — cost per hot lead by segment, with scale / pause / keep-testing verdicts.

## What it deliberately does not do (v0.1)

- It does **not send email**. Sending belongs behind an explicit approval step, on a separate warmed domain, never your primary domain. Hosted tools hide this risk; this project makes it visible.
- It does **not come with a lead database**. Bring leads from sources you have a right to contact.
- It does **not fabricate proof**. If a claim is not in `allowed_proof`, the agent cannot use it.

## Quick start

```bash
cd auto-gtm-agent
pip install pyyaml          # the only dependency
export PYTHONPATH=$PWD/src

# 1. Validate the bundled example config for The AI Capitol
python3 -m autogtm --config config/the-ai-capitol.yaml validate

# 2. Run the full demo on fictional sample leads
python3 -m autogtm demo
# -> demo-output/demo-report.json

# 3. Score and draft from your own leads
python3 -m autogtm --config config/your-business.yaml score --leads leads.csv
python3 -m autogtm --config config/your-business.yaml draft --leads leads.csv --out drafts.json

# 4. Triage a reply, and review a campaign
python3 -m autogtm --config config/your-business.yaml triage --text "Send pricing, can we talk Tuesday?"
python3 -m autogtm --config config/your-business.yaml learn --results results.csv
```

Copy `config/example.yaml` to start your own business config.
Sample leads in `examples/` are fictional and exist to show the pipeline.

## Use it as a skill / plugin

- `SKILL.md` + `skill.yaml` — install as an agent skill (Muse, Hermes-style agents, and other SKILL.md-compatible runtimes).
- `plugin.json` — a personal-agent plugin manifest declaring five actions: `learn_offer`, `score_icp`, `draft_emails`, `triage_reply`, `learn_results`.

## Tests

```bash
python3 -m pytest tests/ -q
```

## Roadmap

- v0.2: approval-gated sender adapter (separate warmed domain, explicit `--i-approved` flag, daily cap enforced in code)
- v0.2: enrichment adapters (bring-your-own API key) for lead sources
- v0.3: reply inbox watcher that drafts, never sends, escalations

## License

MIT. See `LICENSE`.
