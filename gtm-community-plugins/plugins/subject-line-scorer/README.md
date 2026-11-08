# Subject Line Scorer

Score a subject line before it is used. Spam-trigger risk is scored inversely.

## Category
- GTM — Outreach & Sequences
- Tool kind: `score`

## Tool
- `subject_line_scorer` — Score a subject line before it is used. Spam-trigger risk is scored inversely.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "metrics": {
      "type": "object",
      "description": "Scores 0-100 keyed by: length, personalisation, specificity, curiosity, spam_trigger_risk"
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
    "length": 70,
    "personalisation": 70,
    "specificity": 70,
    "curiosity": 70,
    "spam_trigger_risk": 70
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `score`
- `result` — the score result, built only from the inputs and this plugin's items: length, personalisation, specificity, curiosity, spam trigger risk
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
