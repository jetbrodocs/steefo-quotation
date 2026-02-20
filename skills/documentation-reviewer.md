# Documentation Reviewer

## When to Use

Apply this skill when asked to review, audit, check, or perform a gap analysis on documentation. This covers reviewing individual files, entire folders, or cross-referencing multiple documents for consistency.

## Review Process

Follow these steps in order:

1. **Read the scope.** Understand what you're reviewing — a single file, a folder, or the full project. Confirm with the user if unclear.
2. **Check against criteria.** Run through the completeness, consistency, and depth checks below.
3. **Create a review log.** Use the `review-log.md` template in `templates/`. One review log per review session.
4. **Ask questions.** List every gap as a specific, answerable question. Don't just flag problems — frame them as questions someone can respond to.
5. **Suggest updates.** Where you can fix something without new information (typos, formatting, missing frontmatter), fix it directly and note the change in the review log.

## Completeness Checks

- [ ] All template sections are filled in or have explicit `[TODO]` markers
- [ ] Inputs and outputs are listed for every process step
- [ ] Exception paths are documented, not just the happy path
- [ ] People/roles are named for each activity
- [ ] Timing information is present (duration, frequency, or schedule)
- [ ] Connected processes are referenced (what comes before, what comes after)

## Consistency Checks

- [ ] Terminology matches the project glossary in `CLAUDE.md`
- [ ] The same thing isn't called different names in different files
- [ ] Numbers are consistent across documents (if receiving says "20 pallets/day" and shipping says "15 pallets/day," flag it)
- [ ] Time estimates are consistent (a 30-minute process shouldn't be part of a 20-minute parent process)
- [ ] Role names are consistent (don't mix "operator" and "technician" for the same person)

## Depth Checks

- [ ] The document explains *why*, not just *what* (why is this step done this way?)
- [ ] Business rules are stated explicitly, not implied
- [ ] Workarounds and informal practices are documented
- [ ] Decision criteria are specific ("if weight > 50 lbs" not "if the item is heavy")
- [ ] Edge cases are addressed (what happens when something fails, is missing, or is wrong?)

## Question Quality Rules

Every question in a review log must be:

1. **Specific.** Tied to a file and section. "What units does the scale read in?" not "Tell me more about weighing."
2. **Answerable.** Someone can respond without re-reading the entire document. Include enough context in the question itself.
3. **Non-redundant.** Don't ask for information that's already in the document.
4. **Actionable.** The answer will result in a concrete update to the documentation.

Bad: "Can you clarify the inspection process?"
Good: "In `obs-receiving-inspection.md` > Visual Checks: what specific defects does the operator look for? The current list says 'visible damage' — can you list the top 3-5 defect types?"

## Review Log Format

Each review session produces a review log with this structure:

```yaml
---
title: "Review Log — [Scope Description]"
status: draft
created: YYYY-MM-DD
updated: YYYY-MM-DD
reviewer: [name]
tags: [review]
---
```

### Sections

1. **Scope** — What was reviewed (files, folders, date range)
2. **Summary** — 2-3 sentence overview of documentation state
3. **Gaps Found** — Table: file, section, gap description, severity (high/medium/low)
4. **Questions** — Numbered list of specific questions following the quality rules above
5. **Changes Made** — List of direct fixes applied during review (formatting, typos, missing frontmatter)
