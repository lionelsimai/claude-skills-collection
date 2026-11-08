# Membership Tier Scorer

Score a paid membership tier design. Sponsors pay first in Lionel's model, member paywalls need explicit review.

## Category
- Community — Monetisation
- Tool kind: `score`

## Tool
- `membership_tier_scorer` — Score a paid membership tier design. Sponsors pay first in Lionel's model, member paywalls need explicit review.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "metrics": {
      "type": "object",
      "description": "Scores 0-100 keyed by: value_delivered, price_fit, exclusivity, delivery_cost, support_load"
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
    "value_delivered": 70,
    "price_fit": 70,
    "exclusivity": 70,
    "delivery_cost": 70,
    "support_load": 70
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `score`
- `result` — the score result, built only from the inputs and this plugin's items: value delivered, price fit, exclusivity, delivery cost, support load
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
