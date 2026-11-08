# Quote Follow-up Drafter

Draft a quote follow-up from supplied quote facts. Draft only.

## Category
- GTM — Proposals & Pricing
- Tool kind: `template`

## Tool
- `quote_follow_up_drafter` — Draft a quote follow-up from supplied quote facts. Draft only.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "facts": {
      "type": "object",
      "description": "Supplied facts only, keys include: quote_reference, decision_blocker_help, deadline_reminder, next_step"
    }
  },
  "required": [
    "facts"
  ]
}
```

## Example call
```json
{
  "facts": {
    "quote_reference": "[supplied: quote reference]",
    "decision_blocker_help": "[supplied: decision blocker help]",
    "deadline_reminder": "[supplied: deadline reminder]"
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `template`
- `result` — the template result, built only from the inputs and this plugin's items: quote reference, decision blocker help, deadline reminder, next step
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
