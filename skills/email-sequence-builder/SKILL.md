---
name: email-sequence-builder
description: |
  Build automated email nurture sequences for sales, onboarding, or engagement.
  
  TRIGGERS - Use this skill when:
  - User wants to create email sequences or drip campaigns
  - User mentions email automation, nurture sequences, or email funnels
  - User wants welcome sequences, onboarding emails, or sales follow-ups
---

# Email Sequence Builder

## Overview

Creates complete email sequences for any purpose — welcome series, sales nurturing, onboarding, re-engagement, or launch sequences. Each email is strategically timed and builds on the previous one.

## Workflow

### Step 1: Define the Sequence

Ask the user:
1. **Purpose**: Welcome, nurture, sell, onboard, or re-engage?
2. **Audience**: Who receives this? Where are they in the journey?
3. **Goal**: What action should they take by the end?
4. **Emails**: How many? (default: 5-7)
5. **Frequency**: Daily, every 2 days, weekly?
6. **Offer/Product**: What are you ultimately selling or promoting?

### Step 2: Choose the Sequence Type

| Type | Emails | Timing | Goal |
|------|--------|--------|------|
| **Welcome** | 5-7 | Daily for 7 days | Build trust, set expectations |
| **Nurture** | 7-10 | Every 2-3 days | Educate, build desire |
| **Sales** | 5-7 | Daily during launch | Convert to purchase |
| **Onboarding** | 5-7 | Triggered by actions | Activate new users |
| **Re-engagement** | 3-5 | Every 3-5 days | Win back inactive users |
| **Cart Abandonment** | 3 | 1hr, 24hr, 72hr | Recover lost sales |

### Step 3: Map the Emotional Journey

Each email should move them one step closer to the goal:

```
Email 1: WELCOME — "You're in the right place"
Email 2: VALUE — "Here's something useful right now"
Email 3: STORY — "Here's why I do this" (build connection)
Email 4: PROOF — "Here's what's possible" (case study/results)
Email 5: TEACH — "Here's how to get started"
Email 6: OFFER — "Here's how I can help you go further"
Email 7: URGENCY — "Last chance / final reminder"
```

### Step 4: Write Each Email

**For each email, include:**

- **Subject line** (+ 1 A/B variation)
- **Preview text** (the snippet shown in inbox)
- **Body** (under 300 words)
- **CTA** (one clear action)
- **Send timing** (when relative to signup/trigger)
- **Goal** (what this email specifically achieves)

**Email writing rules:**
- Write like a human, not a brand
- One idea per email
- One CTA per email
- Short paragraphs (1-3 sentences)
- Use the reader's first name {{first_name}}
- Subject lines under 50 characters

## Output Format

```markdown
# Email Sequence: [Name]

## Sequence Overview
- **Type**: [welcome/nurture/sales/etc.]
- **Emails**: [count]
- **Duration**: [total days]
- **Goal**: [end action]
- **Trigger**: [what starts the sequence]

---

## Email 1 of [X]
**Send**: [timing — e.g., Immediately / Day 0]
**Goal**: [what this email achieves]

**Subject A**: [primary subject line]
**Subject B**: [A/B variation]
**Preview**: [preview text]

---

[Email body with {{first_name}} personalization]

[CTA button text or link text]

---

## Email 2 of [X]
[Continue same format...]

---

## Sequence Logic
- If opened Email 3 but didn't click → [action]
- If clicked CTA in Email 5 → [action]
- If no opens after Email 4 → [action]

## Tech Setup Notes
- Platform recommendations: [ConvertKit, Mailchimp, ActiveCampaign, etc.]
- Tags/segments to create
- Automation triggers to set up
```

## Quality Checklist

- [ ] Each email has a single, clear purpose
- [ ] Subject lines are under 50 characters
- [ ] Preview text complements (not repeats) subject
- [ ] Emotional journey builds logically
- [ ] One CTA per email
- [ ] Personalization variables included
- [ ] A/B subject line variations provided
- [ ] Sequence logic handles engagement branches
