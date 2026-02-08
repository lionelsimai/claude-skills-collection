---
name: chatbot-builder
description: |
  Design conversational chatbot flows with intents, responses, and escalation logic.
  TRIGGERS - Use when user wants to build a chatbot, design conversation flows, or create automated chat responses.
---

# Chatbot Builder

## Overview
Designs complete chatbot architectures with conversation flows, intent mapping, response templates, and escalation rules.

## Workflow

### Step 1: Define the Bot
1. **Purpose**: Customer support, lead qualification, FAQ, onboarding, or sales?
2. **Platform**: Website widget, WhatsApp, Messenger, Slack, or custom?
3. **Persona**: What's the bot's personality?
4. **Scope**: What topics should it handle? What should it NOT handle?
5. **Escalation**: When should it hand off to a human?

### Step 2: Map Intents

| Intent | Example Phrases | Priority |
|--------|----------------|----------|
| Greeting | "hi", "hello", "hey there" | High |
| Pricing | "how much", "pricing", "cost" | High |
| Support | "help", "problem", "not working" | High |
| [Custom] | [phrases] | [priority] |

### Step 3: Design Conversation Flows

```
USER: [trigger phrase]
  ↓
BOT: [response + follow-up question]
  ↓
USER: [option A] → BOT: [response A] → [next step]
USER: [option B] → BOT: [response B] → [next step]
USER: [unclear] → BOT: [clarification] → [retry]
  ↓
[3 unclear attempts] → ESCALATE TO HUMAN
```

### Step 4: Write Response Templates

For each intent:
- **Initial response**: First message
- **Follow-up questions**: Gather needed info
- **Resolution**: Answer or action
- **Fallback**: When bot can't help
- **Handoff message**: Transition to human

## Output Format

```markdown
# Chatbot Design: [Bot Name]

## Bot Profile
- **Name**: [bot name]
- **Personality**: [description]
- **Platform**: [where it lives]
- **Supported languages**: [languages]

## Intent Map
[Table of all intents with examples and responses]

## Conversation Flows

### Flow 1: [Name]
[Visual flow with decision trees]

### Flow 2: [Name]
[Visual flow]

## Response Templates
[All response messages organized by intent]

## Escalation Rules
- After [X] failed attempts → human
- Keywords [list] → immediate human
- Sentiment negative → human
- Off-hours → ticket + follow-up

## Knowledge Base
[FAQ answers the bot should know]

## Implementation Notes
- Platform: [recommended tool]
- AI model: [if using LLM]
- Integration: [APIs needed]
```

## Quality Checklist
- [ ] All common intents mapped
- [ ] Fallback responses for unrecognized input
- [ ] Escalation rules clear
- [ ] Persona consistent across responses
- [ ] Tested with 10+ conversation paths
