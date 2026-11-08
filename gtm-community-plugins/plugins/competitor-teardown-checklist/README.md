# Competitor Teardown Checklist

Audit a competitor teardown for completeness before it is used in planning.

## Category
- GTM — ICP & Market Research
- Tool kind: `checklist`

## Tool
- `competitor_teardown_checklist` — Audit a competitor teardown for completeness before it is used in planning.

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
      "description": "Completed items from: positioning statement, pricing page, feature matrix, customer proof, content themes, call to action"
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
    "positioning statement",
    "pricing page"
  ]
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `checklist`
- `result` — the checklist result, built only from the inputs and this plugin's items: positioning statement, pricing page, feature matrix, customer proof, content themes, call to action
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
