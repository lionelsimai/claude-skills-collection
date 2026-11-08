# Conflict De-escalation Drafter

Draft a de-escalation reply. Draft only, human moderator sends.

## Category
- Community — Moderation & Safety
- Tool kind: `template`

## Tool
- `conflict_de_escalation_drafter` — Draft a de-escalation reply. Draft only, human moderator sends.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "facts": {
      "type": "object",
      "description": "Supplied facts only, keys include: calm_opening, shared_ground, rule_reminder, private_follow-up_offer"
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
    "calm_opening": "[supplied: calm opening]",
    "shared_ground": "[supplied: shared ground]",
    "rule_reminder": "[supplied: rule reminder]"
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `template`
- `result` — the template result, built only from the inputs and this plugin's items: calm opening, shared ground, rule reminder, private follow-up offer
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
