---
name: excel-model-builder
description: |
  Build financial models, trackers, and spreadsheets with formulas and formatting.
  
  TRIGGERS - Use this skill when:
  - User wants to create a spreadsheet, financial model, or Excel file
  - User mentions Excel, Google Sheets, financial projections, or budgets
  - User needs a tracker, calculator, or data template
---

# Excel Model Builder

## Overview

Creates structured spreadsheets and financial models with formulas, formatting, and clear documentation. Outputs ready-to-use Excel files or Google Sheets templates.

## Workflow

### Step 1: Define the Model

Ask the user:
1. **Purpose**: What decisions will this model inform?
2. **Type**: Financial projection, budget, tracker, calculator, or dashboard?
3. **Inputs**: What data will be entered?
4. **Outputs**: What numbers/insights do you need?
5. **Time horizon**: Monthly, quarterly, annual?
6. **Format**: Excel (.xlsx) or Google Sheets formula format?

### Step 2: Design the Structure

**Standard model layout:**

| Tab | Purpose |
|-----|---------|
| **Dashboard** | Summary view with key metrics |
| **Assumptions** | All inputs in one place (change here, model updates) |
| **Revenue** | Revenue projections and breakdowns |
| **Costs** | Cost structure and projections |
| **P&L** | Profit & Loss statement |
| **Cash Flow** | Cash flow projections (if needed) |

### Step 3: Build with Formulas

**Rules for good models:**
1. **Inputs highlighted** (yellow cells = editable)
2. **No hardcoded numbers** in formulas — reference the Assumptions tab
3. **Clear labels** for every row and column
4. **Consistent formatting** (currency, percentages, dates)
5. **Error handling** with IFERROR()
6. **Named ranges** for key assumptions

### Step 4: Create the Spreadsheet

Use openpyxl (Python) to generate .xlsx files with:
- Multiple tabs
- Formulas (not just values)
- Conditional formatting
- Number formatting
- Headers and borders
- Print-ready layout

## Output

Generate actual .xlsx file with:
- All formulas intact
- Formatting applied
- Sample data that can be replaced
- Instructions tab explaining how to use it

## Quality Checklist

- [ ] All inputs on one tab (Assumptions)
- [ ] No hardcoded numbers in formulas
- [ ] Yellow highlighting on editable cells
- [ ] Dashboard shows key metrics at a glance
- [ ] Formulas use cell references (not typed values)
- [ ] Error handling on division formulas
- [ ] Instructions included
