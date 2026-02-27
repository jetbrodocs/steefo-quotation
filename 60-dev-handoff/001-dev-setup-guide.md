---
title: "Dev Setup Guide: Sample Data and Seed Files"
status: draft
created: 2026-02-25
updated: 2026-02-25
tags: [dev-handoff, setup, seed-data]
---

# Dev Setup Guide: Sample Data and Seed Files

This folder contains everything needed to seed the quotation tool with real Steefo data during development. All content is extracted from two actual technical offers provided by Steefo.

## Source Documents

| Document | File | Pages | Items |
|---|---|---|---|
| QTN-542-R2 | `00-inbox/Technical Offer_QTN-542-R2_P460.pdf` | 42 | 11 equipment items (no Wire Rod Mill or Central Oil Lubrication) |
| QTN-569 | `00-inbox/Technical Offer_QTN-569_P480.pdf` | 75 | 13 equipment items (includes Wire Rod Block Mill + Central Oil Lubrication) |

---

## Folder Structure

```
60-dev-handoff/
├── 001-dev-setup-guide.md          ← This file
├── split-pdfs.py                   ← Script to regenerate item PDFs from source
├── extract-seed-data.py            ← Script to regenerate seed text from source
├── sample-pdfs/
│   ├── qtn-542-items/              ← 11 split equipment item PDFs
│   └── qtn-569-items/              ← 13 split equipment item PDFs
└── seed-data/
    ├── default-introduction.txt    ← Clean introduction text for DefaultIntroduction entity
    ├── default-terms.txt           ← Clean terms text for DefaultTerms entity
    ├── exclusion-templates.txt     ← 11 exclusion clauses, one per line
    ├── introduction-raw.txt        ← Raw pdfplumber extraction (with headers/footers)
    ├── terms-qtn-542-raw.txt       ← Raw terms extraction from QTN-542
    ├── terms-qtn-569-raw.txt       ← Raw terms extraction from QTN-569
    ├── production-chart-p512.xlsx   ← Sample production chart Excel (P512)
    ├── exclusions-qtn-542-raw.txt  ← Raw exclusions extraction from QTN-542
    ├── exclusions-qtn-569-raw.txt  ← Raw exclusions extraction from QTN-569
    ├── scope-of-supply-qtn-542-raw.txt  ← Raw scope table text from QTN-542
    └── scope-of-supply-qtn-569-raw.txt  ← Raw scope table text from QTN-569
```

---

## 1. Catalog Items (PRD entity: `CatalogItem`)

Use the QTN-569 item set as the primary seed catalog — it has 13 items and represents the larger, more complete product line. QTN-542 items overlap but have fewer pages per item (different spec level).

### QTN-569 Equipment Items → Catalog Seed

| # | File | Name | Category | Pages | Scope Rows (approx.) |
|---|---|---|---|---|---|
| 1 | `01-550mm-heavy-duty-roughing-mill.pdf` | 550mm Heavy Duty Roughing Mill | Mill Equipment | 4 | 9 rows (1.1-1.9) |
| 2 | `02-400mm-continuous-intermediate-mill.pdf` | 400mm Continuous Intermediate Mill | Mill Equipment | 3 | 6 rows (2.1-2.6) |
| 3 | `03-360mm-continuous-intermediate-mill.pdf` | 360mm Continuous Intermediate Mill | Mill Equipment | 3 | 6 rows (3.1-3.6) |
| 4 | `04-320mm-continuous-intermediate-mill.pdf` | 320mm Continuous Intermediate Mill | Mill Equipment | 3 | 6 rows (4.1-4.6) |
| 5 | `05-280mm-continuous-finishing-mill-4-stand.pdf` | 280mm Continuous Finishing Mill | Mill Equipment | 3 | 6 rows (5.1-5.6) |
| 6 | `06-auxiliary-equipment.pdf` | Auxiliary Equipment | Auxiliary Equipment | 7 | 12 rows (6.1-6.12) |
| 7 | `07-electricals.pdf` | Electricals | Electricals | 9 | 14 rows (7.1-7.14) |
| 8 | `08-automatic-cooling-bed-twin-channel-cold-shear.pdf` | Automatic Cooling Bed with Twin Channel & Cold Shear | Cooling & Finishing | 4 | 4 rows (8.1-8.4) |
| 9 | `09-continuous-operating-dividing-shear-tmt-bars.pdf` | Continuous Operating Dividing Shear for TMT Bars | Cooling & Finishing | 1 | 1 row (item 9) |
| 10 | `10-bar-finishing-bundling-tying-machine.pdf` | Bar Finishing, Bundling & Tying Machine | Cooling & Finishing | 2 | 4 rows (10.1-10.4) |
| 11 | `11-tmt-system.pdf` | TMT System | TMT | 6 | 10 rows (11.1-11.10) |
| 12 | `12-central-oil-lubrication-system.pdf` | Central Oil Lubrication System | Auxiliary Equipment | 2 | 1 row (item 12) |
| 13 | `13-wire-rod-block-mill.pdf` | Wire Rod Block Mill | Mill Equipment | 15 | ~40 rows (sections A-K in wire rod scope table) |

