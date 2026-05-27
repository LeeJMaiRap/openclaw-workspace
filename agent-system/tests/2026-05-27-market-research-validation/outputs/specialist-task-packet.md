# Specialist Task Packet: Market Research Agent

## Metadata

- Requester: Business PM Agent
- Assignee: Market Research Agent
- Date: 2026-05-27 UTC
- Verification Level: Paper
- Source Input: `../inputs/market-research-input.md`

## Objective

Produce Paper-level affiliate market research for a budget phone tripod campaign using only provided/project context.

## Role Boundary

Market Research Agent owns:

- niche/category context;
- audience pain points;
- keywords/phrases;
- competitor/content pattern hypotheses;
- opportunity angles;
- evidence quality and limitations;
- next handoff recommendation.

Market Research Agent does not own:

- final business decision;
- product scoring/purchase decision;
- copywriting execution;
- performance metric claims beyond provided context;
- posting, messaging, ads, purchases, payment/API use, or external platform writes.

## Allowed Files / Folders

Read:

```text
agent-system/tests/2026-05-27-market-research-validation/inputs/market-research-input.md
agent-system/skills-library/adapted/affiliate/market-research/SKILL.md
agent-system/docs/specialist-handoff-protocol.md
```

Write:

```text
agent-system/tests/2026-05-27-market-research-validation/outputs/market-research-report.md
agent-system/tests/2026-05-27-market-research-validation/outputs/specialist-task-report.md
```

## Forbidden Actions

- Do not post content.
- Do not message customers.
- Do not run ads.
- Do not purchase/order products.
- Do not use payment/API keys.
- Do not scrape login-gated/private data.
- Do not claim validated market demand.
- Do not invent live-web sources.
- Do not claim personal product experience.

## Evidence Required

- Created market research report path.
- Report sections matching market-research skill output format.
- Explicit assumptions and limitations.
- Explicit external-action block.

## Preflight

Local/Paper task only. No install, network, deployment, cloud, DNS, billing, or secret access required.

## Stop Conditions

Stop and escalate to Business PM / Doanh if:

- live web research becomes required;
- Product Hunter role is needed for product scoring;
- external action is requested;
- evidence cannot support requested claim;
- source-of-truth conflict appears with PM Agent policy.

## Expected Output

1. `market-research-report.md`
2. `specialist-task-report.md`
3. Clear PASS/BLOCKED status for Paper-level handoff.
