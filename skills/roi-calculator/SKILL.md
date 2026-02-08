---
name: roi-calculator
description: |
  Calculate and present ROI for AI projects, services, or business investments.
  
  TRIGGERS - Use this skill when:
  - User wants to calculate ROI for a project or service
  - User needs to justify an investment or expense
  - User wants to present cost-benefit analysis to stakeholders
  - User mentions ROI, cost savings, payback period, or business case
---

# ROI Calculator

## Overview

Calculates and presents clear ROI analysis for projects, services, or investments. Creates stakeholder-ready reports with hard numbers.

## Workflow

### Step 1: Gather the Numbers

Ask the user:
1. **What's the investment?** (service, tool, project, hire)
2. **Total cost**: One-time + ongoing monthly/annual costs
3. **Current state**: Time spent, cost of current process, error rate
4. **Expected improvement**: Time saved, revenue gained, errors reduced
5. **Timeline**: When do benefits start? Over what period?

### Step 2: Calculate Core Metrics

**ROI Formula:**
```
ROI = ((Total Benefits - Total Costs) / Total Costs) × 100
```

**Key Metrics to Calculate:**
- **Net benefit** = Total benefits - Total costs
- **ROI %** = Net benefit / Total costs × 100
- **Payback period** = Total costs / Monthly benefit
- **Monthly recurring savings**
- **Annual impact**
- **Break-even point**

**For Time Savings:**
```
Hours saved per month × Hourly rate = Monthly savings
Monthly savings × 12 = Annual savings
```

**For Revenue Impact:**
```
New revenue enabled + Revenue from freed-up time = Total revenue impact
```

### Step 3: Build the Analysis

## Output Format

```markdown
# ROI Analysis: [Investment Name]

## Executive Summary
**Bottom line**: For every $1 invested, you get $[X] back.
- **Total investment**: $[X]
- **Annual return**: $[X]
- **ROI**: [X]%
- **Payback period**: [X] months

## Cost Breakdown

| Cost Item | One-Time | Monthly | Annual |
|-----------|----------|---------|--------|
| [Item 1] | $X | $X | $X |
| [Item 2] | $X | $X | $X |
| **Total** | **$X** | **$X** | **$X** |

## Benefits Breakdown

| Benefit | Monthly Value | Annual Value | How Calculated |
|---------|-------------|-------------|----------------|
| Time savings | $X | $X | [X hrs × $X/hr] |
| Error reduction | $X | $X | [X errors × $X cost] |
| Revenue increase | $X | $X | [explanation] |
| **Total** | **$X** | **$X** | |

## 12-Month Projection

| Month | Cumulative Cost | Cumulative Benefit | Net Position |
|-------|----------------|-------------------|-------------|
| 1 | $X | $X | -$X |
| 3 | $X | $X | -$X |
| 6 | $X | $X | +$X |
| 12 | $X | $X | +$X |

## Break-Even Point
**Month [X]** — After this point, every month generates $[X] in net value.

## Conservative vs Optimistic Scenarios

| Scenario | ROI | Payback | Annual Return |
|----------|-----|---------|--------------|
| Conservative (50% of projected) | X% | X months | $X |
| **Expected** | **X%** | **X months** | **$X** |
| Optimistic (150% of projected) | X% | X months | $X |

## Recommendation
[Clear recommendation with confidence level]
```

## Quality Checklist

- [ ] All assumptions stated explicitly
- [ ] Conservative estimate included
- [ ] Payback period calculated
- [ ] Monthly projection shows break-even
- [ ] Benefits are quantified (not just "saves time")
- [ ] Stakeholder-ready formatting
