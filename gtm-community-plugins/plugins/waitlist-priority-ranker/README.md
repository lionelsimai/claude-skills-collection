# Waitlist Priority Ranker

Rank a waitlist fairly from supplied criteria.

## Category
- Community — Events
- Tool kind: `prioritize`

## Tool
- `waitlist_priority_ranker` — Rank a waitlist fairly from supplied criteria.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "items": {
      "type": "array",
      "items": {
        "type": "object"
      }
    }
  },
  "required": [
    "items"
  ]
}
```

## Example call
```json
{
  "items": [
    {
      "name": "Example 1",
      "impact": 8,
      "effort": 2
    },
    {
      "name": "Example 2",
      "impact": 7,
      "effort": 3
    },
    {
      "name": "Example 3",
      "impact": 6,
      "effort": 4
    }
  ]
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `prioritize`
- `result` — the prioritize result, built only from the inputs and this plugin's items: member tenure, rsvp speed, past attendance, contribution, effort
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
