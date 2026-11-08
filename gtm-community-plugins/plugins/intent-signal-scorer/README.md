# Intent Signal Scorer

Score buying intent from supplied behavioural signals.

## Category
- GTM — Lead Scoring & Enrichment
- Tool kind: `score`

## Tool
- `intent_signal_scorer` — Score buying intent from supplied behavioural signals.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "metrics": {
      "type": "object",
      "description": "Scores 0-100 keyed by: pricing_page_visits, comparison_searches, repeat_visits, content_depth, recency"
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
    "pricing_page_visits": 70,
    "comparison_searches": 70,
    "repeat_visits": 70,
    "content_depth": 70,
    "recency": 70
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `score`
- `result` — the score result, built only from the inputs and this plugin's items: pricing page visits, comparison searches, repeat visits, content depth, recency
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
