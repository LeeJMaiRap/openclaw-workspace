# Agent System Activation Guide

Status: draft guide
Date: 2026-05-27 UTC

## Purpose

Define when PM Agent / Business PM Agent should activate specialist agents in `agent-system/`, what packet is required, and which approval gates block external or high-risk actions.

## Source-of-Truth Rule

Canonical PM Agent remains:

```text
systems/pm-agent/
```

`agent-system/` is an adapter/specialist layer. It must not replace canonical PM Agent workflow, policies, verification levels, or approvals.

## Required Handoff Artifacts

Before any specialist work starts, create Specialist Task Packet:

```text
agent-system/templates/specialist-task-packet.md
```

After specialist work completes, require Specialist Task Report:

```text
agent-system/templates/specialist-task-report.md
```

Shared protocol:

```text
agent-system/docs/specialist-handoff-protocol.md
```

## Universal Activation Checklist

Activate specialist only when all are true:

- [ ] Task has clear objective.
- [ ] Task belongs to specialist role.
- [ ] Allowed files/folders are explicit.
- [ ] Forbidden actions are explicit.
- [ ] Verification Level is stated.
- [ ] Evidence required is stated.
- [ ] Stop conditions are stated.
- [ ] External actions are approval-gated.
- [ ] PM / Business PM remains orchestrator.

Do not activate if task is ambiguous and could cause external action, broad edits, destructive action, secret use, billing, deployment, or source-of-truth conflict.

## Verification Levels

Default for new specialist flow:

```text
Paper
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
conversion-ready
validated demand
verified authentic
```

unless evidence matches canonical PM Agent verification policy.

## Software Team Activation

### Product Agent

Activate when:

- requirements are unclear;
- PRD/user stories/acceptance criteria needed;
- MVP scope needs separation from non-goals;
- business need must become implementation-ready spec.

Do not activate for:

- architecture decisions alone;
- code implementation;
- QA acceptance.

Handoff output:

- PRD section;
- user stories;
- acceptance criteria;
- open questions;
- non-goals.

### Architect Agent

Activate when:

- system boundaries are unclear;
- stack/ADR decision needed;
- frontend/backend/API/data integration needs design;
- technical risk needs structured review before implementation.

Do not activate for:

- daily code execution;
- final PM approval;
- UI/API implementation ownership.

Handoff output:

- architecture brief;
- ADR;
- system boundaries;
- risks;
- specialist handoff notes.

### Frontend Agent

Activate when:

- UI component, screen, client state, form, or frontend behavior is needed;
- frontend verification evidence is needed.

Do not activate for:

- backend/data ownership;
- API contract changes without agreement;
- product scope changes.

Handoff output:

- frontend plan/spec;
- component notes;
- file changes if approved;
- frontend verification evidence.

### Backend Agent

Activate when:

- API/service/data/auth/validation backend work is needed;
- backend verification evidence is needed.

Do not activate for:

- UI ownership;
- product scope changes;
- frontend behavior decisions alone.

Handoff output:

- API/backend plan/spec;
- contract notes;
- file changes if approved;
- backend verification evidence.

### QA Agent

Activate when:

- review/verification is needed;
- acceptance needs PASS/FAIL/BLOCKED;
- regression/security/accessibility/performance risk needs scan;
- evidence claim needs validation.

Do not activate for:

- feature scope decisions;
- silently accepting blockers.

Handoff output:

- test/review plan;
- PASS/FAIL/BLOCKED result;
- evidence list;
- blocker list.

## Business / Affiliate Team Activation

### Business PM Agent

Activate when:

- affiliate campaign coordination is needed;
- strategy brief, weekly plan, approval gate, or specialist routing is needed;
- multiple business specialists must be coordinated.

Do not activate for:

- posting;
- messaging customers/sellers;
- running ads;
- payment/API usage;
- fake personal experience or guaranteed outcome claims.

Handoff output:

- campaign plan;
- specialist routing;
- approval checklist;
- risk/compliance notes.

