# Cold Email Draft Builder

Draft a cold email from one supplied personal signal and supplied proof only. Draft only.

## Category
- GTM — Outreach & Sequences
- Tool kind: `template`

## Tool
- `cold_email_draft_builder` — Draft a cold email from one supplied personal signal and supplied proof only. Draft only.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "facts": {
      "type": "object",
      "description": "Supplied facts only, keys include: subject_line, personal_signal, problem_statement, relevant_proof_supplied_by_user, soft_call_to_action"
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
    "subject_line": "[supplied: subject line]",
    "personal_signal": "[supplied: personal signal]",
    "problem_statement": "[supplied: problem statement]"
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `template`
- `result` — the template result, built only from the inputs and this plugin's items: subject line, personal signal, problem statement, relevant proof supplied by user, soft call to action
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
