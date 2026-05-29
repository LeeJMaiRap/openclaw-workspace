# Final Test Report: Live Read-Only Validation + Shopee Case

Date: 2026-05-29 UTC
Scope: Agent-system validation, not public campaign execution
Final status: PASS WITH LIMITATIONS

## Executive Summary

This test validates the agent-system direction using a real but controlled affiliate-style product case.

The system did **not** publish content, buy anything, log in, add to cart, message sellers, or bypass bot walls. All work stayed read-only or user-provided evidence based.

Final result:

```text
PASS WITH LIMITATIONS
```

Why:

- The specialist-agent flow worked.
- Evidence was captured in files.
- Risky claims were blocked.
- The system adapted when Amazon was not suitable for Vietnam.
- The system correctly moved to Shopee evidence when Doanh provided screenshots.
- The system did not self-publish.
- The main limitation is that Shopee could not be fetched directly by the agent, so final marketplace evidence depends on Doanh-provided screenshots/manual facts.

## Was this aligned with the original agent-system direction?

Answer:

```text
YES, if treated as a validation case.
NO, if continued as a real affiliate campaign without explicit Business PM approval.
```

The correct framing is:

```text
agent-system is not selling a tripod.
agent-system is using a tripod/Shopee case to validate the specialist workflow.
```

This distinction matters because the original direction was to build a reusable agent-system, not to execute uncontrolled marketing actions.

## Original Agent-System Direction Being Tested

The intended system direction was:

- PM Agent / Business PM acts as orchestrator.
- Specialist agents own specialist tasks.
- Each specialist produces structured artifacts.
- Claims must be backed by evidence.
- External actions require explicit human approval.
- Risky or unsupported claims must be blocked.
- The system should work step-by-step, not jump to publishing.

This test exercised these roles:

| Role | Coverage | Evidence |
|---|---:|---|
| Business PM | Covered in this validation case | Business decision docs and human approval gates |
| Market Research | Covered in this validation case | Live market research evidence |
| Product Hunter | Covered in this validation case | Product/source checks |
| Content Copy | Covered in this validation case | Drafts and final internal copy |
| Claim Safety | Covered in this validation case | Safety review files and blocked phrases |
| Human Approval Gate | Covered in this validation case | No publishing without Doanh approval |

## Timeline of Validation

### 1. Planning-only phase

Initial artifact:

```text
agent-system/tests/2026-05-27-live-readonly-validation-plan/test-report.md
```

Result:

```text
PASS: live read-only validation plan created.
```

This phase only defined safe live-validation rules:

- public web only;
- no login;
- no cart/purchase;
- no messages;
- no social actions;
- no CAPTCHA/bot-wall bypass;
- stop on blocked/private/payment flows.

### 2. Actual live read-only validation

Main artifact:

```text
agent-system/tests/2026-05-27-live-readonly-validation-plan/outputs/live-readonly-validation-report.md
```

Result:

```text
PASS with limits.
```

Validated angles:

- shaky/stable video fix;
- beginner setup checklist / one-person filming;
- extendable floor phone tripod with remote.

Limits:

- marketplace pages were partly blocked;
- Walmart hit bot/human wall;
- Amazon/search extraction was weak at first;
- marketplace price/rating/review/sales were not reliable yet.

### 3. Product/source validation

Aureday and Amazon were checked as public sources.

Important result:

- Aureday was usable as spec evidence.
- Amazon confirmed product identity but was not good as Vietnam destination because product was unavailable.

This was a good system behavior: the system did not force a bad destination.

### 4. Market-fit correction: Shopee over Amazon

Doanh challenged the Amazon direction for Vietnam.

System response was correct:

- acknowledged Shopee is better for Vietnam buyer context;
- stopped treating Amazon as purchase destination;
- moved to Shopee destination validation.

This shows Business PM correction worked.

### 5. Shopee validation

Shopee direct fetch failed, so the system used manual evidence from Doanh screenshots.

Key artifacts:

```text
agent-system/tests/2026-05-27-live-readonly-validation-plan/outputs/live-validation-shopee-destination-validation-plan.md
agent-system/tests/2026-05-27-live-readonly-validation-plan/outputs/live-validation-shopee-destination-source-check.md
agent-system/tests/2026-05-27-live-readonly-validation-plan/outputs/live-validation-shopee-manual-evidence-source-check.md
```

Result:

```text
Shopee evidence usable for internal validation, but not independently fetched by agent.
```

This limitation was clearly labeled, which is correct.

### 6. Shopee-specific content drafting

Key artifacts:

```text
agent-system/tests/2026-05-27-live-readonly-validation-plan/outputs/live-validation-shopee-source-specific-draft.md
agent-system/tests/2026-05-27-live-readonly-validation-plan/outputs/live-validation-shopee-draft-safety-review.md
agent-system/tests/2026-05-27-live-readonly-validation-plan/outputs/live-validation-shopee-final-draft.md
```

Important correction:

- The Shopee product is `TSS PRO 1M80`.
- It is not Aureday.
- It is not Amazon.
- It is not `50 inch`.
- It has no visible `1KG` claim in supplied Shopee evidence.

The system correctly rewrote copy instead of reusing the wrong product claims.

### 7. Business PM decision and prepublish plan

Key artifacts:

```text
agent-system/tests/2026-05-27-live-readonly-validation-plan/outputs/live-validation-shopee-business-pm-decision.md
agent-system/tests/2026-05-27-live-readonly-validation-plan/outputs/live-validation-shopee-prepublish-recheck-plan.md
```

These are valid artifacts, but they also reveal the risk of drifting too far into campaign execution.

The better interpretation is:

```text
These files prove the system knows how to stop at approval gates.
They should not trigger publish work unless Business PM explicitly decides to run a real campaign.
```

