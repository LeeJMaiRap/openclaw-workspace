# Live Validation Lessons

Date: 2026-05-29 UTC
Scope: Agent-system process guidance
Source case: `agent-system/tests/2026-05-27-live-readonly-validation-plan/`

## Purpose

This document records lessons from the live read-only validation and Shopee manual-evidence case.

The goal is to prevent future validation work from drifting into uncontrolled campaign execution.

Core rule:

```text
A validation case is evidence for improving the agent-system.
It is not a public campaign unless Business PM explicitly switches mode.
```

## Three Work Modes

Every affiliate/business validation task must declare one mode before work continues.

### 1. Validation Mode

Purpose:

- Test the agent-system.
- Validate specialist handoffs.
- Gather evidence.
- Produce internal reports.

Allowed:

- public read-only research;
- user-provided screenshots/manual facts;
- internal drafts marked not for publish;
- safety reviews;
- final test reports.

Not allowed:

- posting;
- buying;
- add to cart;
- seller messages;
- login-required flows;
- social actions;
- publish pack unless explicitly approved as campaign preparation.

Stop condition:

```text
When the test objective is proven, stop and write a final test report.
```

### 2. Campaign Preparation Mode

Purpose:

- Prepare assets for a possible real campaign.
- Still not publishing.

Requires explicit Business PM approval.

Allowed:

- channel-specific draft pack;
- prepublish checklist;
- same-day fact recheck plan;
- risk review;
- final approval packet.

Not allowed:

- posting;
- buying;
- add to cart;
- seller messages;
- claims not checked same day;
- using stale price/rating/stock claims.

Stop condition:

```text
Stop before publish. Wait for exact channel, copy, link, timing, and Business PM approval.
```

### 3. Publish Mode

Purpose:

- External action.
- Public content or user-facing campaign execution.

Requires a separate explicit approval.

Approval must specify:

- platform/channel;
- exact copy;
- link/product;
- media/assets;
- timing;
- who is represented;
- whether the assistant may post or only prepare.

Default:

```text
Publish Mode is OFF.
```

## Mode Labels Required in Future Artifacts

Every future validation artifact should include:

```text
Mode: Validation / Campaign Preparation / Publish
External action: none / planned / approved
Publish status: not for publish / pending approval / approved
Evidence level: direct public fetch / manual evidence / mixed / synthetic
```

Example:

```text
Mode: Validation
External action: none
Publish status: not for publish
Evidence level: manual evidence from user screenshots
```

## Manual Evidence Rules

Use manual evidence when public pages cannot be fetched directly by agent tools or when platform pages are app-rendered, blocked, login-gated, or extraction fails.

Manual evidence is acceptable only if clearly labeled.

### Required fields

Each manual-evidence artifact must record:

- who provided evidence;
- date/time evidence was captured or received;
- source URL if available;
- screenshot list or description;
- fields visible in screenshots;
- fields not visible;
- claims allowed from screenshots;
- claims not allowed;
- whether same-day recheck is required.

### Required wording

Use:

```text
According to user-provided screenshots dated <date>...
```

or in Vietnamese:

```text
Theo ảnh chụp do Doanh cung cấp ngày <ngày>...
```

Do not write:

```text
Agent verified directly on Shopee...
```

unless the agent actually fetched/read the page directly.

## Marketplace Evidence Rules

Marketplace facts are time-sensitive.

Treat these as volatile:

- price;
- discount;
- voucher;
- stock;
- shipping;
- rating;
- review count;
- sold count;
- seller response rate;
- variants;
- platform badges or buyer protection labels.

Rules:

- Use volatile facts in internal reports only unless same-day checked.
- If public copy mentions volatile facts, include date checked.
- If facts are not same-day checked, remove them from public copy.
- Never invent price/rating/stock/sales.

## Claim Safety Rules

Do not convert seller marketing language into agent claims.

If listing says:

