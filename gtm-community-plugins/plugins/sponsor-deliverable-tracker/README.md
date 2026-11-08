# Sponsor Deliverable Tracker

Track sponsor deliverables promised versus delivered.

## Category
- GTM — Sponsors & Partners
- Tool kind: `checklist`

## Tool
- `sponsor_deliverable_tracker` — Track sponsor deliverables promised versus delivered.

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
      "description": "Completed items from: logo placed, speaking slot, lead list shared, social post, post-event report"
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
    "logo placed",
    "speaking slot"
  ]
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `checklist`
- `result` — the checklist result, built only from the inputs and this plugin's items: logo placed, speaking slot, lead list shared, social post, post-event report
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
