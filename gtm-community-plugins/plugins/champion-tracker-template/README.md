# Champion Tracker Template

Render a champion tracking sheet from supplied facts only.

## Category
- GTM — Lead Scoring & Enrichment
- Tool kind: `template`

## Tool
- `champion_tracker_template` — Render a champion tracking sheet from supplied facts only.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "facts": {
      "type": "object",
      "description": "Supplied facts only, keys include: champion_name, role, influence_level, last_contact, next_action"
    }
  },
  "required": [
    "facts"
  ]
}
```

## Example call
```json
{
  "facts": {
    "champion_name": "[supplied: champion name]",
    "role": "[supplied: role]",
    "influence_level": "[supplied: influence level]"
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `template`
- `result` — the template result, built only from the inputs and this plugin's items: champion name, role, influence level, last contact, next action
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
