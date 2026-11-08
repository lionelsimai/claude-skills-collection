# Speaker Fit Scorer (Community)

Score a speaker for a community event from supplied information.

## Category
- Community — Speakers & Sponsors
- Tool kind: `score`

## Tool
- `speaker_fit_scorer_community` — Score a speaker for a community event from supplied information.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "metrics": {
      "type": "object",
      "description": "Scores 0-100 keyed by: topic_relevance, audience_level, talk_experience, diversity_of_perspective, availability"
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
    "topic_relevance": 70,
    "audience_level": 70,
    "talk_experience": 70,
    "diversity_of_perspective": 70,
    "availability": 70
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `score`
- `result` — the score result, built only from the inputs and this plugin's items: topic relevance, audience level, talk experience, diversity of perspective, availability
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
