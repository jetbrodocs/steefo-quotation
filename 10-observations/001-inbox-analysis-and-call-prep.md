---
title: "Discovery: Steefo Quotation Tool"
status: approved
created: 2026-02-20
updated: 2026-02-21
tags: [observation, discovery, requirements]
---

# Discovery: Steefo Quotation Tool

## Source Material

| Item | Format | Details |
|---|---|---|
| WhatsApp messages from Suril Agarwal | Text (in 001-initial_notes.md) | Dated 19/02/26 |
| Technical Offer QTN-542-R2 (P460) | PDF, 42 pages | Dated 26/06/2025, 120,000 TPA mill |
| Technical Offer QTN-569 (P480) | PDF, 75 pages | Dated 05/12/2025, 160,000 TPA mill |
| Discovery call with Suril | Meeting notes (002-MOM20FEB26.md) | Dated 20/02/2026 |

---

## The Client

- **Company:** Steefo Engineering Corporation, Ahmedabad, India
- **Owner:** Suril Agarwal (surilagrawal@steefo.com)
- **Business:** Designs, manufactures, and supplies Rolling Mill & Billet Plant equipment
- **Experience:** 45+ years, projects in 20+ countries
- **Certifications:** Govt. of India Recognised Star Export House, NSIC-CRISIL Rating SE 1A

---

## Quotation Document Structure

Confirmed during the call using QTN-569 (P480, 75 pages) as reference.

### Page-by-Page Breakdown

| Pages | Section | Behavior |
|---|---|---|
| 1 | Introduction | Static body. Customizable header, footer, and introduction text. |
| 2 | Technical Parameters | 3 editable fields: mill production, basic raw material, finished products. Rest is static. |
| 3 | Basic Data & Media Requirements | Static except power requirement (editable). |
| 4 | Design Parameters & Production Table | User uploads an Excel sheet. System converts it to the quotation format. |
| 5-70 | Equipment Sections | **Item selection from catalog.** Each selected item generates ~5-6 pages. |
| 71 | Scope of Supply | Pre-filled with defaults. User can toggle S/C per line item. |
| 72-74 | Terms / Conditions / Commercial | Pre-filled with defaults. User can edit before finalizing. |
| 75 | Exclusions | Template-based suggestions with custom writing support. |

### Section Categories

**Static with editable fields (pages 1-3):** Fixed layout. A few fields change per quotation.

**Excel upload (page 4):** Steefo has production tables in Excel. The system converts these into the quotation format. Excel format is similar to the production table on page 4 of QTN-569. Awaiting sample Excel file from Steefo.

**Item catalog (pages 5-70):** The core feature. User picks equipment items from a catalog. Each selected item contributes ~5-6 pages. Items uploaded as PDF. System stitches them as-is. Each size/configuration variant is a separate catalog entry (e.g., "510mm Roughing Mill" and "550mm Roughing Mill" are two distinct items).

**Scope of Supply (page 71):** Pre-filled with default S/C assignments. User can toggle Steefo (S) vs Customer (C) per line item per project. Assignments change per project.

**Pre-filled editable (pages 72-74):** Default content loaded automatically. User modifies as needed per project.

**Exclusions (page 75):** Template-based auto-suggestions. User picks from templates or writes custom exclusions. Possible LLM-assisted writing for drafting exclusion clauses (future enhancement).

### Equipment Items Identified from PDFs

