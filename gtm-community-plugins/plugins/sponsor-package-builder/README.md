# Sponsor Package Builder

Build a sponsor package from supplied audience facts and deliverables only.

## Category
- Community — Monetisation
- Tool kind: `template`

## Tool
- `sponsor_package_builder` — Build a sponsor package from supplied audience facts and deliverables only.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "facts": {
      "type": "object",
      "description": "Supplied facts only, keys include: audience_supplied_by_user, deliverables, term, investment, reporting"
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
    "audience_supplied_by_user": "[supplied: audience supplied by user]",
    "deliverables": "[supplied: deliverables]",
    "term": "[supplied: term]"
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `template`
- `result` — the template result, built only from the inputs and this plugin's items: audience supplied by user, deliverables, term, investment, reporting
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
