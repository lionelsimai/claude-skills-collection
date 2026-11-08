# Content Idea Scorer

Score a content idea before production time is spent.

## Category
- GTM — Content & Thought Leadership
- Tool kind: `score`

## Tool
- `content_idea_scorer` — Score a content idea before production time is spent.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "metrics": {
      "type": "object",
      "description": "Scores 0-100 keyed by: audience_relevance, originality, proof_available, effort_to_produce, distribution_fit"
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
    "audience_relevance": 70,
    "originality": 70,
    "proof_available": 70,
    "effort_to_produce": 70,
    "distribution_fit": 70
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `score`
- `result` — the score result, built only from the inputs and this plugin's items: audience relevance, originality, proof available, effort to produce, distribution fit
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
