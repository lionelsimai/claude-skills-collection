# Quality Bar

This is the contract every skill and plugin in this collection must meet.
It exists so the collection stays world-class as it grows: breadth means
nothing if a user cannot trust the next file they open.

## Every skill must have

- [ ] YAML frontmatter with `name` and a trigger-rich `description`
      (say what it does AND the phrases/situations that should trigger it),
      plus `category`, `license` and `version`.
- [ ] A "When to use" section (or an equivalent Purpose/Overview section
      that makes the trigger situations explicit).
- [ ] A step-by-step workflow a competent agent can follow without
      inventing the missing steps.
- [ ] Guardrails and quality checks: what never to do, what to verify,
      and how to check the output before delivering it.
- [ ] At least one worked example or a defined output format.
- [ ] No fabricated claims: no invented metrics, clients, attendance
      figures or results anywhere in the text or examples. Example
      numbers must be clearly illustrative or sourced.
- [ ] No private data: no personal names, home-directory paths, account
      details or one person's private constraints. Generalise.

## Every plugin must have

- [ ] A valid manifest (`plugin.json`, `marketplace.json` or
      `ai-plugin.json`) that parses as JSON and whose paths exist.
- [ ] An honest transport story: claim an MCP server only if the package
      actually ships one; document CLI or REST contracts as what they are.
- [ ] Code that runs on the Python 3 standard library only, unless the
      dependency is named, justified and pinned in the plugin's README.
- [ ] Smoke tests for callable tools, and a README with install and
      usage snippets that were actually run.

## Before submitting

1. Run `python3 tools/build_catalog.py` to regenerate `catalog.json`
   and `skills/INDEX.md`.
2. Run `python3 tools/validate.py` — it must exit 0, and your new files
   must add zero warnings.
3. Run `python3 tests/test_collection.py` — all tests must pass.
4. Read your own skill once as if you were the agent receiving it cold.
   If a step needs knowledge only you have, write it into the skill.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the submission process.
