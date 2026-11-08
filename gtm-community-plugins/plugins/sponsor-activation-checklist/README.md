# Sponsor Activation Checklist

Check sponsor activation readiness for a community event.

## Category
- Community — Speakers & Sponsors
- Tool kind: `checklist`

## Tool
- `sponsor_activation_checklist` — Check sponsor activation readiness for a community event.

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
      "description": "Completed items from: logo assets, booth plan, speaking slot, lead capture, post-event report date"
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
    "logo assets",
    "booth plan"
  ]
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `checklist`
- `result` — the checklist result, built only from the inputs and this plugin's items: logo assets, booth plan, speaking slot, lead capture, post-event report date
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
