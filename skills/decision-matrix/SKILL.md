---
name: decision-matrix
description: |
  Create weighted decision matrices for complex choices with scoring and recommendations.
  TRIGGERS - Use when user needs to compare options, make a decision, or evaluate alternatives.
---

# Decision Matrix

## Overview
Creates structured decision matrices that objectively compare options using weighted criteria.

## Workflow

### Step 1: Define the Decision
1. **What are you deciding?**
2. **Options**: What are the 2-5 options?
3. **Criteria**: What matters most? (cost, speed, quality, risk, etc.)
4. **Stakeholders**: Who cares about this decision?

### Step 2: Weight the Criteria

| Criteria | Weight (1-10) | Why |
|----------|--------------|-----|
| [Criteria 1] | [weight] | [reasoning] |
| [Criteria 2] | [weight] | [reasoning] |

### Step 3: Score Each Option

| Criteria (Weight) | Option A | Option B | Option C |
|-------------------|----------|----------|----------|
| [C1] (×8) | [score/10] = [weighted] | [score] = [weighted] | [score] = [weighted] |
| [C2] (×6) | [score/10] = [weighted] | [score] = [weighted] | [score] = [weighted] |
| **TOTAL** | **[sum]** | **[sum]** | **[sum]** |

### Step 4: Recommendation

```markdown
## Recommendation: [Winner]

**Score**: [X] out of [max possible]

**Why this wins**: [2-3 sentences]

**Key tradeoffs**: [what you give up]

**Risk factors**: [what could go wrong]

**Dissenting view**: [argument for the runner-up]
```

## Quality Checklist
- [ ] Criteria weighted before scoring
- [ ] Scores justified (not arbitrary)
- [ ] Winner explained with reasoning
- [ ] Tradeoffs acknowledged
- [ ] Dissenting view presented
