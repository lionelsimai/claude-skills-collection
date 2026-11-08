# Member Health Checklist

Check member health signals for a cohort review.

## Category
- Community — Retention & Churn
- Tool kind: `checklist`

## Tool
- `member_health_checklist` — Check member health signals for a cohort review.

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
      "description": "Completed items from: logged in recently, attended event, posted or replied, used a resource, gave feedback"
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
    "logged in recently",
    "attended event"
  ]
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `checklist`
- `result` — the checklist result, built only from the inputs and this plugin's items: logged in recently, attended event, posted or replied, used a resource, gave feedback
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
