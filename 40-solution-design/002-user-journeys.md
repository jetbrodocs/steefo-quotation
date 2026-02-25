---
title: "User Journeys: Steefo Quotation Preparation Tool"
status: draft
created: 2026-02-21
updated: 2026-02-25
tags: [solution-design, user-journeys, quotation]
---

# User Journeys: Steefo Quotation Preparation Tool

Companion document to `001-quotation-tool-prd.md`.

---

## Super Admin (Suril)

### Who they are

Suril Agarwal is the owner of Steefo Engineering Corporation. He manages the equipment catalog, exclusion templates, default content (introduction and terms), and user accounts. He also builds quotations himself.

### Their typical workflow

**Setting up the catalog (one-time, then maintained as equipment changes)**

1. Suril logs into the system. He sees the Quotation List as the landing page.
2. He navigates to Catalog Management from the menu.
3. He sees an empty catalog (first time) or the existing list of equipment items.
4. He clicks "Add Item". The form appears.
5. He enters:
   - Name: "550mm Heavy Duty Roughing Mill"
   - Description: "1 Stand, 550mm (22 inch) heavy duty roughing mill"
   - Category: "Mill Equipment"
6. He uploads the PDF file for this item (6 pages of technical drawings and specs).
7. The system shows the uploaded PDF preview and the page count (6 pages).
8. He defines the scope of supply rows for this item. He adds 11 rows:
   - 1.1 High Speed Flywheel, Qty: 1 No., all columns S except Erection & Comm. = C
   - 1.2 Reduction Gear Box, Qty: 2 Nos., same pattern
   - ... (9 more sub-items)
   - For each row, he sets the default S or C per column. Most are S for Steefo. Erection & Comm. is typically C for Customer.
9. He clicks "Save". The item appears in the catalog with code ITEM-0001.
10. He repeats for each equipment item. After 30 minutes, the catalog has 14 items with a total of ~60 scope rows across all items.

**Adding a new equipment item later**

1. A month later, Steefo designs a new "Central Oil Lubrication System" item.
2. Suril navigates to Catalog Management, clicks "Add Item".
3. He fills in the name, description, uploads the PDF.
4. He defines 3 scope rows for lubrication-related sub-items.
5. Saves. The item is immediately available to all builders for new quotations.

**Managing exclusion templates**

1. Suril navigates to Exclusion Templates from the menu.
2. He clicks "Add Template" and enters: "Shed (Hanger), Cranes, Rails & DSL for Crane"
3. He repeats for each standard exclusion clause. After 5 minutes, 9 templates exist.
4. Builders can now pick from these when assembling quotations.

**Managing default content (one-time setup, then updated as needed)**

1. Suril navigates to Default Content from the menu.
2. He sees two sections: Introduction and Terms & Conditions.
3. In the Introduction section, he pastes Steefo's standard introduction paragraph — the same text that appears on page 1 of every technical offer. He clicks "Save Introduction".
4. In the Terms & Conditions section, he pastes the standard terms text — preferred makes of boughtout items, scope of services, facilities to implement project. He clicks "Save Terms".
5. From now on, every new quotation will be pre-filled with this text. Builders can still edit it per-quotation.
6. Six months later, Steefo updates their standard terms to include a new payment clause. Suril returns to Default Content, edits the Terms section, and saves. New quotations pick up the updated text. Existing drafts and locked versions are unaffected.

**Adding a new user**

1. A new staff member joins and needs to prepare quotations.
2. Suril navigates to User Management, clicks "Add User".
3. He enters the username and password, selects the "Quotation Builder" role.
4. Saves. The new user can now log in and build quotations.

### What success looks like

The catalog has all current equipment items with accurate PDFs and scope rows. Exclusion templates cover the standard clauses. Default introduction and terms are set up so new quotations start pre-filled. When a builder creates a quotation, every item they need is available in the catalog. Suril only touches the admin screens when equipment specs change, a new item is designed, or the standard text needs updating.

---

## Quotation Builder (Ramesh)

### Who they are

Ramesh is one of 2-3 staff members at Steefo who prepare technical offers. He has basic computer skills. He receives customer enquiries and assembles quotations using the system.

### Their typical workflow

**Creating a new quotation**

