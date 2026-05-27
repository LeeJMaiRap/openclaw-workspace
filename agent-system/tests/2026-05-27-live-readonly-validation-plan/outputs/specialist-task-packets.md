# Specialist Task Packets: Live Read-Only Validation Plan

Status: planning only
Verification Level: Read-only evidence review target
External Actions: forbidden

No live research is performed by this file.

---

## 1. Market Research Agent Packet

Objective: after Doanh approval, check limited public read-only sources for market/audience language around budget phone tripod.

Allowed inputs:

```text
agent-system/tests/2026-05-27-live-readonly-validation-plan/inputs/live-readonly-validation-scope.md
agent-system/tests/2026-05-27-market-research-validation/outputs/market-research-report.md
```

Allowed output after approval:

```text
agent-system/tests/2026-05-27-live-readonly-validation-plan/outputs/live-market-research-evidence.md
```

Evidence required:

- public source title/URL;
- access date UTC;
- observed phrase/keyword;
- market signal;
- limitation.

Forbidden:

- login;
- comments/messages/follows/likes/shares;
- scraping private/login-gated pages;
- high-volume crawling;
- validated-demand claims.

Stop if:

- source needs login/payment/private access;
- platform action could change state;
- evidence cannot support requested claim.

---

## 2. Product Hunter Agent Packet

Objective: after Doanh approval, check limited public read-only product/SKU pages for visible specs, price range, review signals, and risks.

Allowed inputs:

```text
agent-system/tests/2026-05-27-live-readonly-validation-plan/inputs/live-readonly-validation-scope.md
agent-system/tests/2026-05-27-product-hunter-validation/outputs/product-hunting-report.md
```

Allowed output after approval:

```text
agent-system/tests/2026-05-27-live-readonly-validation-plan/outputs/live-product-hunting-evidence.md
```

Evidence required:

- product URL;
- product name;
- visible price/rating/review/sales/specs if present;
- unknown fields marked unknown;
- risk notes;
- claim limits.

Forbidden:

- add-to-cart;
- purchase/order;
- seller/customer messaging;
- affiliate link/tracking changes;
- payment/API use;
- authenticity/testing/use claims.

Stop if:

- page requires login;
- product proof requires purchase/testing;
- source asks for personal/payment data;
- evidence creates high-risk claim conflict.

---

## 3. Business PM Review Packet

Objective: review live read-only evidence, preserve limitations, and decide whether to route to Content Copy Agent or ask Doanh for approval.

Allowed output after approval:

```text
agent-system/tests/2026-05-27-live-readonly-validation-plan/outputs/live-readonly-validation-report.md
```

Required decisions:

- primary angle remains valid / changed / blocked;
- product shortlist remains valid / changed / blocked;
- claims allowed / not allowed;
- whether more evidence is needed;
- whether human approval is needed for next step.

Forbidden:

- external execution;
- publishing;
- ads;
- purchase/order;
- unsupported claim upgrade.
