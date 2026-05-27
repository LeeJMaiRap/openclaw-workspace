# Specialist Task Packets: Full Affiliate Team Simulation

Verification Level: Paper
Date: 2026-05-27 UTC
Requester: Business PM Agent
External Actions: forbidden

---

## 1. Market Research Agent Packet

Objective: summarize reusable market findings for budget phone tripod campaign from validated Market Research report.

Read:

```text
agent-system/tests/2026-05-27-market-research-validation/outputs/market-research-report.md
```

Write: section in `full-affiliate-team-transcript.md`.

Forbidden:

- live web/marketplace research;
- posting/messaging/ads/payment/API/purchases;
- validated-demand claims.

Evidence required:

- pain points;
- keywords/phrases;
- recommended angles;
- limitations.

Stop conditions:

- live source needed;
- claim exceeds evidence;
- external action requested.

---

## 2. Product Hunter Agent Packet

Objective: summarize product shortlist and claim limits from validated Product Hunter report.

Read:

```text
agent-system/tests/2026-05-27-product-hunter-validation/outputs/product-hunting-report.md
```

Write: section in `full-affiliate-team-transcript.md`.

Forbidden:

- purchases/orders/add-to-cart;
- affiliate link changes;
- seller/customer messaging;
- fake use/testing/authenticity claims;
- live price/voucher/stock claims.

Evidence required:

- shortlist;
- risk notes;
- allowed/not allowed claims;
- limitations.

Stop conditions:

- live validation required;
- high-risk product claim requested;
- external action requested.

---

## 3. Content Copy Agent Packet

Objective: create draft-only copy pack for P2 primary and P1 secondary using safe angles.

Read:

```text
agent-system/tests/2026-05-27-full-affiliate-team-simulation/inputs/full-affiliate-team-input.md
agent-system/tests/2026-05-27-market-research-validation/outputs/market-research-report.md
agent-system/tests/2026-05-27-product-hunter-validation/outputs/product-hunting-report.md
```

Write:

```text
agent-system/tests/2026-05-27-full-affiliate-team-simulation/outputs/content-copy-pack.md
```

Forbidden:

- posting;
- messaging;
- ads;
- fake personal experience/testing;
- best/cheapest/authentic/viral/income claims;
- live deal/voucher claims.

Evidence required:

- hooks;
- captions;
- CTA variants;
- compliance notes;
- test recommendation.

Stop conditions:

- copy requires unsupported product claim;
- external action requested;
- human approval needed.

---

## 4. Performance Analyst Agent Packet

Objective: compute sample metrics and recommend next experiments without overclaiming.

Read:

```text
agent-system/tests/2026-05-27-full-affiliate-team-simulation/inputs/full-affiliate-team-input.md
```

Write:

```text
agent-system/tests/2026-05-27-full-affiliate-team-simulation/outputs/performance-analysis.md
```

Forbidden:

- manipulating data;
- launching campaigns/ads;
- conversion-ready claims;
- external actions.

Evidence required:

- CTR;
- CVR;
- commission per 1k views;
- limitations;
- next experiment recommendation.

Stop conditions:

- data insufficient for requested claim;
- external action requested;
- budget/ad decision needed.
