# Monetisation Idea Ranker

Rank monetisation ideas protecting member goodwill.

## Category
- Community — Monetisation
- Tool kind: `prioritize`

## Tool
- `monetisation_idea_ranker` — Rank monetisation ideas protecting member goodwill.

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
- `result` — the prioritize result, built only from the inputs and this plugin's items: revenue potential, member goodwill, effort, sponsor fit, speed to launch
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