```text
chống rung tối đa
ổn định tuyệt đối
cực kỳ đáng giá
hoàn hảo
vững chắc
```

Safer transformation:

```text
listing mô tả có 4 chân đế / đế cao su / remote Bluetooth / xoay 360° / chiều cao 1m80
```

Blocked unless independently proven:

- best / tốt nhất;
- cheapest / rẻ nhất;
- most durable / bền nhất;
- guaranteed stable / ổn định tuyệt đối;
- official/authentic seller / chính hãng;
- trusted shop / shop uy tín;
- personally tested / mình đã test;
- personally used / mình đang dùng;
- compatible with every phone / phù hợp mọi điện thoại;
- guaranteed sales / ra đơn chắc chắn;
- viral guarantee / giúp viral.

## Recommended Future Test Artifact Structure

To avoid too many scattered files, future live validation tests should prefer this shorter structure:

```text
inputs/
  scope.md
outputs/
  01-evidence.md
  02-specialist-reports.md
  03-safety-review.md
  04-final-test-report.md
```

Only create extra files when needed for auditability.

If a case becomes large, add an index:

```text
outputs/README.md
```

The index should explain:

- what each file is;
- which files are final;
- which files are drafts;
- what decision remains.

## Stop Gates

### Stop Gate A: Validation Complete

Trigger:

- original test objective is proven;
- specialist flow has enough evidence;
- safety issues are documented;
- remaining work would mostly prepare real campaign execution.

Action:

```text
Stop validation. Write final test report. Do not create more product/copy artifacts.
```

### Stop Gate B: Marketplace Blocked

Trigger:

- bot wall;
- CAPTCHA;
- login required;
- private/payment page;
- unreadable dynamic page.

Action:

```text
Stop direct fetch. Do not bypass. Use manual evidence mode if user provides screenshots.
```

### Stop Gate C: Publish Boundary

Trigger:

- task starts requiring exact channel copy;
- prepublish checklist;
- same-day price/rating/shipping recheck;
- CTA to buy now;
- posting or scheduling.

Action:

```text
Ask Business PM whether mode changes from Validation to Campaign Preparation or Publish.
```

Default if unclear:

```text
Stay in Validation Mode.
```

## Vietnamese Next-Step Proposal Format

For every future next-step proposal to Doanh, use this structure:

```text
Bước tiếp theo: <tên bước>

Bước đó làm gì:
- ...

Vì sao cần:
- ...

Ảnh hưởng:
- Không sửa code / có sửa file nào / có external action không.

Kết quả mong đợi:
- ...

Chế độ:
- Validation / Campaign Preparation / Publish
```

If the next step approaches campaign execution, add:

```text
Cần anh xác nhận: đây vẫn là kiểm thử hệ thống hay chuyển sang chuẩn bị chiến dịch thật?
```

## Decision Rule: When to Stop a Product Case

Stop a product case when all are true:

- the workflow was tested;
- evidence limits are known;
- claim safety was exercised;
- Business PM decision gate exists;
- further work would mostly refine publish assets.

Then write a final report and move lessons into docs.

Do not keep expanding the product case only because there is another possible artifact to create.

## Lessons from Shopee Case

### What went well

- The system did not bypass blocked pages.
- Amazon was correctly rejected as a weak Vietnam destination.
- Shopee was prioritized after Business PM challenge.
- User-provided screenshots were labeled as manual evidence.
- Copy was rewritten for `TSS PRO 1M80`, not blindly reused from Aureday/Amazon.
- Unsafe claims were blocked.
- Final report re-centered the work on agent-system.

### What should improve

- The assistant should explain high-level purpose before creating another artifact.
- The assistant should stop earlier once validation goal is met.
- Future tests should use fewer output files.
- Manual evidence mode should be declared at top of each artifact.
- Prepublish artifacts should require explicit mode change.

## Final Operating Principle

```text
Build reusable agent-system capability first.
Use product cases as test evidence.
Do not let product cases become uncontrolled campaigns.
```
