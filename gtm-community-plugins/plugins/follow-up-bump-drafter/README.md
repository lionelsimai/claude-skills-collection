# Follow-up Bump Drafter

Draft a short follow-up bump from supplied facts only. Draft only.

## Category
- GTM — Outreach & Sequences
- Tool kind: `template`

## Tool
- `follow_up_bump_drafter` — Draft a short follow-up bump from supplied facts only. Draft only.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "facts": {
      "type": "object",
      "description": "Supplied facts only, keys include: thread_reference, new_value_point, choice_question, easy_opt_out"
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
    "thread_reference": "[supplied: thread reference]",
    "new_value_point": "[supplied: new value point]",
    "choice_question": "[supplied: choice question]"
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `template`
- `result` — the template result, built only from the inputs and this plugin's items: thread reference, new value point, choice question, easy opt out
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