1. A customer enquiry arrives by email for a 160,000 TPA rolling mill. Ramesh reviews the requirements: they need a roughing mill, intermediate mills, finishing mill, auxiliary equipment, electricals, cooling bed, TMT system, and UTM machine.
2. Ramesh logs into the system. He sees the Quotation List showing existing quotations.
3. He clicks "New Quotation".
4. He enters:
   - Project Code: P480
   - QTN Code: QTN569
   - Date: 05/12/2025
5. He clicks "Create". The system creates P480-QTN569-V1 and opens the editor.

**Editing the front pages (5 minutes)**

6. The Introduction section is pre-filled with text from the Default Introduction master. Ramesh reads it. No changes needed for this project. He moves to the next section.
7. In Technical Parameters, he fills in:
   - Mill Production: "25 to 30 Tons / Hr."
   - Basic Raw Material: "Billets 100 & 130 mm"
   - Finished Products: "8 mm Ø to 32mm High Strength TMT Re Bars, Wire Rod Mill 5.5mm to 8mm"
8. In Basic Data, he fills in:
   - Power Requirement: "3 MW"
9. He clicks "Save". The system confirms the save. He can close the browser and come back tomorrow.

**Uploading the production table (2 minutes)**

10. Ramesh has an Excel file with rolling parameters for this project. He navigates to the Production Table section.
11. He clicks "Upload" and selects the Excel file.
12. The system converts it and shows a preview of the formatted table: product types (TMT Bars 8mm through 32mm), rolling speeds, capacities, annual production figures.
13. The table looks correct. He clicks "Save".

**Selecting equipment items (3 minutes)**

14. Ramesh navigates to the Equipment Selection section. He sees a list of all active catalog items with checkboxes.
15. He checks:
    - 550mm Heavy Duty Roughing Mill (6 pages)
    - 400mm Continuous Intermediate Mill (4 pages)
    - 360mm Continuous Intermediate Mill (4 pages)
    - 320mm Continuous Intermediate Mill (4 pages)
    - 280mm Continuous Finishing Mill (4 pages)
    - Auxiliary Equipment (4 pages)
    - Electricals (2 pages)
    - Automatic Cooling Bed with Twin Channel & Cold Shear (5 pages)
    - Continuous Operating Dividing Shear for TMT Bars (1 page)
    - Bar Finishing, Bundling & Tying Machine (4 pages)
    - TMT System (5 pages)
    - UTM Machine (2 pages)
    - Central Oil Lubrication System (3 pages)
    - Wire Rod Block Mill (4 pages)
16. The system shows: 14 items selected, ~52 pages of equipment content.
17. He clicks "Save".

**Adjusting scope of supply (5-10 minutes)**

18. Ramesh navigates to the Scope of Supply section. The system has auto-populated ~60 rows grouped by equipment category, with default S/C values from the catalog.
19. He scans the table. Most defaults are correct for this project.
20. For the Cooling Bed section (item 8), the customer has their own erection team. Ramesh changes "Erection & Comm." from C to S for rows 8.1 through 8.4. He clicks each cell to toggle.
21. He scrolls through the rest. Satisfied. Clicks "Save".

**Editing terms and conditions (3 minutes)**

22. Ramesh navigates to the Terms & Conditions section. The system shows content pre-filled from the Default Terms master: preferred makes of boughtout items, scope of services, facilities to implement project.
23. He reviews. The high voltage specification needs to change from 30 KV to 33 KV for this project. He edits that line.
24. He clicks "Save".

**Selecting exclusions (2 minutes)**

25. Ramesh navigates to the Exclusions section. He sees checkboxes for all active exclusion templates.
26. He checks all 9 standard exclusions:
    - Shed (Hanger), Cranes, Rails & DSL for Crane
    - HT Side, Transformers, all Cables, Capacitors & Earthing
    - All Civil Work and Mill Foundations...
    - (6 more)
27. No custom exclusions needed. Clicks "Save".

**Saving and returning the next day**

28. It is 5 PM. Ramesh closes the browser. The quotation is saved as draft.
29. The next morning, he logs back in. He sees P480-QTN569-V1 (Draft) in his quotation list. He clicks it and the editor opens exactly where he left off.
30. He reviews everything once more. Decides the introduction needs a small edit for this customer's country.

**Previewing and locking (2 minutes)**

