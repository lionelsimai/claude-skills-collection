# Continuous Integration

This repository's checks are two stdlib-only commands:

```bash
python3 tools/validate.py
python3 tests/test_collection.py
```

## GitHub Actions workflow (paste-ready)

This workflow is **not** committed under `.github/workflows/` in the
automated push, because the GitHub App integration used to publish this
repository does not have the `workflow` scope — GitHub rejects pushes
that create or change workflow files without it. Add it once through
the GitHub web editor: create `.github/workflows/validate.yml` in the
repo UI and paste the YAML below.

```yaml
name: Validate collection

on:
  push:
  pull_request:

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Build catalog and check it is current
        run: |
          python3 tools/build_catalog.py
          git diff --exit-code catalog.json skills/INDEX.md
      - name: Validate collection
        run: python3 tools/validate.py
      - name: Run tests
        run: python3 tests/test_collection.py
      - name: Resume Optimizer plugin smoke tests
        run: python3 resume-optimizer/plugin/tests/test_plugin.py
```

## What each step proves

- **Catalog freshness** — `catalog.json` and `skills/INDEX.md` are
  generated files; CI fails if a PR adds a skill without regenerating
  them.
- **Validate** — every JSON manifest parses, every marketplace plugin
  path exists, catalog counts match the folders on disk, README links
  resolve, and frontmatter compliance is reported.
- **Tests** — the frontmatter parser, the new-skill quality gates
  (When to use, guardrails, example/output, sanitisation) and the
  marketplace/catalog checks.
- **Plugin smoke tests** — the Resume Optimizer MCP tools and REST
  routes actually answer.
