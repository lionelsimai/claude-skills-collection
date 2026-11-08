# Paid Event Break-even Calculator

Calculate break-even ticket sales from supplied costs and price.

## Category
- Community — Monetisation
- Tool kind: `analyze`

## Tool
- `paid_event_break_even_calculator` — Calculate break-even ticket sales from supplied costs and price.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "counts": {
      "type": "object"
    },
    "amounts": {
      "type": "object"
    },
    "series": {
      "type": "array",
      "items": {
        "type": "number"
      }
    }
  },
  "required": []
}
```

## Example call
```json
{
  "counts": {
    "venue_cost": 2000,
    "food_cost": 1500,
    "other_costs": 500,
    "ticket_price": 50
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `analyze`
- `result` — the analyze result, built only from the inputs and this plugin's items: venue cost, food cost, other costs, ticket price, break-even tickets
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
