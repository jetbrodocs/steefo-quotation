---
title: "Gap Analysis: Current vs Proposed Quotation Process"
status: approved
created: 2026-02-21
updated: 2026-02-21
tags: [analysis, gap-analysis, requirements]
---

# Gap Analysis: Current vs Proposed Quotation Process

## Summary

Steefo's current quotation process is manual, file-scattered, and error-prone. The proposed system addresses every identified pain point. This analysis maps each gap between as-is and to-be, identifies the core functional requirements, and ranks them by priority.

## Source Documents

- `10-observations/001-inbox-analysis-and-call-prep.md` (approved)
- `20-process-maps/001-quotation-creation-current.md` (approved)
- `20-process-maps/002-quotation-creation-proposed.md` (approved)

---

## Findings

### Process Gaps

| # | Gap | Current State | Required State | Impact |
|---|---|---|---|---|
| 1 | No centralized catalog | Equipment page sets spread across individual machines. 2-3 staff may have different file versions. | Single catalog in the system. Super admin manages items. All builders see the same content. | Risk of sending outdated specs. Duplication of effort. |
| 2 | Manual document assembly | Staff copies pages from multiple Word/PDF files into one document. | System stitches selected item PDFs automatically. | Hours of manual work per quotation. Copy-paste errors. |
| 3 | Manual page numbering | Staff updates "Page X of Y" headers/footers by hand after every change. | System generates continuous page numbering automatically. | Numbering errors in sent quotations. Rework after every edit. |
| 4 | No version control | Versions tracked by file naming (QTN-542-R2). Previous versions may be overwritten. | System-managed versions. Lock to freeze. Create new version from locked. All versions downloadable. | Risk of losing previous versions. No audit trail. |
| 5 | No multi-session support | Quotation must be assembled in one effort or staff manually saves partial work. | Draft state. Builder saves progress. Returns across sessions. | Quotations build up over days/weeks. Partial work may be lost. |
| 6 | No collaboration | One person works on files on their machine. | Multiple builders access the same system from any device. | Bottleneck if one person is unavailable. |
| 7 | Scope of Supply is manual | Staff builds the S/C responsibility table from scratch or copies from a previous quotation. | Pre-filled defaults. Builder toggles S/C per line item. Table auto-populates based on selected items. | Slow. Easy to miss items or assign wrong responsibility. |
| 8 | Production table is manual | Staff calculates in Excel, then manually formats into the document. | Upload Excel. System converts to quotation format. | Formatting inconsistency. Manual rework. |
| 9 | No quotation state tracking | No formal tracking of which quotations are in progress, completed, or sent. | Three states: draft, locked, sent. | No visibility into quotation pipeline. |
| 10 | Exclusions written from scratch | Staff types exclusion clauses manually each time. | Template-based suggestions. Pick from templates or write custom. | Repeated effort. Inconsistent language across quotations. |

### Content Architecture Analysis

The quotation document has five distinct content types. Each requires different handling:

| Content Type | Pages | Data Source | Edit Model | PDF Generation |
|---|---|---|---|---|
| Static with editable fields | 1-3 | System template + user input | Form fields | System-generated |
| Excel upload | 4 | User-uploaded Excel | Upload + preview | System-converted |
| Catalog items (PDF stitch) | 5-70 | Pre-uploaded PDFs in catalog | Select/deselect | Concatenate as-is |
| Pre-filled editable | 71-74 | Default templates + user edits | Rich text editing | System-generated |
| Selectable list | 75 | Template suggestions + custom | Pick + write | System-generated |

**Key insight:** The system is not a single-mode tool. It combines a form builder (pages 1-3), a file converter (page 4), a PDF stitcher (pages 5-70), a rich text editor (pages 71-74), and a template picker (page 75). Each mode has different UI and backend requirements.

### Scope of Supply Table Analysis

The Scope of Supply table (page 71) is structurally coupled to item selection. When items are selected on pages 5-70, corresponding rows should appear in the scope table. Each row has multiple responsibility columns (Basic Data, Basic Design, Detailed Design, Supply, Supervision of Erection, Erection & Comm., Supervision of Comm.) that can be toggled between S and C.

From the two sample PDFs:
- QTN-542 has ~60 line items across 12 equipment categories in its scope table (pages 37-39).
- QTN-569 likely has more due to additional equipment (75 pages total).

**Key insight:** Each catalog item needs associated scope-of-supply rows with default S/C values. When a builder selects an item, its scope rows auto-populate in the table. The builder then toggles individual cells.

### Quotation Lifecycle Analysis

Based on the call and process mapping:

```
                    ┌─────────────────────────┐
                    │                         │
   Create ──→ Draft ──→ Locked ──→ Sent       │
                ↑         │                   │
                │         └── Create New ─────┘
                │              Version (V2 draft)
                │
                └── (save, return, edit across sessions)
```

