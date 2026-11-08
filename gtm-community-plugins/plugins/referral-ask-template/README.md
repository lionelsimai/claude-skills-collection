# Referral Ask Template

Draft a referral ask from supplied facts only. Draft only, never sent automatically.

## Category
- GTM — Lead Generation
- Tool kind: `template`

## Tool
- `referral_ask_template` — Draft a referral ask from supplied facts only. Draft only, never sent automatically.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "facts": {
      "type": "object",
      "description": "Supplied facts only, keys include: context, reason_for_asking, specific_person_type, easy_yes_path, thank_you_note"
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
    "context": "[supplied: context]",
    "reason_for_asking": "[supplied: reason for asking]",
    "specific_person_type": "[supplied: specific person type]"
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `template`
- `result` — the template result, built only from the inputs and this plugin's items: context, reason for asking, specific person type, easy yes path, thank you note
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
