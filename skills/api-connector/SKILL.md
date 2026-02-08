---
name: api-connector
description: |
  Connect to external APIs, process responses, and build integrations.
  TRIGGERS - Use when user wants to connect APIs, build integrations, or process API data.
---

# API Connector

## Overview
Designs and implements API integrations including authentication, request formatting, response parsing, and error handling.

## Workflow

### Step 1: Define the Integration
1. **API**: Which service are you connecting to?
2. **Purpose**: What data do you need or what action to trigger?
3. **Direction**: Read data, write data, or both?
4. **Platform**: Where is this running? (n8n, Make, Zapier, custom code)
5. **Frequency**: One-time, on-demand, or scheduled?

### Step 2: Map the Integration

```markdown
[SOURCE] → [API Call] → [PROCESS] → [DESTINATION]
```

### Step 3: Build the Connection

For each API call, document:

```markdown
## API Call: [Name]

### Endpoint
`[METHOD] [URL]`

### Authentication
- **Type**: [API key, OAuth2, Bearer token]
- **Setup**: [How to get credentials]

### Request
**Headers:**
```json
{
  "Authorization": "Bearer {{API_KEY}}",
  "Content-Type": "application/json"
}
```

**Body (if POST/PUT):**
```json
{
  "field": "{{value}}"
}
```

### Response
**Success (200):**
```json
{
  "data": { ... }
}
```

**Fields to extract:**
| Field | Path | Use |
|-------|------|-----|
| [name] | response.data.name | [purpose] |

### Error Handling
| Status | Meaning | Action |
|--------|---------|--------|
| 400 | Bad request | Check input format |
| 401 | Unauthorized | Refresh token |
| 429 | Rate limited | Wait and retry |
| 500 | Server error | Retry with backoff |
```

## Output Format
Complete integration documentation with code samples for the user's platform.

## Quality Checklist
- [ ] Authentication method documented
- [ ] Request format with examples
- [ ] Response parsing specified
- [ ] Error handling for common status codes
- [ ] Rate limiting considered
- [ ] Test endpoint provided
