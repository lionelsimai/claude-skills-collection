# Ambassador Activity Reporter

Report ambassador programme activity from supplied counts.

## Category
- Community — Ambassadors
- Tool kind: `analyze`

## Tool
- `ambassador_activity_reporter` — Report ambassador programme activity from supplied counts.

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
    "active_ambassadors": 100,
    "events_hosted": 90,
    "posts_made": 80,
    "members_helped": 70,
    "coverage_rate": 60
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `analyze`
- `result` — the analyze result, built only from the inputs and this plugin's items: active ambassadors, events hosted, posts made, members helped, coverage rate
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
