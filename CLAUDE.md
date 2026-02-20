# Project Configuration

## Project Description

<!-- Replace this with a 2-3 sentence description of the project -->
[TODO: Describe the project — what site, facility, or system is being documented? What is the goal of the documentation effort?]

## Domain Glossary

| Term | Definition |
|---|---|
| <!-- Add terms as you encounter them --> | |

## Skill Routing

This project uses 5 documentation skills. Apply them automatically based on the context:

| Context | Skill to Apply | Trigger |
|---|---|---|
| **Any writing or editing task** | `documentation-writer` | Always apply as baseline for all documentation output |
| **Creating/editing observations** | `observation-capture` | Working in `10-observations/` folder or capturing site visit notes |
| **Creating/editing process maps** | `process-mapping` | Working in `20-process-maps/` folder or building flows from observations |
| **Creating/editing solution design** | `solution-design` | Working in `40-solution-design/` folder or extracting requirements |
| **Reviewing documentation** | `documentation-reviewer` | Asked to review, audit, check, or find gaps in docs |

**Layering:** `documentation-writer` is the foundation — apply it always. Then layer the specialized skill on top based on the specific task.

**Example:** When creating a new observation, apply both `documentation-writer` (for writing standards) and `observation-capture` (for observation-specific structure and capture tips).

## Folder Structure

| Folder | Purpose |
|---|---|
| `00-inbox/` | Raw notes, uploads, unprocessed material |
| `10-observations/` | Structured observations from site visits |
| `20-process-maps/` | Process documentation built from observations |
| `30-analysis/` | Analysis documents, findings, comparisons |
| `40-solution-design/` | Requirements, data models, architecture, tech decisions |
| `50-review-logs/` | Review session logs with gaps and questions |

## Team

| Name | Role | Notes |
|---|---|---|
| <!-- Add team members --> | | |

## Project-Specific Rules

<!-- Add any rules that apply only to this project -->
<!-- Examples: -->
<!-- - All observations must be reviewed within 48 hours of capture -->
<!-- - Use metric units only -->
<!-- - Reference SAP transaction codes where applicable -->
