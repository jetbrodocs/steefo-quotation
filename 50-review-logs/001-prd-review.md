---
title: "Review Log — PRD and User Journeys"
status: approved
created: 2026-02-22
updated: 2026-02-25
reviewer: Claude
tags: [review]
---

# Review Log — PRD and User Journeys

## Scope

Reviewed `40-solution-design/001-quotation-tool-prd.md` and `40-solution-design/002-user-journeys.md` against:
- `10-observations/001-inbox-analysis-and-call-prep.md`
- `20-process-maps/002-quotation-creation-proposed.md`
- `30-analysis/001-gap-analysis.md`
- `00-inbox/flow-docs/prd-guide.md` (PRD checklist)

## Summary

**Review 1 (2026-02-22):** Found 1 high, 7 medium, 5 low gaps. All resolved.

**Review 2 (2026-02-25):** After adding Default Introduction and Default Terms masters, re-reviewed the full PRD (now 10 sections, 15 event types, 15 screens, 8 reports). Found 0 high, 4 medium, 6 low new issues. All resolved. PRD guide checklist passes fully. All 16 MVP functional requirements and 6 non-functional requirements are covered.

## Gaps Found

| # | File | Section | Gap | Severity |
|---|---|---|---|---|
| G1 | PRD, entity QuotationVersion | Field definitions | Header and footer fields missing. Observation says page 1 has "customizable header, footer, and introduction text." Screen 11a description says "Edit introduction text, header fields." But the entity only has `introduction_text` — no header or footer fields. | High |
| G2 | PRD | Missing section | Letterhead template management has no entity, screen, or process step. Resolved Q1 in gap analysis says "replicate Steefo's letterhead design in system templates" but the PRD has no mechanism for uploading or configuring the letterhead. | Medium |
| G3 | PRD | Throughout | "Technical offer" is Steefo's actual term for the output document (PDF titles say "Technical Offer QTN-542-R2"). The PRD uses "quotation" exclusively. Could confuse end users. | Medium |
| G4 | PRD, entity QuotationVersion | Field definitions | No `created_by` field. Gap analysis role table says builder can "Edit Quotations (own drafts)" implying ownership. PRD has no ownership model. | Medium |
| G5 | User journeys | Edge cases | Missing catalog item scenario (process map Exception C) not covered. Builder needs an item not in the catalog — contacts admin, admin uploads, builder refreshes. | Medium |
| G6 | PRD | Section 3 | Exclusion Template CRUD (3 event types, 3 screens) was added without an explicit source requirement in the gap analysis. Reasonable inference from "template-based suggestions" but not formally traced. | Medium |
| G7 | User journeys | Ramesh workflow | Page counts don't match observations. User journey says 14 items = ~52 equipment pages. Observations say QTN-569 pages 5-70 = ~66 equipment pages for similar items. | Medium |
| G8 | PRD | Process overview / user journeys | Cover page ambiguity. Observation says cover page has "project code, quotation code, date." User journey lists page 1 as Introduction. Is the cover page the introduction page, or a separate page? | Medium |
| G9 | PRD | Open Question 3 | References "screen 10d" — should be "screen 11d" after renumbering. | Low |
| G10 | PRD | Section 2 | S and C abbreviations never defined. Should state S = Steefo (Supplier), C = Customer at least once. | Low |
| G11 | All docs | Throughout | "Super admin" vs "Super Admin" and "quotation builder" vs "Quotation Builder" — inconsistent capitalization. | Low |
| G12 | PRD | Section 4 | Catalog item deactivation is terminal (no reactivation). Not explicitly discussed with Steefo. If admin deactivates by mistake, must create a new item from scratch. | Low |
| G13 | PRD | Not present | NF4 (handle up to 200 pages) and NF5 (PDF upload ~10 pages each) not formalized as constraints. | Low |

## Questions and Resolutions

1. **G1:** Header/footer fields — **Resolved.** The header (REF NO., DATE, Page X of Y) is entirely system-generated from existing fields (project_code, qtn_code, date, page numbers). No additional entity fields needed. Screen 11a description updated to clarify header is not editable.

2. **G2:** Letterhead management — **Resolved.** Letterhead is always the same across all quotations. Static template hardcoded by developer. No management screen needed. Note added to PRD Process Overview.

3. **G3:** Terminology — **Resolved.** System UI should use "Technical Offer" to match Steefo's language. PRD retains "quotation" in entity/code names for brevity. Terminology note added to PRD Section 1.

4. **G4:** Ownership model — **Resolved.** Any builder can edit any draft quotation. No ownership model needed. PRD is correct as-is. Gap analysis "own drafts" phrasing was informal, not a requirement.

5. **G5:** Missing catalog item — **Resolved.** Handled outside the system (phone/WhatsApp). No in-system "Request Item" feature. Edge case added to user journeys.

6. **G6:** Exclusion Template CRUD — **Resolved.** Approved as in scope. Formally traced from gap analysis F10 ("template-based suggestions").

7. **G8:** Cover page — **Resolved.** Introduction page IS the cover page (same page). Consistent with QTN-569 PDF page 1. Note added to user journey PDF preview section.

8. **G12:** Reactivation — **Resolved.** Admin can reactivate mistakenly deactivated items and templates. Added CATALOG_ITEM_REACTIVATED and EXCLUSION_TEMPLATE_REACTIVATED event steps, updated state machines, permissions, reports, screens, and flowcharts.

### Unresolved (accepted as-is)