### QTN-542 Equipment Items (alternate variant set)

These overlap with QTN-569 but represent a different product line configuration. Useful for testing builders selecting different item variants.

| # | File | Name | Category | Pages |
|---|---|---|---|---|
| 1 | `01-510mm-heavy-duty-roughing-mill.pdf` | 510mm Heavy Duty Roughing Mill | Mill Equipment | 4 |
| 2 | `02-410mm-continuous-intermediate-mill.pdf` | 410mm Continuous Intermediate Mill | Mill Equipment | 3 |
| 3 | `03-360mm-continuous-intermediate-mill.pdf` | 360mm Continuous Intermediate Mill | Mill Equipment | 3 |
| 4 | `04-320mm-continuous-intermediate-mill.pdf` | 320mm Continuous Intermediate Mill | Mill Equipment | 3 |
| 5 | `05-280mm-continuous-finishing-mill-6-stand.pdf` | 280mm Continuous Finishing Mill (6-Stand) | Mill Equipment | 3 |
| 6 | `06-auxiliary-equipment.pdf` | Auxiliary Equipment | Auxiliary Equipment | 3 |
| 7 | `07-electricals.pdf` | Electricals | Electricals | 1 |
| 8 | `08-automatic-cooling-bed-twin-channel-cold-shear.pdf` | Automatic Cooling Bed with Twin Channel & Cold Shear | Cooling & Finishing | 4 |
| 9 | `09-bar-finishing-bundling-tying-machine.pdf` | Bar Finishing, Bundling & Tying Machine | Cooling & Finishing | 3 |
| 10 | `10-tmt-system.pdf` | TMT System | TMT | 4 |
| 11 | `11-utm-machine.pdf` | UTM Machine | Testing | 1 |

### Scope Row Template Format

Each catalog item needs `scope_row_templates` as a JSON array. Each row has these fields:

```json
{
  "sr_no": "1.1",
  "description": "High Speed Flywheel",
  "qty": "1 No.",
  "basic_data": "S",
  "basic_design": "S",
  "detailed_design": "S",
  "supply": "S",
  "supervision_of_erection": "S",
  "erection_and_comm": "C",
  "supervision_of_comm": "S"
}
```

The 7 responsibility columns are: `basic_data`, `basic_design`, `detailed_design`, `supply`, `supervision_of_erection`, `erection_and_comm`, `supervision_of_comm`. Values are `"S"` (Steefo) or `"C"` (Customer).

The scope of supply data is in `seed-data/scope-of-supply-qtn-569-raw.txt`. Pages 53-55 contain the main rolling mill scope (items 1-12), pages 71-72 contain the wire rod mill scope (item 13).

**Key pattern from the data:** Most columns default to `S` except `erection_and_comm` which is typically `C`. This is the standard Steefo pattern — they supply everything but the customer handles erection.

