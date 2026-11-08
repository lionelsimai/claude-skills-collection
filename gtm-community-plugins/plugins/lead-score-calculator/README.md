# Lead Score Calculator

Calculate a transparent lead score from supplied signals.

## Category
- GTM — Lead Scoring & Enrichment
- Tool kind: `score`

## Tool
- `lead_score_calculator` — Calculate a transparent lead score from supplied signals.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "metrics": {
      "type": "object",
      "description": "Scores 0-100 keyed by: firmographic_fit, engagement_recency, page_intent, role_seniority, company_growth"
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
    "firmographic_fit": 70,
    "engagement_recency": 70,
    "page_intent": 70,
    "role_seniority": 70,
    "company_growth": 70
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `score`
- `result` — the score result, built only from the inputs and this plugin's items: firmographic fit, engagement recency, page intent, role seniority, company growth
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
