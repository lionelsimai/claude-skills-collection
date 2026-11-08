# Onboarding Checklist Builder

Check a new member onboarding journey for completion.

## Category
- Community — Member Onboarding
- Tool kind: `checklist`

## Tool
- `onboarding_checklist_builder` — Check a new member onboarding journey for completion.

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
      "description": "Completed items from: profile complete, introduction posted, starter resource read, first event rsvp, buddy assigned"
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
    "profile complete",
    "introduction posted"
  ]
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `checklist`
- `result` — the checklist result, built only from the inputs and this plugin's items: profile complete, introduction posted, starter resource read, first event rsvp, buddy assigned
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