| # | Equipment Section | QTN-542 (P460) | QTN-569 (P480) | Pages (approx) |
|---|---|---|---|---|
| 1 | Heavy Duty Roughing Mill (510/550mm) | 510mm, 1 stand | 550mm, 1 stand | 4-5 |
| 2 | Continuous Intermediate Mill (410/400mm) | 410mm, 2 stands | 400mm, 2 stands | 3-4 |
| 3 | Continuous Intermediate Mill (360mm) | 4 stands | 4 stands | 3-4 |
| 4 | Continuous Intermediate Mill (320mm) | 4 stands | 4 stands | 3-4 |
| 5 | Continuous Finishing Mill (280mm) | 6 stands | 4 stands | 3-4 |
| 6 | Auxiliary Equipment | Yes | Yes | 3-4 |
| 7 | Electricals | Yes | Yes | 1-2 |
| 8 | Automatic Cooling Bed with Twin Channel & Cold Shear | Yes | Yes | 4-5 |
| 9 | Continuous Operating Dividing Shear for TMT Bars | Yes | Yes | 1 |
| 10 | Bar Finishing, Bundling & Tying Machine (Packing Bed) | Yes | Yes | 3-4 |
| 11 | TMT System | Yes | Yes | 4-5 |
| 12 | UTM Machine | Yes | Yes | 1-2 |
| 13 | Central Oil Lubrication System | No | Yes | [UNKNOWN: page count] |
| 14 | Wire Rod Block Mill | No | Yes (6 stands) | [UNKNOWN: page count] |

The system includes a **master catalog management** feature. Steefo adds, edits, and removes items as needed. The 14 items above are the starting set; exact count does not need to be fixed upfront.

---

## System Requirements

### Authentication & Roles

- Login required. Documents are confidential.
- Two roles:
  - **Super admin:** Creates and manages users. Full access.
  - **Quotation builder:** Creates and edits quotations. No user management.
- No deeper role hierarchy needed.

### Project & Version Management

- **No client/party names in the system.** Use alphanumeric codes only.
- **Project code format:** P480, P460, etc.
- **Quotation code format:** QTN569, QTN542, etc.
- **Version format:** V1, V2, V3, etc.
- Users create a quotation, edit it, and eventually **lock** it.
- Once locked, they can only create a new version (V2, V3...).
- Any version is downloadable at any time with proper file naming.

### Content & Upload

- **Equipment items:** Uploaded as PDF. System stitches them into the final document.
- **Editable sections (intro, specs, scope, terms, exclusions):** System-generated from templates and user input.
- **Production table:** Uploaded as Excel. System converts to quotation format.

### Output

- **Cover page:** Project code, quotation code, date. No client names.
- **Page numbering:** Continuous "Page X of Y" across the entire assembled document.
- **Format:** PDF download.

---

## Key Differences Between the Two Sample Offers

| Aspect | QTN-542-R2 (P460) | QTN-569 (P480) |
|---|---|---|
| Total pages | 42 | 75 |
| Mill capacity | 120,000 Tons/Year | 160,000 TPA |
| Roughing mill size | 510mm | 550mm |
| Finishing mill stands | 6 | 4 |
| Wire Rod Block Mill | Not included | Included (6 stands) |
| Central Oil Lubrication | Not a separate section | Separate section |
| High voltage | 30 KV | 33 KV |
| Low voltage | 400V | 415V |
| Production table | Not included | Included (detailed per bar size) |

---

## Resolved Questions

| # | Question | Answer |
|---|---|---|
| 1 | Complete item list? | System has master catalog management. Items added dynamically. |
| 2 | Size/config variants? | Separate catalog entries per variant. |
| 3 | Upload format? | PDF for equipment items. System-generated for editable sections. |
| 4 | Scope of Supply S/C changes? | Changes per project. Pre-filled defaults, user toggles. |
| 5 | Cover page metadata? | Project code, quotation code, date only. |
| 6 | Continuous page numbering? | Yes, Page X of Y across entire document. |
| 7 | Timeline? | No fixed deadline. Right product, right time. |
| 8 | Source files for prototyping? | Use the two existing PDFs (QTN-542 and QTN-569). |
| 9 | How exclusions work? | Template-based suggestions + custom writing. Possible LLM assist (future). |
| 10 | Excel format for production table? | Similar to page 4 of QTN-569. Sample file requested from Steefo. |

## Remaining TODOs

1. Awaiting sample Excel file from Steefo for production table format.
2. Page counts unknown for Central Oil Lubrication System and Wire Rod Block Mill items.
