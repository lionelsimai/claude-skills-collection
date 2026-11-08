# Monthly Report Builder

Build a monthly community report from supplied metrics only.

## Category
- Community — Community Analytics
- Tool kind: `template`

## Tool
- `monthly_report_builder` — Build a monthly community report from supplied metrics only.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "facts": {
      "type": "object",
      "description": "Supplied facts only, keys include: headline_metric, growth, engagement_highlight_supplied_by_user, challenges, next_month_priority"
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
    "growth": "[supplied: growth]",
    "engagement_highlight_supplied_by_user": "[supplied: engagement highlight supplied by user]"
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `template`
- `result` — the template result, built only from the inputs and this plugin's items: headline metric, growth, engagement highlight supplied by user, challenges, next month priority
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
