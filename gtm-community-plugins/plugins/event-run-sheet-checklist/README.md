# Event Run Sheet Checklist

Check an event run sheet before event day.

## Category
- Community — Events
- Tool kind: `checklist`

## Tool
- `event_run_sheet_checklist` — Check an event run sheet before event day.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "completed": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Completed items from: venue confirmed, speakers confirmed, av tested, registration list, signage, photographer briefed"
    }
  },
  "required": [
    "completed"
  ]
}
```

## Example call
```json
{
  "completed": [
    "venue confirmed",
    "speakers confirmed"
  ]
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `checklist`
- `result` — the checklist result, built only from the inputs and this plugin's items: venue confirmed, speakers confirmed, av tested, registration list, signage, photographer briefed
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
