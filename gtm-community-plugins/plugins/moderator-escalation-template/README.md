# Moderator Escalation Template

Render a moderation escalation record from supplied evidence only.

## Category
- Community — Moderation & Safety
- Tool kind: `template`

## Tool
- `moderator_escalation_template` — Render a moderation escalation record from supplied evidence only.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "facts": {
      "type": "object",
      "description": "Supplied facts only, keys include: incident_summary, evidence_supplied_by_moderator, rule_reference, action_taken, appeal_note"
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
    "incident_summary": "[supplied: incident summary]",
    "evidence_supplied_by_moderator": "[supplied: evidence supplied by moderator]",
    "rule_reference": "[supplied: rule reference]"
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `template`
- `result` — the template result, built only from the inputs and this plugin's items: incident summary, evidence supplied by moderator, rule reference, action taken, appeal note
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
