# Agent Profiles

Phase 1 agent profiles for `agent-system`.

## Profile Structure

Each agent folder contains:

- `AGENT.md` — role, boundaries, inputs, outputs, handoffs.
- `skills.json` — mapped primary/supporting skills.
- `README.md` — short purpose and lifecycle note.

## Phase 1 Agents

### Software Delivery

| Agent | Folder | Primary Skill |
|---|---|---|
| PM Agent | `software/pm-agent/` | `software/project-planning` |
| Product Agent | `software/product-agent/` | `software/product-requirements` |
| Frontend Agent | `software/frontend-agent/` | `software/frontend-react` |
| Backend Agent | `software/backend-agent/` | `software/backend-api` |
| QA Agent | `software/qa-agent/` | `software/qa-verification` |

### Business / Affiliate

| Agent | Folder | Primary Skill |
|---|---|---|
| Content Copy Agent | `business/content-copy-agent/` | `affiliate/content-copywriting` |
| Performance Analyst Agent | `business/performance-analyst-agent/` | `affiliate/performance-analysis` |

## Role Boundary

- PM Agent orchestrates; does not become frontend/backend/QA implementer.
- Product Agent defines what/why; specialist agents define how.
- QA Agent can block acceptance.
- Affiliate agents create drafts/reports only; external actions need approval.

## Validation

Current validation run:

`../tests/2026-05-26-skill-validation/test-report.md`