## Did the system drift from the original goal?

Answer:

```text
Partially at risk, but not yet harmful.
```

### What stayed aligned

- Work stayed inside test folder.
- No external publish action happened.
- No purchase/cart/login happened.
- Evidence and limitations were documented.
- Claims were safety-reviewed.
- Business PM approval gates were preserved.
- The system adapted from Amazon to Shopee based on market context.

### What created drift risk

- Too many small copy/publish-adjacent artifacts were created.
- The conversation became focused on a single Shopee product.
- The next-step proposals started sounding like campaign execution instead of system validation.
- The user had to ask whether the work was drifting.

### Corrective action

This final report closes the validation loop and re-centers the work on agent-system.

Recommended stance after this report:

```text
Stop deepening the Shopee/tripod case unless Doanh explicitly wants a real campaign.
Use the case as validation evidence for agent-system design.
```

## Agent-System Capabilities Proven

### 1. Safe live-read-only behavior

Proven:

- stopped on bot walls;
- did not bypass restrictions;
- did not log in;
- did not buy/add to cart/message/post.

### 2. Evidence-based product reasoning

Proven:

- separated article/category evidence from product-page evidence;
- separated brand page evidence from marketplace destination evidence;
- rejected unsupported claims.

### 3. Market-context correction

Proven:

- Amazon is not automatically the right destination for Vietnam;
- Shopee was correctly prioritized after Business PM challenge.

### 4. Claim safety

Proven blocked claims:

- `best` / `tốt nhất`;
- `giá rẻ nhất`;
- `chống rung tối đa` as own claim;
- `ổn định tuyệt đối`;
- `shop uy tín/chính hãng`;
- `đã test/mình đang dùng`;
- `phù hợp mọi điện thoại`;
- `tải trọng 1KG` without Shopee evidence.

### 5. Human approval gate

Proven:

- public posting was not performed;
- prepublish state was clearly marked as requiring Business PM/human check;
- final content stayed internal.

## Weaknesses Found

### 1. Next-step framing was unclear

The agent repeatedly proposed the next small artifact without explaining the bigger purpose well enough.

Effect:

- Doanh could not easily see why the next step mattered.
- The work felt like it might be drifting toward content production.

Fix:

- Each next step must state whether it belongs to:
  - system validation;
  - campaign preparation;
  - actual publishing.

### 2. Too many artifacts in one case

Many output files were created for one Shopee case.

Effect:

- Good audit trail.
- But high cognitive load.

Fix:

- Future tests should have a shorter final artifact structure:

```text
01-evidence.md
02-specialist-reports.md
03-safety-review.md
04-final-test-report.md
```

### 3. Shopee direct validation remains weak

Shopee could not be read directly by agent tools.

Effect:

- Manual screenshots are acceptable, but must be labeled.
- Agent cannot fully automate marketplace validation for Shopee without better tooling or user-provided screenshots.

Fix:

- Define a formal `manual-evidence` mode.
- Require screenshot date, source, and fields captured.

### 4. Publish-adjacent flow needs stronger boundary

The system created a prepublish checklist, which is useful, but it can feel like it is moving toward publishing.

Fix:

- Add explicit stop marker:

```text
STOP: validation complete. Do not prepare publish pack unless Business PM explicitly changes mode to campaign execution.
```

## Final Verdict

```text
PASS WITH LIMITATIONS
```

### PASS because

- The agent-system specialist workflow worked end-to-end.
- The system moved beyond Paper-level validation into controlled read-only live validation.
- Evidence was documented.
- Claims were constrained.
- Human approval gates were preserved.
- A real market-context correction happened.

### WITH LIMITATIONS because

- Shopee evidence depended on user screenshots.
- The agent could not directly fetch Shopee content.
- The flow became too artifact-heavy.
- Next-step explanations were not clear enough at the campaign boundary.

## Decision: Stop or Continue?

Recommended decision:

```text
STOP this Shopee case as a validation case.
Do not continue toward publish unless Doanh explicitly asks for real campaign execution.
```

Why:

- The validation goal has been met.
- Further work would mostly become campaign execution, not agent-system validation.
- The better next system step is to improve the agent-system based on lessons learned.

## Recommended Next System Step

Create a short improvement note for the agent-system process:

```text
agent-system/docs/live-validation-lessons.md
```

That file should define:

- how to avoid drifting from validation into campaign execution;
- required labels for manual evidence;
- artifact naming pattern for future tests;
- stronger stop gates before publish-adjacent work;
- better Vietnamese next-step explanation format.

## Vietnamese explanation for next step

Bước tiếp theo nên làm:

```text
Tạo agent-system/docs/live-validation-lessons.md
```

Bước đó làm gì:

- Rút bài học từ case Shopee.
- Ghi quy tắc để các lần kiểm thử sau không bị sa đà vào một sản phẩm.
- Chuẩn hóa khi nào là kiểm thử hệ thống, khi nào là chuẩn bị chiến dịch, khi nào là đăng thật.
- Ghi cách dùng ảnh chụp/manual evidence khi agent không đọc được trang.

Vì sao cần:

- Đây là bước biến bài test thành cải tiến cho agent-system.
- Tránh lặp lại lỗi làm anh khó hiểu bước tiếp theo.
- Giữ đúng định hướng ban đầu: xây hệ thống agent, không chạy lan man một case sản phẩm.

Ảnh hưởng:

- Không sửa code.
- Không đăng bài.
- Không mua hàng.
- Chỉ thêm tài liệu quy trình cho agent-system.

Kết quả mong đợi:

- Agent-system có quy tắc rõ hơn cho live validation.
- Những lần sau nhìn vào là biết đang ở chế độ nào: validation, campaign prep, hay publish.
- Business PM dễ quyết định hơn.