---

## 2. Exclusion Templates (PRD entity: `ExclusionTemplate`)

File: `seed-data/exclusion-templates.txt` — one clause per line, 11 total.

Seed the database with these 11 exclusion templates. QTN-569 uses 11 exclusions, QTN-542 uses 9 (a subset). The QTN-569 set is the more complete one.

| # | Clause Text |
|---|---|
| 1 | Shed (Hanger), Cranes, Rails & DSL for Crane |
| 2 | HT Side, Transformers, all Cables, Capacitors & Earthing |
| 3 | All Civil Work and Mill Foundations including water & electrical trenches. |
| 4 | Fabrication on Site like – Trough, Charging Rack, Walk Ways, etc. |
| 5 | Interconnecting Air, Oil, Water & Hydraulic Pipe Lines |
| 6 | Re Heating Furnace |
| 7 | Workshop Machinery including, Air Compressor CNC Rib Cutting & Roll Branding Machine |
| 8 | Material Testing Equipment |
| 9 | Bought out Items like Rolls, Bearings, etc. |
| 10 | Erection and Installation |
| 11 | First Fill of Lubricants |

---

## 3. Default Introduction (PRD entity: `DefaultIntroduction`)

File: `seed-data/default-introduction.txt`

Single record. Seed via database migration. The text is identical in both QTN-542 and QTN-569 — this is Steefo's standard introduction paragraph that appears on page 1 of every technical offer.

The introduction text is 6 paragraphs covering: company overview, core activities, 45-year experience, design capability, 20-country track record, and project satisfaction.

---

## 4. Default Terms (PRD entity: `DefaultTerms`)

File: `seed-data/default-terms.txt`

Single record. Seed via database migration. Contains two sections:

1. **Preferred Make of Standard Boughtout Items** — a list of ~25 component categories with approved manufacturer names
2. **Consultation & Supervision of Erection, Installation & Commissioning** — scope of services (5 items) and facilities the client must provide (7 items)

Note: The terms text varies slightly between quotations (e.g., QTN-542 has "30 KV" high voltage spec, QTN-569 has "33 KV"). The seed data uses the QTN-569 version. Builders edit per-quotation.

---

## 5. Page Map Reference

### QTN-542-R2 (42 pages) — Document Structure

| Pages | Content | Content Type |
|---|---|---|
| 1 | Introduction (cover page) | System-generated |
| 2 | Technical Parameters | System-generated |
| 3 | Basic Data & Media Requirements | System-generated |
| 4 | Summary / Equipment List | System-generated |
| 5-8 | 510mm Heavy Duty Roughing Mill | PDF stitch |
| 9-11 | 410mm Continuous Intermediate Mill | PDF stitch |
| 12-14 | 360mm Continuous Intermediate Mill | PDF stitch |
| 15-17 | 320mm Continuous Intermediate Mill | PDF stitch |
| 18-20 | 280mm Continuous Finishing Mill (6-Stand) | PDF stitch |
| 21-23 | Auxiliary Equipment | PDF stitch |
| 24 | Electricals | PDF stitch |
| 25-28 | Automatic Cooling Bed with Twin Channel & Cold Shear | PDF stitch |
| 28 | Continuous Operating Dividing Shear (bottom of page, shares with Cooling Bed) | PDF stitch |
| 29-31 | Bar Finishing, Bundling & Tying Machine | PDF stitch |
| 32-35 | TMT System | PDF stitch |
| 36 | UTM Machine | PDF stitch |
| 37-39 | Scope of Supply table | System-generated |
| 40 | Preferred Make of Standard Boughtout Items | System-generated |
| 41 | Scope of Services & Facilities | System-generated |
| 42 | Exclusions | System-generated |

### QTN-569 (75 pages) — Document Structure

