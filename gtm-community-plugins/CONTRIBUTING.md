# Contributing

## Rules
- Stdlib Python only. No dependencies, no network calls, no credentials.
- Keep the guardrails: no fabrication, drafts only, human approval, no auto-send.
- Fictional sample data only. No real people, clients or metrics.
- A new plugin needs: `plugins/<slug>/plugin.json`, `README.md`, `handler.py`, and a sample input that runs.

## Add a plugin
- Copy an existing plugin folder, change its slug, description and config items
- Run `python3 tests/test_suite.py` — it must pass, including your new tool

## Licence
- Contributions are under MIT.
