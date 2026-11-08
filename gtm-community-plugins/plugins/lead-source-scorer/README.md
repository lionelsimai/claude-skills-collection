# Lead Source Scorer

Score a lead source so budget goes to sources that convert.

## Category
- GTM — Lead Generation
- Tool kind: `score`

## Tool
- `lead_source_scorer` — Score a lead source so budget goes to sources that convert.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "metrics": {
      "type": "object",
      "description": "Scores 0-100 keyed by: conversion_rate, cost_per_lead, data_completeness, reply_rate, unsubscribe_rate"
    }
  },
  "required": [
    "metrics"
  ]
}
```

## Example call
```json
{
  "metrics": {
    "conversion_rate": 70,
    "cost_per_lead": 70,
    "data_completeness": 70,
    "reply_rate": 70,
    "unsubscribe_rate": 70
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `score`
- `result` — the score result, built only from the inputs and this plugin's items: conversion rate, cost per lead, data completeness, reply rate, unsubscribe rate
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