| Pages | Content | Content Type |
|---|---|---|
| 1 | Introduction (cover page) | System-generated |
| 2 | Technical Parameters | System-generated |
| 3 | Basic Data & Media Requirements | System-generated |
| 4 | Design Parameters & Production Table | System-generated (from Excel upload) |
| 5 | Summary / Equipment List | System-generated |
| 6-9 | 550mm Heavy Duty Roughing Mill | PDF stitch |
| 10-12 | 400mm Continuous Intermediate Mill | PDF stitch |
| 13-15 | 360mm Continuous Intermediate Mill | PDF stitch |
| 16-18 | 320mm Continuous Intermediate Mill | PDF stitch |
| 19-21 | 280mm Continuous Finishing Mill (4-Stand) | PDF stitch |
| 22-28 | Auxiliary Equipment | PDF stitch |
| 29-37 | Electricals | PDF stitch |
| 38-41 | Automatic Cooling Bed with Twin Channel & Cold Shear | PDF stitch |
| 42 | Continuous Operating Dividing Shear for TMT Bars | PDF stitch |
| 43-44 | Bar Finishing, Bundling & Tying Machine | PDF stitch |
| 45-50 | TMT System | PDF stitch |
| 51-52 | Central Oil Lubrication System | PDF stitch |
| 53-55 | Scope of Supply (main rolling mill) | System-generated |
| 56-70 | Wire Rod Block Mill | PDF stitch |
| 71-72 | Scope of Supply (wire rod mill) | System-generated |
| 73 | Preferred Make of Standard Boughtout Items | System-generated |
| 74 | Consultation & Supervision / Scope of Services | System-generated |
| 75 | Exclusions | System-generated |

**Note on QTN-569 structure:** This quotation has two separate scope of supply tables — one for the main rolling mill (pages 53-55, after the main equipment items) and one for the wire rod mill (pages 71-72, after the Wire Rod Block Mill item pages). In the system, these merge into a single Scope of Supply section since the scope table auto-populates from all selected items.

---

## 6. Seeding Instructions

### Step 1: Default Content (database migration)

Seed `DefaultIntroduction` and `DefaultTerms` with a fixed UUID each:

```sql
INSERT INTO default_introductions (id, content, updated_at)
VALUES ('00000000-0000-0000-0000-000000000001', '<content from default-introduction.txt>', NOW());

INSERT INTO default_terms (id, content, updated_at)
VALUES ('00000000-0000-0000-0000-000000000002', '<content from default-terms.txt>', NOW());
```

### Step 2: Exclusion Templates (seed script)

Read `seed-data/exclusion-templates.txt` line by line. Create one `ExclusionTemplate` per line with `display_order` matching line number and `status = 'active'`.

### Step 3: Catalog Items (seed script)

For each item PDF in `sample-pdfs/qtn-569-items/`:

1. Upload the PDF to file storage
2. Create a `CatalogItem` with name, description, category from the table in Section 1
3. Parse the scope of supply data from `seed-data/scope-of-supply-qtn-569-raw.txt` to populate `scope_row_templates`
4. Set `display_order` matching the item number, `status = 'active'`

### Step 4: Users (seed script)

Create two users per PRD:

| Username | Role | Notes |
|---|---|---|
| suril | super_admin | Can manage catalog, templates, default content, users, and build quotations |
| ramesh | quotation_builder | Can create and edit quotations |

### Step 5: Verify

After seeding, verify by creating a test quotation:
1. Log in as ramesh
2. Create new quotation (project code: P480, QTN code: QTN569, date: 05/12/2025)
3. Verify introduction is pre-filled from DefaultIntroduction
4. Select all 13 equipment items
5. Verify scope of supply table has ~80+ rows auto-populated
6. Verify terms are pre-filled from DefaultTerms
7. Select all 11 exclusion templates
8. Preview PDF — should resemble QTN-569 structure

---

## 7. Regenerating Files

If the source PDFs change or you need to regenerate:

```bash
# From project root
python3 60-dev-handoff/split-pdfs.py        # Regenerate item PDFs
python3 60-dev-handoff/extract-seed-data.py  # Regenerate seed text files
```

Requires: `pip install pypdf pdfplumber`
