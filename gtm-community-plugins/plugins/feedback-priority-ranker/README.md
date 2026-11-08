# Feedback Priority Ranker

Rank feedback themes by mentions and effort.

## Category
- Community — Feedback & NPS
- Tool kind: `prioritize`

## Tool
- `feedback_priority_ranker` — Rank feedback themes by mentions and effort.

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
- `result` — the prioritize result, built only from the inputs and this plugin's items: mentions, severity, member impact, effort to fix, strategic fit
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
