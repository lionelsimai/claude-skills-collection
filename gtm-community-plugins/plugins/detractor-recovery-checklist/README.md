# Detractor Recovery Checklist

Check detractor recovery steps are complete.

## Category
- Community — Feedback & NPS
- Tool kind: `checklist`

## Tool
- `detractor_recovery_checklist` — Check detractor recovery steps are complete.

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
      "description": "Completed items from: acknowledge within 48h, understand issue, offer fix, follow up, log learning"
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
    "acknowledge within 48h",
    "understand issue"
  ]
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `checklist`
- `result` — the checklist result, built only from the inputs and this plugin's items: acknowledge within 48h, understand issue, offer fix, follow up, log learning
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
