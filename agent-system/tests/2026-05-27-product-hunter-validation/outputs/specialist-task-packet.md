# Specialist Task Packet: Product Hunter Agent

## Metadata

- Requester: Business PM Agent
- Assignee: Product Hunter Agent
- Date: 2026-05-27 UTC
- Verification Level: Paper
- Source Input: `../inputs/product-hunter-input.md`
- Upstream Research: `../../2026-05-27-market-research-validation/outputs/market-research-report.md`

## Objective

Produce Paper-level product hunting report and shortlist recommendation for budget phone tripod campaign using provided synthetic candidate data and upstream Market Research Agent output.

## Role Boundary

Product Hunter Agent owns:

- product criteria;
- candidate comparison;
- offer/review/spec/commission screening;
- product risk screen;
- product scorecard;
- shortlist recommendation;
- claims allowed / not allowed.

Product Hunter Agent does not own:

- final campaign decision;
- market trend validation;
- copywriting execution;
- purchases/orders;
- affiliate link changes;
- posting/messaging/ads;
- fake use/testing/authenticity claims.

## Allowed Files / Folders

Read:

```text
agent-system/tests/2026-05-27-product-hunter-validation/inputs/product-hunter-input.md
agent-system/tests/2026-05-27-market-research-validation/outputs/market-research-report.md
agent-system/skills-library/adapted/affiliate/product-hunting/SKILL.md
agent-system/docs/specialist-handoff-protocol.md
```

Write:

```text
agent-system/tests/2026-05-27-product-hunter-validation/outputs/product-hunting-report.md
agent-system/tests/2026-05-27-product-hunter-validation/outputs/specialist-task-report.md
```

## Forbidden Actions

- Do not purchase/order products.
- Do not add items to cart.
- Do not modify affiliate links/tracking.
- Do not post content.
- Do not message customers/sellers.
- Do not run ads.
- Do not use payment/API keys.
- Do not invent live marketplace facts.
- Do not claim personal use/testing/authenticity.
- Do not claim conversion-ready product selection.

## Evidence Required

- Created product hunting report path.
- Report sections matching product-hunting skill output format.
- Explicit assumptions, unknowns, and limitations.
- Explicit external-action block.

## Preflight

Local/Paper task only. No install, network, deployment, cloud, DNS, billing, or secret access required.

## Stop Conditions

Stop and escalate to Business PM / Doanh if:

- live marketplace validation becomes required;
- purchase/add-to-cart/payment/API action is requested;
- candidate data is insufficient for even Paper-level scoring;
- high-risk compliance/claim issue appears;
- source-of-truth conflict appears with PM Agent policy.

## Expected Output

1. `product-hunting-report.md`
2. `specialist-task-report.md`
3. Clear PASS/BLOCKED status for Paper-level handoff.
