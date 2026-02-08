---
name: churn-analyzer
description: |
  Analyze customer churn patterns and create retention strategies.
  TRIGGERS - Use when user wants to reduce churn, improve retention, or understand why customers leave.
---

# Churn Analyzer

## Overview
Analyzes churn patterns, identifies root causes, and creates actionable retention strategies.

## Workflow

### Step 1: Gather Context
1. **Business model**: SaaS, service, product?
2. **Current churn rate**: Monthly/annual?
3. **Customer segments**: Different tiers or types?
4. **Known reasons**: Why do customers say they leave?
5. **Available data**: What customer data do you have?

### Step 2: Analyze Churn

**Churn calculation:**
```
Monthly churn = Customers lost / Starting customers × 100
Annual churn = 1 - (1 - monthly churn)^12
Revenue churn = MRR lost / Starting MRR × 100
```

**Analysis dimensions:**
- By segment (plan tier, industry, size)
- By tenure (when do they leave?)
- By engagement (usage before churn)
- By acquisition source (where they came from)
- By season (time patterns)

## Output Format

```markdown
# Churn Analysis: [Company]

## Current State
- **Monthly churn**: [X%]
- **Annual churn**: [X%]
- **Revenue impact**: $[X] lost/month
- **Industry benchmark**: [X%]

## Churn Patterns

### By Tenure
| Period | Churn Rate | Insight |
|--------|-----------|---------|
| Month 1 | X% | [early churn = onboarding problem] |
| Month 2-3 | X% | [value realization gap] |
| Month 6+ | X% | [engagement decay] |

### By Segment
[Breakdown by customer type]

## Root Cause Analysis
1. **[Cause 1]** — [% of churn] — [evidence]
2. **[Cause 2]** — [% of churn] — [evidence]
3. **[Cause 3]** — [% of churn] — [evidence]

## Retention Strategy

### Quick Wins (This Month)
1. [Action]: Expected impact [X% reduction]
2. [Action]: Expected impact [X% reduction]

### Medium-Term (This Quarter)
1. [Action]: Expected impact [X% reduction]

### Long-Term (This Year)
1. [Action]: Expected impact [X% reduction]

## Financial Impact
If churn reduces from [X%] to [Y%]:
- Monthly revenue saved: $[X]
- Annual impact: $[X]
- LTV improvement: [X%]
```

## Quality Checklist
- [ ] Churn calculated correctly (logo + revenue)
- [ ] Patterns identified by multiple dimensions
- [ ] Root causes ranked by impact
- [ ] Retention strategies are specific and actionable
- [ ] Financial impact quantified