### Market Research Agent

Activate when:

- niche/trend/audience/customer pain research is needed;
- competitor/content pattern notes needed;
- keyword/phrase ideas needed;
- evidence quality and market assumptions need labeling.

Do not activate for:

- product/SKU scoring ownership;
- final business decision;
- copywriting execution;
- live read/write actions without approval.

Handoff output:

- market research report;
- pain points;
- keywords/phrases;
- opportunity angles;
- limitations and open questions.

### Product Hunter Agent

Activate when:

- product/SKU candidates need scoring;
- offer/review/spec/commission comparison needed;
- product risks and claim limits needed;
- shortlist needed before copy/testing.

Do not activate for:

- purchases/orders/add-to-cart;
- payment actions;
- final campaign decision;
- fake testing/authenticity/use claims.

Handoff output:

- product hunting report;
- criteria matrix;
- risk screen;
- scorecard;
- shortlist;
- allowed/not-allowed claims.

### Content Copy Agent

Activate when:

- hooks/captions/scripts/CTAs/draft copy pack needed;
- compliance notes for copy needed;
- variants needed for Paper-level campaign test.

Do not activate for:

- posting;
- customer messaging;
- ads;
- fake personal experience;
- unsupported best/cheapest/viral/income claims.

Handoff output:

- copy pack;
- hooks;
- captions;
- CTA variants;
- compliance notes;
- test recommendation.

### Performance Analyst Agent

Activate when:

- campaign metrics table/CSV needs analysis;
- CTR/CVR/commission/test result needs calculation;
- winner/loser hypotheses and next experiments needed.

Do not activate for:

- inventing missing metrics;
- manipulating data;
- launching campaigns/ads;
- strong claims from small samples.

Handoff output:

- performance report;
- formulas;
- metric table;
- limitations;
- experiment backlog;
- recommendation.

## Decision Tree

```text
Need PM orchestration?
  -> PM Agent / Business PM Agent

Software requirement unclear?
  -> Product Agent

Architecture/boundary unclear?
  -> Architect Agent

UI/client work?
  -> Frontend Agent

API/data/backend work?
  -> Backend Agent

Review/verification needed?
  -> QA Agent

Affiliate market/audience context missing?
  -> Market Research Agent

Affiliate product/SKU shortlist needed?
  -> Product Hunter Agent

Affiliate copy needed?
  -> Content Copy Agent

Affiliate metrics available?
  -> Performance Analyst Agent
```

## Approval Gates

Ask Doanh before:

- external posting;
- messaging/commenting as campaign action;
- running ads;
- purchases/orders/add-to-cart;
- payment/API key usage;
- affiliate link/tracking changes;
- deployment/cloud/DNS/billing changes;
- destructive broad edits;
- live read-only validation if scope is unclear or platform state could change;
- claiming personal use/testing/authenticity;
- accepting Critical/High QA/security blocker.

## Stop Conditions

Stop and escalate if:

- scope expands;
- role boundary conflict appears;
- required evidence is missing;
- task needs forbidden action;
- source-of-truth conflict appears with `systems/pm-agent/`;
- Verification Level cannot support requested claim;
- specialist output has unresolved blocker;
- human approval is required but not present.

## Recommended Activation Flow

1. PM / Business PM defines objective and Verification Level.
2. PM / Business PM creates Specialist Task Packet.
3. Specialist produces output within allowed scope.
4. Specialist returns Specialist Task Report.
5. PM / Business PM checks evidence and blockers.
6. QA reviews when acceptance/evidence risk exists.
7. Human approval gate handles external or high-risk action.
8. PM / Business PM updates project state or marks blocker.

## Current Readiness

- Software team: Paper-level simulations complete.
- Business team: full affiliate Paper-level simulation complete.
- Market Research Agent: Paper-validated.
- Product Hunter Agent: Paper-validated.
- Content Copy Agent and Performance Analyst Agent: validated inside business/full-team Paper simulations.
- No live/external validation yet.
