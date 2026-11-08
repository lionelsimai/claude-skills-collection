# ICP Fit Scorer

Score an account against your ideal customer profile on five weighted criteria.

## Category
- GTM — ICP & Market Research
- Tool kind: `score`

## Tool
- `icp_fit_scorer` — Score an account against your ideal customer profile on five weighted criteria.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "metrics": {
      "type": "object",
      "description": "Scores 0-100 keyed by: company_size_fit, industry_match, geography_fit, technology_fit, buying_signal_strength"
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
    "company_size_fit": 70,
    "industry_match": 70,
    "geography_fit": 70,
    "technology_fit": 70,
    "buying_signal_strength": 70
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `score`
- `result` — the score result, built only from the inputs and this plugin's items: company size fit, industry match, geography fit, technology fit, buying signal strength
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
