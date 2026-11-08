# Spam Signal Scorer

Score spam signals in a post from supplied indicators. Flag for human review only.

## Category
- Community — Moderation & Safety
- Tool kind: `score`

## Tool
- `spam_signal_scorer` — Score spam signals in a post from supplied indicators. Flag for human review only.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "metrics": {
      "type": "object",
      "description": "Scores 0-100 keyed by: link_density, new_account, repeated_text, keyword_stuffing, report_count"
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
    "link_density": 70,
    "new_account": 70,
    "repeated_text": 70,
    "keyword_stuffing": 70,
    "report_count": 70
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `score`
- `result` — the score result, built only from the inputs and this plugin's items: link density, new account, repeated text, keyword stuffing, report count
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