States:
- **Draft:** Editable. Builder works on it across multiple sessions. Can preview PDF at any time.
- **Locked:** Read-only. PDF finalized. Builder can download. Can create a new version (copies all data into a new draft).
- **Sent:** Marker indicating the quotation was delivered to the customer. Still downloadable.

### User Role Analysis

| Role | Create Users | Manage Catalog | Create Quotations | Edit Quotations | Lock/Send | Download |
|---|---|---|---|---|---|---|
| Super admin | Yes | Yes | Yes | Yes | Yes | Yes |
| Quotation builder | No | No | Yes | Yes (own drafts) | Yes | Yes |

**Key insight:** Super admin is not a separate person. It is Suril or a trusted staff member who also builds quotations. The role adds catalog and user management on top of builder capabilities.

---

## Functional Requirements

Derived from the gaps and analysis above. Ranked by priority.

### Must Have (MVP)

| # | Requirement | Derived From |
|---|---|---|
| F1 | User login with username/password | Gap 6, call requirement |
| F2 | Two roles: super admin and quotation builder | Call requirement |
| F3 | Equipment item catalog: add, edit, deactivate items (PDF upload) | Gap 1 |
| F4 | Create new quotation with project code, QTN code, date | Process map 002 step 2 |
| F5 | Edit front pages: form fields for introduction, technical params, basic data | Content type: static with editable fields |
| F6 | Upload production table Excel, convert to quotation format | Content type: Excel upload |
| F7 | Select equipment items from catalog (checkboxes) | Content type: catalog items |
| F8 | Scope of Supply table: auto-populate from selected items, toggle S/C per cell | Scope analysis |
| F9 | Edit terms/conditions pages from pre-filled defaults | Content type: pre-filled editable |
| F10 | Exclusions: template-based suggestions + custom text | Content type: selectable list |
| F11 | Save draft, return across sessions | Gap 5 |
| F12 | Preview exact PDF render in browser | Process map 002, resolved Q2 |
| F13 | Lock version (read-only) | Gap 4 |
| F14 | Download PDF with continuous page numbering and proper file naming | Gap 3, resolved Q6 |
| F15 | Create new version from locked version | Gap 4, Exception B |
| F16 | Mark quotation as sent | Gap 9, call requirement |

### Should Have (Post-MVP)

| # | Requirement | Derived From |
|---|---|---|
| F17 | Quotation list/dashboard with status filters (draft, locked, sent) | Gap 9 |
| F18 | Catalog item versioning (track which PDF version was used in which quotation) | Gap 1, future-proofing |
| F19 | Version diff/changelog between quotation versions | Resolved Q3: nice to have |
| F20 | LLM-assisted exclusion clause writing | Call: Suril suggested AI for easy writing |

### Won't Have (Out of Scope)

| # | Item | Reason |
|---|---|---|
| X1 | Email sending from system | Resolved Q1: download only |
| X2 | Client/party name storage | Call: alphanumeric codes only, no client names |
| X3 | Commercial/pricing module | Technical offer only, no pricing discussed |
| X4 | Multi-language support | Not discussed, all offers in English |

---

## Non-Functional Requirements

| # | Requirement | Notes |
|---|---|---|
| NF1 | Simple UI. Big buttons, minimal text input. | Users are basic computer users. |
| NF2 | Web-based. Accessible from any device with a browser. | 2-3 users across machines. Login requirement. |
| NF3 | PDF output must match Steefo's existing offer format. | Continuous page numbering, letterhead consistency. |
| NF4 | Handle documents up to 200 pages. | Suril mentioned 100-200 page offers. |
| NF5 | Support PDF item uploads up to ~10 pages each. | Typical item is 5-6 pages. |
| NF6 | Confidential. Login required. No public access. | Call requirement. |

---

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| PDF generation quality: page numbering overlay on stitched PDFs may not align with Steefo's header format | Medium | High | Prototype PDF generation early. Test with actual Steefo PDFs. |
| Excel-to-table conversion: unknown Excel format may be complex | Low | Medium | Format is similar to page 4 of QTN-569. Awaiting sample file. Design converter after receiving it. |
| Scope of Supply table complexity: 60+ rows, 7 togglable columns per row | Medium | Medium | Build as an editable grid. Pre-populate from catalog item metadata. |
| User adoption: basic computer users may struggle with web app | Low | High | Keep UI dead simple. Test with Steefo staff before launch. |

---

## Resolved Questions

| # | Question | Answer |
|---|---|---|
| 1 | Letterhead on system-generated pages? | Replicate Steefo's letterhead design in system templates. Full control. Item content PDFs are stitched as-is with page number overlay on top. |
| 2 | Scope of Supply table: per-item rows or master template? | Each catalog item defines its own scope of supply rows. When a builder selects an item, its scope rows auto-populate in the table. The super admin sets default S/C values per row when uploading the item. |
