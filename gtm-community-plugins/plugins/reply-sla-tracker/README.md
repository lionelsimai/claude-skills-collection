# Reply SLA Tracker

Report reply SLA performance from supplied counts.

## Category
- GTM — Reply & Meeting
- Tool kind: `analyze`

## Tool
- `reply_sla_tracker` — Report reply SLA performance from supplied counts.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "counts": {
      "type": "object"
    },
    "amounts": {
      "type": "object"
    },
    "series": {
      "type": "array",
      "items": {
        "type": "number"
      }
    }
  },
  "required": []
}
```

## Example call
```json
{
  "counts": {
    "replies_received": 100,
    "replies_answered": 90,
    "in_time": 80,
    "in_late": 70,
    "average_response_hours": 60
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `analyze`
- `result` — the analyze result, built only from the inputs and this plugin's items: replies received, replies answered, in time, in late, average response hours
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
