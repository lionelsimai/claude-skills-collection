# LinkedIn Post Drafter

Draft a LinkedIn post from a supplied insight and example only. Draft only, never auto-posted.

## Category
- GTM — Content & Thought Leadership
- Tool kind: `template`

## Tool
- `linkedin_post_drafter` — Draft a LinkedIn post from a supplied insight and example only. Draft only, never auto-posted.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "facts": {
      "type": "object",
      "description": "Supplied facts only, keys include: hook, supplied_insight, supplied_example, lesson, question_to_readers"
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
    "hook": "[supplied: hook]",
    "supplied_insight": "[supplied: supplied insight]",
    "supplied_example": "[supplied: supplied example]"
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `template`
- `result` — the template result, built only from the inputs and this plugin's items: hook, supplied insight, supplied example, lesson, question to readers
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