31. Ramesh clicks "Preview PDF". The system renders the complete document:
    - Page 1: Introduction with Steefo letterhead (this is also the cover page — introduction and cover are the same page, as in the existing QTN-569 PDF)
    - Page 2: Technical Parameters
    - Page 3: Basic Data & Media Requirements
    - Page 4: Design Parameters & Production Table
    - Pages 5-56: Equipment sections (14 items, ~52 pages with page number overlay)
    - Pages 57-59: Scope of Supply table (3 pages with ~60 rows)
    - Pages 60-62: Terms & Conditions (3 pages)
    - Page 63: Exclusions
    - Every page shows "Page X of 63" in the header
32. He scrolls through the preview. Everything looks correct. The page numbers are continuous. The equipment PDFs have Steefo's page number overlay.
33. He clicks "Lock Version". The system confirms: "Version V1 locked. PDF generated."

**Downloading and sending**

34. Ramesh clicks "Download PDF". The file downloads as `P480-QTN569-V1.pdf`.
35. He opens his email, attaches the PDF, and sends it to the customer.
36. Back in the system, he clicks "Mark as Sent". The status changes to "Sent".

**Creating a revised version (when customer requests changes)**

37. Two weeks later, the customer replies: they want to swap the 280mm finishing mill for a different configuration and add 2 more stands.
38. Ramesh logs in. He opens P480-QTN569 from the quotation list. He sees V1 marked as "Sent".
39. He clicks "Create New Version". The system creates P480-QTN569-V2 as a draft with all content copied from V1.
40. He opens the editor. He navigates to Equipment Selection.
41. He unchecks "280mm Continuous Finishing Mill (4 stands)" and checks "280mm Continuous Finishing Mill (6 stands)" — a different catalog item for the 6-stand configuration.
42. The Scope of Supply table updates: rows for the 4-stand mill are removed, rows for the 6-stand mill are added with defaults.
43. He adjusts the Technical Parameters to reflect the updated capacity.
44. He previews, locks, downloads, and sends V2. The file name is `P480-QTN569-V2.pdf`.
45. Both V1 and V2 remain downloadable from the version history.

### What success looks like

Ramesh assembles a 63-page technical offer in about 20-30 minutes of active work, spread across two sessions. The system handles page numbering, PDF stitching, and scope table population automatically. When the customer requests a revision, he creates V2 in 10 minutes by swapping items and adjusting a few fields. No copy-paste from Word files. No manual page numbering. No risk of overwriting V1.

---

## Edge Cases and Error Scenarios

**Builder selects an item, then the admin deactivates it**

1. Ramesh has P480-QTN569-V1 in draft with item "Central Oil Lubrication System" selected.
2. Suril deactivates that catalog item (it was replaced by a newer version uploaded as a new item).
3. Ramesh opens his draft. The item is still selected (deactivation does not retroactively remove it from drafts). But the item appears with a visual indicator (e.g., strikethrough or warning) showing it has been deactivated.
4. Ramesh can keep it or uncheck it and select the replacement item.

**Builder tries to lock with missing required fields**

1. Ramesh tries to lock a version without selecting any equipment items.
2. The system shows a validation error: "At least one equipment item must be selected."
3. Ramesh adds items and retries.

**Invalid Excel upload**

1. Ramesh uploads a malformed Excel file for the production table.
2. The system shows an error describing the problem.
3. Ramesh fixes the file locally and re-uploads.

**Duplicate quotation code**

1. Ramesh tries to create a quotation with project code "P480" and QTN code "QTN569", but that combination already exists.
2. The system shows: "A quotation with code P480-QTN569 already exists." Ramesh uses a different code.

**Builder needs a catalog item that does not exist**

1. Ramesh is assembling a quotation and needs a "Wire Rod Coiler" item, but it is not in the catalog.
2. He contacts Suril by phone or WhatsApp (outside the system).
3. Suril uploads the new item to the catalog via Catalog Management.
4. Ramesh refreshes the Equipment Selection tab. The new item appears in the list.
5. He checks it and continues building the quotation.

Note: There is no in-system "Request Item" feature. This is handled through normal communication channels. Volume is too low (a few items per year) to justify a formal request workflow.

**Two builders editing different quotations simultaneously**

1. Ramesh edits P480-QTN569-V1. Suril edits P460-QTN542-V3. No conflict. They work on separate quotation versions.
2. If both try to edit the same version, the last save wins. Volume is too low (1-5 quotations per month, 2-3 users) for this to be a real problem. No concurrent editing support needed for MVP.
