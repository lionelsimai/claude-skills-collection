# Meeting Booking Checklist

Check a meeting booking flow before the invite goes out.

## Category
- GTM — Reply & Meeting
- Tool kind: `checklist`

## Tool
- `meeting_booking_checklist` — Check a meeting booking flow before the invite goes out.

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
      "description": "Completed items from: two time options, timezone stated, calendar invite, agenda line, reminder set"
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
    "two time options",
    "timezone stated"
  ]
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `checklist`
- `result` — the checklist result, built only from the inputs and this plugin's items: two time options, timezone stated, calendar invite, agenda line, reminder set
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
