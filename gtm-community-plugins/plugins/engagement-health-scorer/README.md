# Engagement Health Scorer

Score community engagement health from supplied metrics.

## Category
- Community — Engagement
- Tool kind: `score`

## Tool
- `engagement_health_scorer` — Score community engagement health from supplied metrics.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "metrics": {
      "type": "object",
      "description": "Scores 0-100 keyed by: active_member_rate, posts_per_week, reply_rate, event_attendance, new_member_activation"
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
    "active_member_rate": 70,
    "posts_per_week": 70,
    "reply_rate": 70,
    "event_attendance": 70,
    "new_member_activation": 70
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `score`
- `result` — the score result, built only from the inputs and this plugin's items: active member rate, posts per week, reply rate, event attendance, new member activation
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
