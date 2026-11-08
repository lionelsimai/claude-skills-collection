# Proposal Win/Loss Classifier

Classify a lost or won proposal outcome from supplied notes.

## Category
- GTM — Proposals & Pricing
- Tool kind: `classify`

## Tool
- `proposal_win_loss_classifier` — Classify a lost or won proposal outcome from supplied notes.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "text": {
      "type": "string"
    }
  },
  "required": [
    "text"
  ]
}
```

## Example call
```json
{
  "text": "This is about price and needs review."
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `classify`
- `result` — the classify result, built only from the inputs and this plugin's items: price, budget frozen, competitor chosen, timing, no response, champion left
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
