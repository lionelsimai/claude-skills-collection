# Engagement Campaign Planner

Plan a four-week engagement campaign.

## Category
- Community — Engagement
- Tool kind: `plan`

## Tool
- `engagement_campaign_planner` — Plan a four-week engagement campaign.

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
- `result` — the plan result, built only from the inputs and this plugin's items: pick theme, week 1 prompt, week 2 challenge, week 3 spotlight, week 4 event tie-in
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
