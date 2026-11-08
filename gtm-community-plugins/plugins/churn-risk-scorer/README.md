# Churn Risk Scorer

Score member churn risk from supplied activity signals. Higher inactivity means higher risk.

## Category
- Community — Retention & Churn
- Tool kind: `score`

## Tool
- `churn_risk_scorer` — Score member churn risk from supplied activity signals. Higher inactivity means higher risk.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "metrics": {
      "type": "object",
      "description": "Scores 0-100 keyed by: days_inactive, event_absence, post_decline, support_issues, tenure"
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
    "days_inactive": 70,
    "event_absence": 70,
    "post_decline": 70,
    "support_issues": 70,
    "tenure": 70
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `score`
- `result` — the score result, built only from the inputs and this plugin's items: days inactive, event absence, post decline, support issues, tenure
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
