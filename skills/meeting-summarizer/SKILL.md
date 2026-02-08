---
name: meeting-summarizer
description: |
  Summarize meetings with key decisions, action items, and follow-ups.
  TRIGGERS - Use when user wants to summarize a meeting, call, or discussion.
---

# Meeting Summarizer

## Overview
Transforms meeting notes, transcripts, or recordings into structured summaries with decisions, action items, and next steps.

## Workflow

### Step 1: Get the Input
Accept meeting notes, transcript, or audio transcription. Ask for:
1. **Meeting type**: Team sync, client call, strategy session, 1:1?
2. **Attendees**: Who was there?
3. **Context**: What was the meeting about?

### Step 2: Extract & Organize

**Summary Structure:**
```markdown
# Meeting Summary: [Title]
**Date**: [Date] | **Duration**: [Length] | **Attendees**: [Names]

## TL;DR
[2-3 sentence summary of the most important outcomes]

## Key Decisions Made
1. [Decision 1] — Owner: [Name]
2. [Decision 2] — Owner: [Name]

## Action Items
| Action | Owner | Due Date | Priority |
|--------|-------|----------|----------|
| [Task] | [Name] | [Date] | High/Med/Low |

## Discussion Highlights
### [Topic 1]
- [Key point]
- [Key point]

### [Topic 2]
- [Key point]

## Open Questions / Parking Lot
- [Question that wasn't resolved]

## Next Meeting
- **Date**: [if scheduled]
- **Agenda items**: [carry-forward topics]
```

## Quality Checklist
- [ ] Every action item has an owner and due date
- [ ] Decisions are clearly stated (not buried in discussion)
- [ ] TL;DR captures the essence in under 3 sentences
- [ ] Open questions captured for follow-up
