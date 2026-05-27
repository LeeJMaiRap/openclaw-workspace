# Specialist Handoff Protocol

## Purpose

Define controlled way for PM Agent Adapter to hand work to specialist agents while preserving canonical PM Agent in `systems/pm-agent`.

## Source of Truth

Canonical PM Agent remains:

```text
systems/pm-agent/
```

This protocol is adapter-side only. It does not modify or replace PM Agent core workflow.

## When to Use

Use when PM Agent Adapter needs proposed specialist support from:

- Product Agent
- Frontend Agent
- Backend Agent
- QA Agent
- Market Research Agent
- Product Hunter Agent
- Content Copy Agent
- Performance Analyst Agent

## Required Gate Before Handoff

Before assigning specialist work, PM Adapter must confirm:

1. Task has clear objective.
2. Task belongs to specialist role.
3. Allowed files/folders are explicit.
4. Forbidden actions are explicit.
5. Verification Level is stated.
6. Evidence required is stated.
7. Preflight is required for Local/Integration/Production.
8. Stop conditions are stated.
9. Actor fields are filled using `systems/pm-agent/runtime/policies/actor-tracking-policy.md`.

## Verification Levels

Use canonical policy:

```text
systems/pm-agent/runtime/policies/verification-level-policy.md
```

Do not claim:

```text
tested
working
secure
performant
accessible
integrated
deployed
production-ready
```

unless evidence matches policy.

## Handoff Flow

```text
PM Agent Adapter
  -> creates Specialist Task Packet
  -> specialist executes or drafts output within allowed scope
  -> specialist returns Specialist Task Report
  -> PM Agent Adapter reviews evidence
  -> QA Agent reviews when needed
  -> PM Adapter updates project state or marks blocker
```

## Role Rules

### PM Agent Adapter

- Orchestrates.
- Creates task packet.
- Checks approval/evidence.
- Does not replace specialist output silently.
- Does not modify canonical PM Agent without approval.

### Product Agent

- Owns PRD, MVP scope, user stories, acceptance criteria.
- Does not decide architecture alone.

### Frontend Agent

- Owns UI/components/state/frontend verification.
- Does not change backend contract without agreement.

### Backend Agent

- Owns API/data/validation/auth boundary/backend verification.
- Does not change product scope or UI behavior without agreement.

### QA Agent

- Owns review, verification, PASS/FAIL/BLOCKED.
- Can block acceptance.

### Market Research Agent

- Owns niche, trend, audience pain, competitor/content pattern, keyword, and evidence-quality research.
- Does not own final business decisions, product purchase/scoring, content publishing, or unsupported claims.

### Product Hunter Agent

- Owns product/SKU shortlist, scoring, offer comparison, product risk screen, and claim limits.
- Does not own purchases/orders, payment actions, final campaign decisions, or fake use/testing/authenticity claims.

### Business/Affiliate Agents

- Draft/report only.
- No posting, messaging, ads, payment, API-key use, or external action without human approval.

## Required Artifacts

For each handoff:

```text
specialist-task-packet.md
specialist-task-report.md
```

Project-specific copies should live under project handoff/evidence path when active project exists.

## Stop Conditions

Stop and ask Doanh if:

- scope expands;
- destructive action needed;
- install/download/deploy/cloud/DNS/billing/secret needed;
- external post/message/ads/payment/API write needed;
- Critical/High QA/security blocker exists;
- evidence cannot support requested claim;
- specialist role boundary conflict appears;
- canonical PM Agent source conflicts with adapter plan.

## Acceptance

PM Adapter may accept specialist work only when:

- task report exists;
- evidence matches requested Verification Level or claim is downgraded;
- blockers are resolved or explicitly accepted by human;
- project state can be updated without source-of-truth conflict.
