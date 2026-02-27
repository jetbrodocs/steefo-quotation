---
title: "Change Note #1: Production Table Specification"
status: draft
created: 2026-02-27
updated: 2026-02-27
tags: [solution-design, change-note, production-table]
---

# Change Note #1: Production Table Specification

**Resolves:** PRD Open Question #3 (Excel-to-table conversion)
**Source:** `00-inbox/Production Chart Working_P512.xlsx` — actual production chart received from Steefo for project P512.
**PRD Reference:** `40-solution-design/001-quotation-tool-prd.md`

---

## Summary

The builder uploads an Excel file containing a production chart. The system parses it into structured JSON (`production_table_data`) for PDF rendering. Page 4 of the technical offer renders both a Design Parameters box and a Production Table grid from this data.

The Excel file contains **two distinct sections** that map to the PDF output:

1. **Design Parameters** — 8 key-value fields rendered as a header box
2. **Production Table** — a data grid with 11 columns and variable rows (one per bar size)
3. **Summary statistics** — 4 calculated values rendered below the table

---

## 1. Design Parameters Fields

These render as a two-column key-value box at the top of the production table page.

| Field | Example Value | Unit | Side |
|---|---|---|---|
| Finished Product Requirement | 160,000 | TPA | Left |
| Billet Requirement | 166,400 | TPA | Left |
| Billet Size | 130 | Sq. | Left |
| Billet Length | 6 | m | Left |
| Billet Weight | 780 | kg | Left |
| Per Hour Production | 25 to 30 | T/hr | Right |
| Maximum Finishing Speed | 25 | m/sec | Right |
| Average Yield | 96 | % | Right |

### PRD Impact

The PRD currently has `mill_production`, `basic_raw_material`, `finished_products` (page 2 — Technical Parameters) and `power_requirement` (page 3 — Basic Data) as separate editable string fields. Those remain unchanged.

The 8 Design Parameters above are **new fields** that live inside the `production_table_data` JSON. They are parsed from the Excel upload, not manually entered. The builder can re-upload to change them.

### Proposed `production_table_data` JSON structure

```json
{
  "design_parameters": {
    "finished_product_requirement": {"value": "160,000", "unit": "TPA"},
    "billet_requirement": {"value": "166,400", "unit": "TPA"},
    "billet_size": {"value": "130", "unit": "Sq."},
    "billet_length": {"value": "6", "unit": "m"},
    "billet_weight": {"value": "780", "unit": "kg"},
    "per_hour_production": {"value": "25 to 30", "unit": "T/hr"},
    "maximum_finishing_speed": {"value": "25", "unit": "m/sec"},
    "average_yield": {"value": "96", "unit": "%"}
  },
  "production_rows": [
    {
      "product_type": "TMT BARS",
      "size_mm": "8",
      "no_of_strands": 1,
      "weight_per_m_kg": 0.390,
      "rolling_speed_m_sec": 25,
      "rolling_length_m": 2000,
      "rolling_time_sec": 80,
      "theoretical_capacity_t_hr": 35.10,
      "actual_capacity_t_hr": 25,
      "annual_rolling_pct": 15,
      "billet_req_tpa": null,
      "prod_time_hrs": 960
    }
  ],
  "summary": {
    "total_annual_rolling_pct": 100,
    "total_billet_req_tpa": 166400,
    "total_prod_time_hrs": 5343,
    "finished_production_yield_pct": 96,
    "finished_production_tpa": 160000,
    "rolling_hrs_available": 7920,
    "hours_required": 5343,
    "mill_utilisation_pct": 67.47
  }
}
```

---

## 2. Production Table Columns

The grid has 11 data columns. Each row represents one bar size.

| # | Column Header | Sub-header | Key | Type | Notes |
|---|---|---|---|---|---|
| 1 | Product Type | — | `product_type` | string | "TMT BARS" or "WIRE ROD". Spans multiple rows in PDF. |
| 2 | (size) | mm | `size_mm` | string | Bar diameter. E.g., "8", "10", "5.5" |
| 3 | No. of Strand(s) | — | `no_of_strands` | integer | Always 1 in samples seen. |
| 4 | Weight/m | kg | `weight_per_m_kg` | decimal | Weight per meter in kilograms. |
| 5 | Rolling Speed | m/sec | `rolling_speed_m_sec` | decimal | Rolling speed in meters per second. |
| 6 | Rolling Length | m | `rolling_length_m` | decimal | Calculated rolling length in meters. |
| 7 | Rolling Time | sec | `rolling_time_sec` | decimal | Calculated rolling time in seconds. |
| 8 | Th. Rolling Capacity | T/hr | `theoretical_capacity_t_hr` | decimal | Theoretical rolling capacity. |
| 9 | Actual Rolling Capacity | T/hr | `actual_capacity_t_hr` | decimal | Actual (derated) rolling capacity. |
| 10 | Annual Production — Rolling %age | — | `annual_rolling_pct` | decimal | Percentage of annual production for this size. Must sum to 100. |
| 10a | Annual Production — Billet Req. | TPA | `billet_req_tpa` | decimal | Billet requirement in tonnes per annum. Single value spanning all rows in same product group. |
| 11 | Annual Prod. Time | Hrs. | `prod_time_hrs` | decimal | Annual production time in hours for this size. |

