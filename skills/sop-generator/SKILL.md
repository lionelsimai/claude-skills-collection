---
name: sop-generator
description: |
  Create clear, step-by-step Standard Operating Procedures for any business process.
  
  TRIGGERS - Use this skill when:
  - User wants to document a process or create an SOP
  - User mentions standard operating procedures, process documentation, or playbooks
  - User wants to create repeatable workflows for their team
---

# SOP Generator

## Overview

Creates clear, actionable SOPs that anyone can follow. Includes step-by-step instructions, decision trees, quality checks, and troubleshooting guides.

## Workflow

### Step 1: Understand the Process

Ask the user:
1. **Process name**: What is this SOP for?
2. **Who performs it**: Role/person responsible
3. **Frequency**: How often is this done?
4. **Steps**: Walk me through it (or describe the outcome)
5. **Tools needed**: Software, access, or resources required
6. **Common mistakes**: What goes wrong?

### Step 2: Structure the SOP

```markdown
# SOP: [Process Name]

## Document Info
| Field | Value |
|-------|-------|
| **Version** | 1.0 |
| **Created** | [Date] |
| **Owner** | [Name/Role] |
| **Frequency** | [How often] |
| **Est. Time** | [Duration] |
| **Last Updated** | [Date] |

## Purpose
[One sentence: why this process exists and what it achieves]

## Scope
- **Who**: [roles that use this SOP]
- **When**: [triggers for starting this process]
- **Prerequisites**: [what must be true before starting]

## Tools & Access Required
- [ ] [Tool 1] — [access level needed]
- [ ] [Tool 2] — [access level needed]

## Step-by-Step Procedure

### Step 1: [Action Verb] [What]
**Time**: ~X minutes
**Tool**: [if applicable]

[Clear instruction — one action per step]

> ⚠️ **Note**: [Important caveat or common mistake]

**Checkpoint**: [How to verify this step is done correctly]

### Step 2: [Action Verb] [What]
[Continue pattern...]

### Decision Point: [Question]
- **If YES** → Go to Step X
- **If NO** → Go to Step Y

## Quality Checklist
- [ ] [Check 1]
- [ ] [Check 2]
- [ ] [Check 3]

## Troubleshooting

| Problem | Likely Cause | Solution |
|---------|-------------|----------|
| [Issue 1] | [Why] | [Fix] |
| [Issue 2] | [Why] | [Fix] |

## Escalation
If something isn't covered above, contact:
- **[Role]**: [how to reach them]

## Change Log
| Date | Version | Changes | Author |
|------|---------|---------|--------|
| [Date] | 1.0 | Initial creation | [Name] |
```

## Quality Checklist

- [ ] Each step starts with an action verb
- [ ] One action per step (not compound steps)
- [ ] Decision points clearly mapped
- [ ] Checkpoints after critical steps
- [ ] Troubleshooting covers top 3-5 issues
- [ ] Time estimates included
- [ ] Tools and access listed upfront
