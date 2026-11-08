# Stale Deal Detector

Flag stale deals from a supplied checklist of deal hygiene items.

## Category
- GTM — Pipeline & CRM
- Tool kind: `checklist`

## Tool
- `stale_deal_detector` — Flag stale deals from a supplied checklist of deal hygiene items.

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
      "description": "Completed items from: last activity date, next step, stage age, owner assigned, close date updated"
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
    "last activity date",
    "next step"
  ]
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `checklist`
- `result` — the checklist result, built only from the inputs and this plugin's items: last activity date, next step, stage age, owner assigned, close date updated
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
