# Agent System Status

Last updated: 2026-05-29 UTC
Baseline commit: `d2fb0de Add agent-system specialist teams and validation flows`
Latest committed workspace snapshot: `7538f39 Commit workspace snapshot`

## Overall Status

Specialist layer ready for internal planning, Paper simulations, and controlled read-only validation.

Not production-ready. Live read-only validation has passed with limitations, but external campaign execution remains unapproved.

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
| Validation artifacts | PASS | 10 test folders with reports |
| Consistency check | PASS | failures=0, warnings=0 |
| Rollback point | PASS | baseline commit `d2fb0de`, latest snapshot `7538f39` |
| Live validation | PASS WITH LIMITATIONS | controlled live read-only validation complete; Shopee case closed as validation case |
| External execution | BLOCKED | requires explicit Doanh/Business PM approval for specific publish/buy/message action |

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
| Live read-only validation plan + Shopee case | `tests/2026-05-27-live-readonly-validation-plan/` | PASS WITH LIMITATIONS |

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
| `docs/live-validation-lessons.md` | lessons and stop gates for live validation vs campaign execution |

## Known Limitations

- Not production-ready.
- Live read-only validation completed, but marketplace access remains limited by bot walls/dynamic pages.
- Shopee evidence in the final case depended on Doanh-provided screenshots/manual facts, not direct agent fetch.
- Marketplace facts such as price/voucher/stock/shipping/rating/review count remain time-sensitive and require same-day recheck before public use.
- No product testing or purchase.
- No campaign posting/messaging/ads/payment/API/affiliate-link change approved.
- External publish mode remains off by default.
- Future tests should use tighter artifact structure to avoid drifting from validation into campaign preparation.

## Current Blockers

| Blocker | Owner | Needed Decision |
|---|---|---|
| External campaign actions blocked | Doanh / Business PM | approve exact channel, copy, link, timing, and action before any external write |
| Shopee direct fetch limited | Doanh / Agent-system maintainer | use manual-evidence mode or improve tooling before relying on marketplace facts |
| Publish boundary control | Agent-system maintainer | keep validation/campaign-prep/publish modes explicit in future workflows |
| Current validation artifacts uncommitted | Doanh / maintainer | decide whether to commit new live-validation outputs and docs |

## Recommended Next Steps

1. Review and commit current live-validation artifacts and docs when Doanh approves.
2. Keep Shopee/tripod case closed as a validation case unless Business PM explicitly switches to campaign preparation.
3. Apply `docs/live-validation-lessons.md` to future validation runs:
   - declare mode: Validation / Campaign Preparation / Publish;
   - label manual evidence;
   - use stop gates;
   - explain next steps in Vietnamese with purpose, reason, impact, and expected result.
4. If continuing system hardening, update templates/checklists so future tests follow the shorter artifact structure.
