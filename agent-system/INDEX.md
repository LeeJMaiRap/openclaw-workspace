# Agent System Index

Status: Phase 5 hardening snapshot 2026-05-27 UTC.

## Source-of-Truth Rule

Canonical PM Agent remains:

```text
systems/pm-agent/
```

`agent-system/` is an adapter/specialist layer. It does not replace or modify canonical PM Agent workflow.

## Shared Protocol

All specialist handoffs use:

```text
agent-system/docs/specialist-handoff-protocol.md
agent-system/templates/specialist-task-packet.md
agent-system/templates/specialist-task-report.md
```

External actions stay approval-gated.

## Agents

### Software Team

| Agent | Path | Status | Primary Skill |
|---|---|---|---|
| PM Agent Adapter | `agents/software/pm-agent/` | draft adapter | `project-planning` |
| Product Agent | `agents/software/product-agent/` | draft profile | `product-requirements` |
| Architect Agent | `agents/software/architect-agent/` | draft profile | `software-architecture` |
| Frontend Agent | `agents/software/frontend-agent/` | draft profile | `frontend-react` |
| Backend Agent | `agents/software/backend-agent/` | draft profile | `backend-api` |
| QA Agent | `agents/software/qa-agent/` | draft profile | `qa-verification` |

### Business / Affiliate Team

| Agent | Path | Status | Primary Skill |
|---|---|---|---|
| Business PM Agent | `agents/business/business-pm-agent/` | draft profile | `affiliate-strategy` |
| Market Research Agent | `agents/business/market-research-agent/` | validated Paper-level | `market-research` |
| Product Hunter Agent | `agents/business/product-hunter-agent/` | validated Paper-level | `product-hunting` |
| Content Copy Agent | `agents/business/content-copy-agent/` | validated in team simulation | `content-copywriting` |
| Performance Analyst Agent | `agents/business/performance-analyst-agent/` | validated in team simulation | `performance-analysis` |

## Adapted Skills

### Software

| Skill | Path | Notes |
|---|---|---|
| project-planning | `skills-library/adapted/software/project-planning/SKILL.md` | PM/planning support |
| product-requirements | `skills-library/adapted/software/product-requirements/SKILL.md` | PRD/user stories/acceptance |
| software-architecture | `skills-library/adapted/software/software-architecture/SKILL.md` | architecture/ADR/boundaries |
| frontend-react | `skills-library/adapted/software/frontend-react/SKILL.md` | frontend role skill |
| backend-api | `skills-library/adapted/software/backend-api/SKILL.md` | backend/API role skill |
| qa-verification | `skills-library/adapted/software/qa-verification/SKILL.md` | verification/review role skill |

### Affiliate

| Skill | Path | Notes |
|---|---|---|
| affiliate-strategy | `skills-library/adapted/affiliate/affiliate-strategy/SKILL.md` | Business PM strategy |
| market-research | `skills-library/adapted/affiliate/market-research/SKILL.md` | reviewed Paper-level |
| product-hunting | `skills-library/adapted/affiliate/product-hunting/SKILL.md` | reviewed Paper-level |
| content-copywriting | `skills-library/adapted/affiliate/content-copywriting/SKILL.md` | draft copy/captions/hooks |
| performance-analysis | `skills-library/adapted/affiliate/performance-analysis/SKILL.md` | metrics/experiments |
| short-video-script | `skills-library/adapted/affiliate/short-video-script/SKILL.md` | video script support |

## Validation Runs

| Test | Path | Result |
|---|---|---|
| Foundation skill validation | `tests/2026-05-26-skill-validation/` | PASS Paper-level |
| Agent handoff simulation | `tests/2026-05-26-agent-handoff-simulation/` | PASS Paper-level |
| Architecture skill validation | `tests/2026-05-26-architecture-skill-validation/` | PASS Paper-level |
| Architect handoff simulation | `tests/2026-05-26-architect-handoff-simulation/` | PASS Paper-level |
| Affiliate strategy validation | `tests/2026-05-26-affiliate-strategy-validation/` | PASS Paper-level |
| Business handoff simulation | `tests/2026-05-26-business-handoff-simulation/` | PASS Paper-level |
| Market Research validation | `tests/2026-05-27-market-research-validation/` | PASS Paper-level with limitations |
| Product Hunter validation | `tests/2026-05-27-product-hunter-validation/` | PASS Paper-level with limitations |
| Full affiliate team simulation | `tests/2026-05-27-full-affiliate-team-simulation/` | PASS Paper-level with limitations |

## Current Known Limitations

- All business campaign validation remains Paper-level.
- Live web/marketplace/product validation not performed.
- Affiliate product candidates in Product Hunter validation are synthetic.
- No posting, messaging, ads, purchase, payment/API, affiliate-link change, or external write has been approved.
- `agent-system/` remains draft adapter/specialist layer, not production workflow.

## Next Options

1. Commit baseline if Doanh approves.
2. Define live read-only validation scope if moving affiliate campaign beyond Paper level.
3. Continue hardening with automated consistency script/report.