### Row variations observed

- **TMT BARS only** (QTN-569 page 4, P512 table 2): 7 rows for sizes 8, 10, 12, 16, 20, 25, 32mm. Product type = "TMT BARS" for all.
- **TMT BARS + WIRE ROD** (P512 table 1): 7 TMT rows + 1 Wire Rod row (5.5mm). Two product types.

The number of rows and sizes varies per quotation. The system should parse whatever rows exist in the Excel.

---

## 3. Summary Statistics

Rendered below the production table grid.

| Label | Key | Unit | Source |
|---|---|---|---|
| Total (in Actual Rolling Capacity column) | `total_annual_rolling_pct` | — | Sum of `annual_rolling_pct` (must = 100) |
| Total Billet Req. | `total_billet_req_tpa` | TPA | Sum or stated total |
| Total Prod. Time | `total_prod_time_hrs` | Hrs. | Sum of `prod_time_hrs` |
| Finished Production at an average {X}% yield | `finished_production_tpa` | TPA | Calculated from total × yield |
| No. of Rolling Hrs available in a year | `rolling_hrs_available` | hrs | Typically 7,920 (330 days × 24 hrs) |
| Hours required for production | `hours_required` | hrs | Same as total_prod_time_hrs |
| Mill Utilisation | `mill_utilisation_pct` | % | hours_required / rolling_hrs_available × 100 |

---

## 4. Excel Parsing Rules

The Excel file has a single sheet. The parser should:

1. **Find the header row** by scanning for a row containing "Product" and "Weight/m" (or "Rolling Speed").
2. **Read data rows** below the header until hitting an empty row or a "Total" row.
3. **Find Design Parameters** by scanning for "DESIGN PARAMETERS" or "Finished Product Requirement" label.
4. **Find summary rows** by scanning for "Total", "Finished Production", "Rolling Hrs", "Hours required", "Mill Utilisation" labels below the data rows.

The Excel may contain **two tables** (one with Wire Rod, one TMT-only). The builder selects which table applies to their quotation. For MVP, parse the **first table found** and let the builder re-upload if they need a different one.

### Cell positions are not fixed

The Excel uses merged cells and varying layouts. Parse by label matching, not by fixed cell coordinates. The header text labels ("Product Type", "mm", "Weight/m", etc.) are reliable anchors.

---

## 5. Screen 12d Update

The Production Table section (screen 12d) should work as follows:

1. Builder clicks "Upload" and selects an `.xlsx` file.
2. System parses the Excel using the rules above.
3. System displays a preview showing:
   - Design Parameters box (8 fields)
   - Production Table grid (all rows and columns)
   - Summary statistics
4. Builder reviews. If wrong, re-uploads a corrected file.
5. Builder clicks "Save" to store `production_table_file_url` and `production_table_data`.

The production table page is **read-only in the UI** — the builder cannot edit individual cells. All edits happen in Excel, then re-upload. This matches Steefo's current workflow where they prepare the production chart in Excel first.

---

## 6. PDF Rendering

The production table page in the PDF should render as shown on page 4 of QTN-569:

1. **Design Parameters box** at top — blue header bar, two-column layout (5 fields left, 3 fields right), values highlighted in orange/yellow.
2. **Production Table heading** — e.g., "PRODUCTION TABLE - TMT BAR" with blue header bar.
3. **Column headers** — two header rows (main header + unit sub-header), blue background.
4. **Data rows** — alternating or plain white background, orange/yellow highlighted values.
5. **Total row** — bold, at bottom of data rows.
6. **Summary statistics** — below the table, each on its own row with blue background label and orange highlighted value.

---

## 7. Seed Data

Sample file: `60-dev-handoff/seed-data/production-chart-p512.xlsx`

This is the actual P512 production chart. It contains two tables:
- **Table 1** (rows 7-17): TMT BARS + WIRE ROD, 150,000 TPA at 97% yield
- **Table 2** (rows 36-47): TMT BAR only, 200,000 TPA at 96% yield

Use Table 2 for test quotation seeding (matches the TMT-only configuration in QTN-569 page 4).

---

## Open Questions

None. The Excel file structure is well-defined and consistent across the samples.
