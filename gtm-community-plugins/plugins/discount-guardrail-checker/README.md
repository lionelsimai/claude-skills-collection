# Discount Guardrail Checker

Score a discount request against guardrails before approval.

## Category
- GTM — Proposals & Pricing
- Tool kind: `score`

## Tool
- `discount_guardrail_checker` — Score a discount request against guardrails before approval.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "metrics": {
      "type": "object",
      "description": "Scores 0-100 keyed by: margin_protected, scope_reduced, payment_terms, expiry_date, approval_level"
    }
  },
  "required": [
    "metrics"
  ]
}
```

## Example call
```json
{
  "metrics": {
    "margin_protected": 70,
    "scope_reduced": 70,
    "payment_terms": 70,
    "expiry_date": 70,
    "approval_level": 70
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `score`
- `result` — the score result, built only from the inputs and this plugin's items: margin protected, scope reduced, payment terms, expiry date, approval level
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
