---
title: "Quotation Creation Process (Proposed / To-Be)"
status: approved
created: 2026-02-21
updated: 2026-02-21
tags: [process, quotation, to-be]
---

# Quotation Creation Process (Proposed / To-Be)

## Process Overview

- **Purpose:** Assemble a technical offer document using the quotation preparation tool.
- **Trigger:** A customer enquiry arrives for Rolling Mill or Billet Plant equipment.
- **End condition:** A versioned PDF technical offer is generated, marked as sent, and available for download.
- **Frequency:** Same as current. [UNKNOWN: quotations per month]
- **Typical duration:** Significantly reduced. Front pages and item selection take minutes instead of hours. PDF assembly is automatic.

## Roles Involved

| Role | Responsibility in This Process |
|---|---|
| Super admin | Manages users. Manages the equipment item catalog (add, edit, remove items). Manages default templates for scope, terms, exclusions. |
| Quotation builder | Creates quotations. Selects items. Edits project-specific fields. Locks versions. Downloads PDFs. |

## Inputs

| Input | Source | Notes |
|---|---|---|
| Customer enquiry | Email, phone, or in-person | Same as current process |
| Equipment item PDFs | Uploaded to system catalog by super admin | Pre-made PDF page sets, ~5-6 pages each |
| Production table Excel | Uploaded per quotation by builder | System converts to quotation format |
| Default templates | Pre-loaded in system | Introduction, scope of supply, terms, exclusions |

## Outputs

| Output | Destination | Notes |
|---|---|---|
| Versioned PDF technical offer | Downloaded from system | Continuous page numbering (Page X of Y), proper file naming |
| Quotation record | Stored in system | Project code, QTN code, version, item selections, all edits preserved |

## Process Steps

### Main Flow

1. Quotation builder logs into the system.
2. Builder creates a new quotation. Enters project code (e.g., P480), quotation code (e.g., QTN569). System assigns version V1 automatically.
3. Builder edits the introduction page. Header, footer, and introduction text fields are pre-filled with defaults. Builder modifies as needed.
4. Builder edits the technical parameters page. Updates 3 fields: mill production, basic raw material, finished products.
5. Builder edits the basic data page. Updates the power requirement field.
6. Builder uploads the production table Excel file. System converts it into the quotation page format.
   - **If Excel format is valid:** System renders the production table. Continue to step 7.
   - **If Excel format is invalid:** System shows an error. Go to Exception A.
7. Builder selects equipment items from the catalog. System displays all available items with names. Builder checks the ones to include. Each selected item adds its PDF pages to the document.
8. Builder reviews the Scope of Supply table. System pre-fills with default S/C assignments for the selected items. Builder toggles S or C per line item as needed.
9. Builder edits the terms and conditions pages. System pre-fills with default content. Builder modifies as needed.
10. Builder selects exclusion clauses. System offers template-based suggestions. Builder picks from templates or writes custom clauses.
11. Builder saves progress at any point. Quotation stays in **draft** state. Builder can return across multiple sessions to continue editing.
12. When ready, builder previews the assembled quotation. System renders the exact final PDF with continuous page numbering.
13. Builder checks the document.
    - **If satisfied:** Builder locks the version. Go to step 14.
    - **If changes needed:** Builder goes back to the relevant step and edits. System preserves all changes.
14. Builder locks version V1. The quotation becomes read-only.
15. Builder downloads the PDF. File name follows the convention: project code + QTN code + version (e.g., P480-QTN569-V1.pdf).
16. Builder marks the quotation as **sent** after delivering it to the customer.

### Exception A: Invalid Excel Upload

A1. System displays a validation error describing the problem (missing columns, wrong format, etc.).
A2. Builder corrects the Excel file locally.
A3. Builder re-uploads. Return to main flow at step 6.

### Exception B: New Version of Existing Quotation

B1. Builder opens the locked quotation (e.g., P480-QTN569-V1).
B2. Builder clicks "Create New Version." System copies all data from V1 into a new editable V2.
B3. Builder makes changes: swap items, update fields, adjust scope.
B4. Return to main flow at step 12 (preview and lock).

### Exception C: Catalog Item Missing

C1. Builder needs an equipment item that is not in the catalog.
C2. Builder contacts the super admin.
C3. Super admin uploads the new item PDF to the catalog with a name and description.
C4. Builder refreshes the item list. New item is now available. Return to main flow at step 7.

## Flow Diagram

```
Login → New Quotation (codes) → Edit Front Pages (1-3) → Upload Excel (4)
                                                              ↓
                                    Select Items from Catalog (5-70) → Scope of Supply (71)
                                                              ↓
                                    Terms (72-74) → Exclusions (75) → Save Draft
                                                              ↓
                                    (return across sessions) → Preview PDF → Lock Version → Download
                                                                                              ↓
                                                                                          Mark Sent
```

```
Quotation states:

  Draft ──→ Locked ──→ Sent
    ↑          ↓
    └── (edit) "Create New Version" → New Draft (V2)
```

## Connected Processes

- **Upstream:** Sales/enquiry process (unchanged).
- **Downstream:** Commercial negotiation (unchanged).
- **Related:** Catalog management process (new). Super admin maintains the equipment item catalog.

## Sub-Process: Catalog Management

1. Super admin logs into the system.
2. Admin navigates to the item catalog.
3. Admin adds a new item: uploads a PDF file, enters a name and description.
4. Item becomes available to all quotation builders immediately.
5. To update an item: admin uploads a new PDF. Previous quotations retain the old version (they are already locked).
6. To remove an item: admin deactivates it. It no longer appears in new quotations. Existing quotations are unaffected.

## Systems and Tools

| Step | System/Tool | How It's Used |
|---|---|---|
| 1-14 | Quotation preparation tool (web app) | All quotation assembly, editing, versioning, PDF generation |
| 6 | Microsoft Excel (user side) | Builder prepares production table locally, uploads to system |
| 14 | PDF viewer | Builder reviews downloaded PDF |
| Email | Email client | Builder sends PDF to customer (outside the system) |

## What Changes vs Current Process

| Aspect | Current (As-Is) | Proposed (To-Be) |
|---|---|---|
| Document assembly | Manual copy-paste from multiple files | System assembles from catalog selections |
| Page numbering | Manual update after every change | Automatic, continuous Page X of Y |
| Version control | File naming conventions (error-prone) | System-managed versions with locking |
| Equipment catalog | Files on local machines | Centralized catalog in the system |
| Scope of Supply | Manual editing from scratch or copy | Pre-filled defaults, toggle S/C per item |
| Production table | Excel → manual formatting into Word | Excel upload → automatic conversion |
| Exclusions | Written from scratch | Template suggestions + custom writing |
| Collaboration | One person works on one machine | Multiple users, same system, any device |

## Resolved Questions

| # | Question | Answer |
|---|---|---|
| 1 | Send PDF via email from system? | No. Download only. User sends via their own email. |
| 2 | Preview type before locking? | Exact PDF preview. Full rendered document in browser. |
| 3 | Track changes between versions? | Nice to have, not priority. Not in initial release. |

## Design Notes

- Quotations need **three states**: draft, locked, sent.
- Draft state supports multi-session editing. Builders save progress and return later.
- Locked state is read-only. Only action: create new version or mark as sent.
- Sent is a final status marker for tracking purposes.
