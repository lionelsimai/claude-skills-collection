---
name: project-planner
description: |
  Create detailed project plans with milestones, dependencies, and resource allocation.
  TRIGGERS - Use when user wants a project plan, timeline, Gantt chart, or project management document.
---

# Project Planner

## Overview
Creates comprehensive project plans with phases, milestones, task breakdowns, dependencies, and resource allocation.

## Output Format

```markdown
# Project Plan: [Project Name]

## Project Overview
- **Objective**: [what success looks like]
- **Duration**: [total timeline]
- **Team**: [who's involved]
- **Budget**: [if applicable]

## Milestones
| Milestone | Target Date | Criteria |
|-----------|------------|----------|
| [M1] | [date] | [what must be true] |

## Phase Breakdown

### Phase 1: [Name] — [Duration]
| Task | Owner | Duration | Dependencies | Status |
|------|-------|----------|-------------|--------|
| [Task] | [who] | [days] | [blockers] | ⬜ |

### Phase 2: [Name] — [Duration]
[Same structure]

## Risk Register
| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| [risk] | High/Med/Low | High/Med/Low | [plan] |

## Communication Plan
- **Standups**: [frequency]
- **Status updates**: [frequency and format]
- **Stakeholder reviews**: [schedule]
```

## Quality Checklist
- [ ] Milestones are specific and measurable
- [ ] Every task has an owner and timeline
- [ ] Dependencies mapped
- [ ] Risks identified with mitigation plans
- [ ] Communication cadence defined
