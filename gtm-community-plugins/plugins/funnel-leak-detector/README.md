# Funnel Leak Detector

Identify the weakest funnel stage from supplied completion items.

## Category
- GTM — Analytics & Learning
- Tool kind: `checklist`

## Tool
- `funnel_leak_detector` — Identify the weakest funnel stage from supplied completion items.

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
      "description": "Completed items from: visit to signup, signup to reply, reply to meeting, meeting to proposal, proposal to close"
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
    "visit to signup",
    "signup to reply"
  ]
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `checklist`
- `result` — the checklist result, built only from the inputs and this plugin's items: visit to signup, signup to reply, reply to meeting, meeting to proposal, proposal to close
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
