# Co-marketing Planner

Plan a co-marketing activity with a partner from a stated goal.

## Category
- GTM — Sponsors & Partners
- Tool kind: `plan`

## Tool
- `co_marketing_planner` — Plan a co-marketing activity with a partner from a stated goal.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "goal": {
      "type": "string"
    },
    "timeframe_days": {
      "type": "integer"
    }
  },
  "required": [
    "goal"
  ]
}
```

## Example call
```json
{
  "goal": "Improve results next quarter with a fictional example team",
  "timeframe_days": 30
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `plan`
- `result` — the plan result, built only from the inputs and this plugin's items: joint audience, shared asset, channel split, owner per side, success metric
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
