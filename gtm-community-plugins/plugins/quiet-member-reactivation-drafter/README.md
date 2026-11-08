# Quiet Member Reactivation Drafter

Draft a reactivation message from supplied facts. Draft only.

## Category
- Community — Engagement
- Tool kind: `template`

## Tool
- `quiet_member_reactivation_drafter` — Draft a reactivation message from supplied facts. Draft only.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "facts": {
      "type": "object",
      "description": "Supplied facts only, keys include: personal_note, what_they_missed_supplied_by_user, low-effort_invite, opt_out_line"
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
    "personal_note": "[supplied: personal note]",
    "what_they_missed_supplied_by_user": "[supplied: what they missed supplied by user]",
    "low-effort_invite": "[supplied: low-effort invite]"
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `template`
- `result` — the template result, built only from the inputs and this plugin's items: personal note, what they missed supplied by user, low-effort invite, opt out line
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
