---
name: ab-test-designer
description: |
  Design A/B tests with hypotheses, variants, sample sizes, and analysis plans.
  TRIGGERS - Use when user wants to run A/B tests, split tests, or experiment with variations.
---

# A/B Test Designer

## Overview
Designs rigorous A/B tests with clear hypotheses, variant specifications, sample size calculations, and analysis plans.

## Workflow

### Step 1: Define the Test
1. **What are you testing?** (page, email, ad, feature)
2. **Current metric**: What's the baseline performance?
3. **Goal**: What improvement are you hoping for?
4. **Traffic/volume**: How many users/emails/impressions per day?

### Step 2: Structure the Test

## Output Format

```markdown
# A/B Test: [Test Name]

## Hypothesis
If we [change X], then [metric Y] will [increase/decrease] by [Z%] because [reasoning].

## Test Details
- **Type**: A/B / A/B/C / Multivariate
- **Primary metric**: [what you're measuring]
- **Secondary metrics**: [supporting metrics]
- **Guardrail metrics**: [what shouldn't get worse]

## Variants

### Control (A)
[Description of current experience]

### Variant (B)
[Description of the change]
[Mockup/wireframe description if applicable]

## Sample Size & Duration
- **Baseline conversion**: [X%]
- **Minimum detectable effect**: [X%]
- **Statistical significance**: 95%
- **Required sample size**: [N per variant]
- **Estimated duration**: [X days]

## Analysis Plan
1. Wait for minimum sample size before checking
2. Check primary metric first
3. Segment analysis: [segments to check]
4. If significant: [implementation plan]
5. If not significant: [next steps]

## Risks & Considerations
- [Risk 1]: [mitigation]
- [Risk 2]: [mitigation]
```

## Quality Checklist
- [ ] Hypothesis is specific and falsifiable
- [ ] One primary metric defined
- [ ] Sample size calculated
- [ ] Duration estimated
- [ ] Analysis plan prevents peeking bias
- [ ] Guardrail metrics identified
