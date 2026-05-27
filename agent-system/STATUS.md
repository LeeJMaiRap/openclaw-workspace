# Agent System Status

Last updated: 2026-05-27 UTC
Baseline commit: `d2fb0de Add agent-system specialist teams and validation flows`

## Overall Status

Paper-level specialist layer ready for internal planning and simulations.

Not production-ready. No live/external validation or campaign execution approved.

## Source-of-Truth Rule

Canonical PM Agent remains:

```text
systems/pm-agent/
```

`agent-system/` is an adapter/specialist layer only.

## Current Health

| Area | Status | Evidence |
|---|---|---|
| Agent profiles | PASS | 11 agents have `AGENT.md`, `README.md`, `skills.json` |
| Skills mappings | PASS | `check-consistency.py` validates skill paths |
| Handoff protocol | PASS | shared packet/report templates exist |
| Validation artifacts | PASS | 9 test folders with reports |
| Consistency check | PASS | failures=0, warnings=0 |
| Rollback point | PASS | baseline commit `d2fb0de` |
| Live validation | NOT STARTED | no live read-only scope approved |
| External execution | BLOCKED | requires Doanh approval |

## Agents

### Software Team

| Agent | Path | Readiness | Notes |
|---|---|---|---|
| PM Agent Adapter | `agents/software/pm-agent/` | adapter-draft | bridges canonical PM to specialist layer |
| Product Agent | `agents/software/product-agent/` | Paper-simulated | requirements/PRD/acceptance |
| Architect Agent | `agents/software/architect-agent/` | Paper-simulated | architecture/ADR/boundaries |
| Frontend Agent | `agents/software/frontend-agent/` | Paper-simulated | UI/client/frontend verification |
| Backend Agent | `agents/software/backend-agent/` | Paper-simulated | API/data/backend verification |
| QA Agent | `agents/software/qa-agent/` | Paper-simulated | review/verification/blockers |

### Business / Affiliate Team

| Agent | Path | Readiness | Notes |
|---|---|---|---|
| Business PM Agent | `agents/business/business-pm-agent/` | Paper-simulated | campaign orchestration/approval gates |
| Market Research Agent | `agents/business/market-research-agent/` | Paper-validated | market/audience/keyword/angle research |
| Product Hunter Agent | `agents/business/product-hunter-agent/` | Paper-validated | product shortlist/scoring/risk screen |
| Content Copy Agent | `agents/business/content-copy-agent/` | Paper-simulated | hooks/captions/CTAs/compliance notes |
| Performance Analyst Agent | `agents/business/performance-analyst-agent/` | Paper-simulated | metrics/experiments/limitations |

## Skills

### Software Skills

| Skill | Path | Status |
|---|---|---|
| project-planning | `skills-library/adapted/software/project-planning/SKILL.md` | adapted |
| product-requirements | `skills-library/adapted/software/product-requirements/SKILL.md` | adapted |
| software-architecture | `skills-library/adapted/software/software-architecture/SKILL.md` | adapted |
| frontend-react | `skills-library/adapted/software/frontend-react/SKILL.md` | adapted |
| backend-api | `skills-library/adapted/software/backend-api/SKILL.md` | adapted |
| qa-verification | `skills-library/adapted/software/qa-verification/SKILL.md` | adapted |

### Affiliate Skills

| Skill | Path | Status |
|---|---|---|
| affiliate-strategy | `skills-library/adapted/affiliate/affiliate-strategy/SKILL.md` | adapted |
| market-research | `skills-library/adapted/affiliate/market-research/SKILL.md` | reviewed-paper |
| product-hunting | `skills-library/adapted/affiliate/product-hunting/SKILL.md` | reviewed-paper |
| content-copywriting | `skills-library/adapted/affiliate/content-copywriting/SKILL.md` | adapted |
| performance-analysis | `skills-library/adapted/affiliate/performance-analysis/SKILL.md` | adapted |
| short-video-script | `skills-library/adapted/affiliate/short-video-script/SKILL.md` | adapted |

## Validation Runs

| Validation | Path | Result |
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

## Tooling

| Tool | Path | Status |
|---|---|---|
| Consistency checker | `tools/check-consistency.py` | PASS |

Run:

```text
python3 agent-system/tools/check-consistency.py
```

Expected current output:

```text
failures: 0
warnings: 0
RESULT: PASS
```

## Key Docs

| Doc | Purpose |
|---|---|
| `INDEX.md` | high-level inventory |
| `STATUS.md` | current dashboard |
| `docs/activation-guide.md` | when/how to activate specialists |
| `docs/specialist-handoff-protocol.md` | controlled handoff protocol |
| `docs/agent-role-matrix.md` | ownership and boundaries |
| `docs/safety-policy.md` | safety constraints |

## Known Limitations

- Paper-level only.
- No live web/marketplace validation.
- No real SKU/product source proof.
- Product Hunter validation used synthetic candidate data.
- No price/voucher/stock/seller reliability/authenticity proof.
- No product testing or purchase.
- No campaign posting/messaging/ads/payment/API/affiliate-link change approved.
- No formal JSON schema file yet.
- No live read-only validation plan yet.

## Current Blockers

| Blocker | Owner | Needed Decision |
|---|---|---|
| Live validation not scoped | Doanh / Business PM | approve allowed read-only sources and constraints |
| External campaign actions blocked | Doanh | approve specific action before any external write |
| Formal schema missing | Agent-system maintainer | create `schemas/agent-skills.schema.json` if needed |
| Current tooling docs uncommitted | Doanh / maintainer | commit current hardening docs/tools when ready |

## Recommended Next Steps

1. Commit current hardening additions:
   - `agent-system/tools/check-consistency.py`
   - `agent-system/reports/2026-05-27-consistency-check-report.md`
   - `agent-system/docs/activation-guide.md`
   - `agent-system/STATUS.md`
   - `memory/2026-05-26.md`
2. Create formal `skills.json` schema.
3. Create live read-only validation plan.
4. If Doanh approves, run live read-only validation without platform writes.
