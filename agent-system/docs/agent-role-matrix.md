# Agent Role Matrix

## Purpose

Define role ownership for Phase 1 `agent-system` while preserving existing PM Agent in `systems/pm-agent` as canonical source of truth.

## PM Source-of-Truth Rule

Canonical PM Agent:

```text
systems/pm-agent/
```

Adapter profile:

```text
agent-system/agents/software/pm-agent/
```

Meaning:

- PM Agent is not newly created in `agent-system`.
- `agent-system/agents/software/pm-agent` is bridge/adapter only.
- Existing PM Agent workflow, policies, templates, verification levels, and approvals remain authoritative.
- Specialist delegation is proposed extension until explicitly approved.

## Software Team

| Agent/Profile | Source | Owns | Does Not Own | Handoff Rule |
|---|---|---|---|---|
| Existing PM Agent / Lệ | `systems/pm-agent/` | PM lifecycle, scope, approvals, project docs, task board, evidence review, reporting, closure | Specialist implementation ownership; unsupported done/working claims | Canonical workflow and policy source |
| PM Agent Adapter | `agent-system/agents/software/pm-agent/` | bridge from PM Agent core to future specialist handoffs; maps task packet/report requirements | replacing/forking PM Agent; modifying `systems/pm-agent`; activating delegation without approval | uses `specialist-handoff-protocol.md` as adapter-side extension |
| Product Agent | `agent-system/agents/software/product-agent/` | PRD, MVP scope, user stories, acceptance criteria, non-goals, open questions | architecture/code/final implementation decisions | requires Specialist Task Packet + returns Specialist Task Report |
| Architect Agent | `agent-system/agents/software/architect-agent/` | stack, architecture, ADRs, boundaries, integration strategy, technical risks, specialist handoff notes | daily task execution; PM approval decisions; frontend/backend implementation ownership | requires Specialist Task Packet + returns Specialist Task Report |
| Frontend Agent | `agent-system/agents/software/frontend-agent/` | UI, components, client state, forms, frontend verification | backend/database ownership; product scope change | requires Specialist Task Packet + returns Specialist Task Report |
| Backend Agent | `agent-system/agents/software/backend-agent/` | API, service logic, validation, auth boundary, backend verification | UI ownership; product scope change | requires Specialist Task Packet + returns Specialist Task Report |
| QA Agent | `agent-system/agents/software/qa-agent/` | test plan, review, verification, regression risk, PASS/FAIL/BLOCKED | feature scope decisions; silent blocker acceptance | can block acceptance; requires Specialist Task Packet + returns Specialist Task Report |

## Affiliate Team

| Agent/Profile | Source | Owns | Does Not Own | Handoff Rule |
|---|---|---|---|---|
| Business PM Agent | `agent-system/agents/business/business-pm-agent/` | weekly plan, campaign coordination, reporting, approval routing, specialist task packets | posting/ads/payment/API-key use without approval; content execution ownership | requires Specialist Task Packet + returns/collects Specialist Task Report |
| Market Research Agent | `agent-system/agents/business/market-research-agent/` | niche, trend, customer pain, competitor/content notes, keywords, evidence quality | final business decisions; product purchase/scoring ownership; unsupported claims | requires Specialist Task Packet + returns Specialist Task Report |
| Product Hunter Agent | `agent-system/agents/business/product-hunter-agent/` | product shortlist, scoring, risks, offer comparison, claim limits | purchases/orders; payment actions; final campaign decision; fake use/testing/authenticity claims | requires Specialist Task Packet + returns Specialist Task Report |
| Content Copy Agent | `agent-system/agents/business/content-copy-agent/` | hooks, captions, scripts, CTAs, draft copy packs, compliance notes | posting directly; messaging customers; fake claims | requires Specialist Task Packet + returns Specialist Task Report |
| Performance Analyst Agent | `agent-system/agents/business/performance-analyst-agent/` | metrics, experiments, CTR/CVR/commission analysis, next actions | manipulating data; launching campaigns/ads | requires Specialist Task Packet + returns Specialist Task Report |

## Shared Handoff Protocol

Specialist agents must follow:

```text
agent-system/docs/specialist-handoff-protocol.md
agent-system/templates/specialist-task-packet.md
agent-system/templates/specialist-task-report.md
```

Canonical policies inherited from PM Agent:

```text
systems/pm-agent/runtime/policies/verification-level-policy.md
systems/pm-agent/runtime/policies/approval-policy.md
systems/pm-agent/runtime/policies/actor-tracking-policy.md
systems/pm-agent/runtime/policies/acceptance-verification-policy.md
```

## Hard Boundaries

- Do not modify `systems/pm-agent` unless Doanh approves.
- Do not treat PM Adapter as canonical PM Agent.
- Do not revive old specialist-agent branch as active workflow.
- Do not claim `tested`, `working`, `integrated`, `deployed`, or `production-ready` without evidence level match.
- Do not post, message, run ads, use payment/API keys, or take external action without approval.
- QA/Reviewer blockers cannot be bypassed silently.
