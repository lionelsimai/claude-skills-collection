# Weekly GTM Review Builder

Build a weekly GTM review from supplied metrics only.

## Category
- GTM — Analytics & Learning
- Tool kind: `template`

## Tool
- `weekly_gtm_review_builder` — Build a weekly GTM review from supplied metrics only.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "facts": {
      "type": "object",
      "description": "Supplied facts only, keys include: headline_metric, wins, losses, lessons, one_priority"
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
    "headline_metric": "[supplied: headline metric]",
    "wins": "[supplied: wins]",
    "losses": "[supplied: losses]"
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `template`
- `result` — the template result, built only from the inputs and this plugin's items: headline metric, wins, losses, lessons, one priority
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
