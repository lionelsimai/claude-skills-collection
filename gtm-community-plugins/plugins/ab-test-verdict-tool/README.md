# A/B Test Verdict Tool

Score whether an A/B test result is strong enough to act on, from supplied data.

## Category
- GTM — Analytics & Learning
- Tool kind: `score`

## Tool
- `ab_test_verdict_tool` — Score whether an A/B test result is strong enough to act on, from supplied data.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "metrics": {
      "type": "object",
      "description": "Scores 0-100 keyed by: sample_size, conversion_lift, consistency, effort, downside_risk"
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
    "sample_size": 70,
    "conversion_lift": 70,
    "consistency": 70,
    "effort": 70,
    "downside_risk": 70
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `score`
- `result` — the score result, built only from the inputs and this plugin's items: sample size, conversion lift, consistency, effort, downside risk
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