- **G7:** Page count estimates left as rough approximations. Exact counts will vary by quotation.
- **G10:** S/C abbreviation definition added to PRD Section 2.
- **G11:** Capitalization inconsistency noted. Not blocking — will standardize during implementation.
- **G13:** Now resolved — NFR section added to PRD in Review 2.

---

## Review 2 — 2026-02-25

### Context

PRD was updated to add Default Introduction and Default Terms master entities. Full second review pass performed.

### New Gaps Found

| # | File | Section | Gap | Severity | Resolution |
|---|---|---|---|---|---|
| G14 | PRD | Missing section | No NFR section. Gap analysis NF1-NF6 not formalized in the PRD. | Medium | Added Section 8 (Non-Functional Requirements) with all 6 NFRs. |
| G15 | PRD | Section 3, QUOTATION_CREATED | V1 creation event stored against Quotation aggregate, not QuotationVersion. Report 7 (version history) would be incomplete for V1. | Medium | Added cascading QUOTATION_VERSION_CREATED event for V1 in QUOTATION_CREATED side effects. |
| G16 | PRD | Section 3, QUOTATION_VERSION_LOCKED | Exclusion template text fetching behavior undocumented. Text fetched at lock time (live) but not stated. | Medium | Added explicit note to lock step: exclusion text fetched at lock time, same as catalog item PDFs. |
| G17 | PRD | Section 2, scope_rows / Screen 12f | Scope of Supply qty and description column editability unspecified. | Medium | Resolved: qty editable, description read-only. Updated field definition and screen description. |
| G18 | PRD | Section 2 | `created_at` fields not in any event payload. Convention not documented. | Low | Added Conventions note: `created_at` derived from event `occurred_at`. |
| G19 | PRD | Section 3, QUOTATION_CREATED | `version_code` not in payload, but present in QUOTATION_VERSION_CREATED. Inconsistency. | Low | Added `version_code` to QUOTATION_CREATED payload. |
| G20 | PRD | Section 3, QUOTATION_VERSION_LOCKED | PDF file naming convention not documented. | Low | Added: `{project_code}-{qtn_code}-V{N}.pdf`. |
| G21 | PRD | Section 2 | Default content entities have no CREATE event. Initial data seeded by developer. | Low | Accepted. Added seeding note. Direct database seed is fine; event trail begins from first admin update. |
| G22 | PRD | Screen 10 | Quotation date not shown on list screen. | Low | Accepted. Date visible when opening the quotation. List shows project code, QTN code, version, status. |
| G23 | PRD | Screen 10, Screen 1 | No search/filter beyond status filters on list screens. | Low | Accepted. Volume too low (~20 items, 1-5 quotations/month) to justify search. |

### Changes Made (Review 2)

#### PRD (`001-quotation-tool-prd.md`)

19. Added Section 8 (Non-Functional Requirements) with 6 NFRs from gap analysis. Renumbered Screen List to Section 9, Process Flowchart to Section 10. (G14)
20. Added cascading QUOTATION_VERSION_CREATED event for V1 in QUOTATION_CREATED side effects. (G15)
21. Added exclusion text lock-time fetching note to QUOTATION_VERSION_LOCKED side effects. (G16)
22. Updated scope_rows field description: qty editable, description read-only. (G17)
23. Updated Screen 12f description: qty editable, description read-only. (G17)
24. Updated Screen 12h description: show full clause text next to checkboxes. (G16)
25. Added Conventions note in Section 2: `created_at` and `updated_at` derived from event `occurred_at`. (G18)
26. Added `version_code` to QUOTATION_CREATED payload. (G19)
27. Added PDF file naming convention to QUOTATION_VERSION_LOCKED side effects. (G20)
28. Added seeding note for Default Introduction and Default Terms entities. (G21)
29. Updated Screen 12f screen note: read-only description column, editable quantity column. (G17)

#### User Journeys (`002-user-journeys.md`)

No changes needed in Review 2. User journeys already updated from default content addition.

## Changes Made

### PRD (`001-quotation-tool-prd.md`)

1. Fixed screen reference in Open Question 3: "screen 10d" → "screen 11d" (G9).
2. Added terminology note to Section 1: system UI should use "Technical Offer" (G3).
3. Added letterhead note to Section 1: static template, hardcoded by developer (G2).
4. Added S/C abbreviation definitions to Section 2 (G10).
5. Updated screen 11a description: header is system-generated, not editable (G1).
6. Added `CATALOG_ITEM_REACTIVATED` step definition to Section 3 (G12).
7. Added `EXCLUSION_TEMPLATE_REACTIVATED` step definition to Section 3 (G12).
8. Updated Catalog Item state machine: added `inactive → CATALOG_ITEM_REACTIVATED → active` transition (G12).
9. Updated Exclusion Template state machine: added `inactive → EXCLUSION_TEMPLATE_REACTIVATED → active` transition (G12).
10. Added 2 reactivation permissions to Section 6 permissions table (G12).
11. Added reactivation events to Reports 1 and 2 in Section 5 (G12).
12. Added "Reactivate" action to screens 3 (Catalog Item Detail) and 5 (Exclusion Template Detail) (G12).
13. Updated Catalog Management flowchart with reactivation edges (G12).
14. Updated Process Overview flow diagram to include all 13 event types.
15. Added note on conditional Deactivate/Reactivate button visibility on screens 3 and 5.

### User Journeys (`002-user-journeys.md`)

16. Added "Builder needs a catalog item that does not exist" edge case (G5).
17. Added cover page clarification: page 1 = introduction page = cover page (G8).
18. Updated frontmatter dates on both files.
