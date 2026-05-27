# Business Handoff Transcript Simulation

Verification Level: Paper

No external actions performed.

---

## 1. Business PM Agent Strategy

Role: campaign strategy, coordination, approval gates.

Strategic question:

```text
Which first affiliate content angle should be tested for budget phone tripod?
```

Recommendation:

```text
Primary: TikTok problem/solution angle around shaky video.
Secondary: Facebook beginner setup guide.
Avoid deal-first angle until voucher/price proof exists.
```

Campaign goal:

- Validate audience pain and click intent.
- Keep campaign small and safe.
- Produce draft copy and metrics plan only.

Content pillars:

1. Shaky video problem.
2. Beginner setup checklist.
3. One-person filming tips.
4. Tripod buying checklist.
5. Before/after framing idea.

2-week roadmap:

| Week | Focus | Draft Outputs | Metric |
|---|---|---|---|
| 1 | validate pain | 3 TikTok hooks + 1 Facebook guide | CTR |
| 2 | iterate | 2 variants from winner + 1 checklist | CTR/CVR/orders |

Handoff to Content Copy Agent:

```text
Create draft hooks/captions/CTAs from pillars.
No posting. No fake experience. Include risk notes.
```

Handoff to Performance Analyst Agent:

```text
Analyze sample metrics. Mark data limitations. Recommend next experiment only.
```

---

## 2. Content Copy Agent Draft

Role: draft copy only.

Hooks:

1. Video bị rung nhìn thiếu chuyên nghiệp? Sửa lỗi này trước khi mua gear đắt.
2. Quay một mình dễ hơn khi điện thoại đứng yên.
3. Setup TikTok cho người mới: điện thoại + ánh sáng gần cửa sổ + tripod.
4. Đừng mua cả đống gear ngay. Sửa lỗi rung video trước.
5. Tripod không làm video tự hay, nhưng giúp khung hình ổn hơn.

Caption draft:

```text
Nếu mới làm TikTok/Reels, anh/chị không cần mua quá nhiều gear ngay. Một tripod điện thoại giá mềm giúp cố định khung hình, quay tutorial/unbox/video nói chuyện một mình dễ hơn, và đỡ phải nhờ người cầm máy.

Lưu ý: kiểm tra chiều cao tripod, kẹp điện thoại, và góc quay cần dùng trước khi đặt.
```

CTA variants:

- Xem giá/voucher hiện tại trên Shopee.
- Lưu lại nếu đang build góc quay nhỏ tại nhà.
- Comment “setup” nếu muốn checklist quay video cho người mới.

Compliance notes:

- Draft only.
- No fake ownership/use claim.
- No guaranteed income/sales claim.
- No “best product” claim without comparison data.
- Human must approve before posting.

Handoff back:

```text
Draft copy ready for human review at Paper level.
```

---

## 3. Performance Analyst Report

Role: metrics analysis only.

Computed metrics:

| content_id | platform | hook_angle | views | clicks | orders | commission_vnd | CTR | CVR | Commission/1k views |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| T1 | TikTok | shaky-video-problem | 1200 | 48 | 3 | 18000 | 4.00% | 6.25% | 15000 |
| T2 | TikTok | cheap-setup | 900 | 27 | 1 | 6000 | 3.00% | 3.70% | 6667 |
| F1 | Facebook | beginner-guide | 600 | 24 | 2 | 12000 | 4.00% | 8.33% | 20000 |
| F2 | Facebook | deal-alert | 500 | 10 | 0 | 0 | 2.00% | 0.00% | 0 |

Formulas:

```text
CTR = clicks / views
CVR = orders / clicks
Commission/1k views = commission_vnd / views * 1000
```

Insights:

- T1 has best total commission and strong CTR.
- F1 has best CVR and commission per 1k views.
- F2 deal-alert underperforms in this small sample.
- Problem/guide angles look better than deal-first in sample.

Limitations:

- Only 4 rows.
- No watch time, spend, refunds, product price, or audience segment.
- Recommendation is weak-confidence, sample-bound.

Recommended next experiments:

1. TikTok before/after shaky video hook.
2. Facebook beginner checklist post.
3. Rewrite cheap-setup with visual cost breakdown.
4. Pause deal-first until stronger offer proof.

---

## 4. Human Approval Gate

External action remains blocked until Doanh approves.

Approval required before:

- posting TikTok/Facebook content;
- messaging/commenting as campaign action;
- running ads;
- changing affiliate links/tracking;
- using API/payment keys;
- claiming personal product use;
- buying product for review.

Status:

```text
PASS: Paper-level strategy/copy/metrics handoff.
BLOCKED: all external actions until human approval.
```
