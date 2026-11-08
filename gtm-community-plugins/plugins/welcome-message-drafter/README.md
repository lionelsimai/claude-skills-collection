# Welcome Message Drafter

Draft a welcome message from supplied community facts. Draft only.

## Category
- Community — Member Onboarding
- Tool kind: `template`

## Tool
- `welcome_message_drafter` — Draft a welcome message from supplied community facts. Draft only.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "facts": {
      "type": "object",
      "description": "Supplied facts only, keys include: member_name_supplied_by_user, first_step, introduce-yourself_prompt, key_resource"
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
    "member_name_supplied_by_user": "[supplied: member name supplied by user]",
    "first_step": "[supplied: first step]",
    "introduce-yourself_prompt": "[supplied: introduce-yourself prompt]"
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `template`
- `result` — the template result, built only from the inputs and this plugin's items: member name supplied by user, first step, introduce-yourself prompt, key resource
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
