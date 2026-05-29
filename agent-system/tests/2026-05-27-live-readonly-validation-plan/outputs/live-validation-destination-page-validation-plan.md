# Live Validation Destination Page Validation Plan

Date: 2026-05-29 UTC
Owner role: Business PM + Product Hunter + Claim Safety
Status: Plan only — no marketplace/affiliate destination validated yet

## Purpose

Validate the exact destination page before creating any channel-specific publish pack.

Current final internal draft is source-specific to:

```text
https://aureday.net/en/product/product-13-996.html
```

But this is a brand/manufacturer-style product page. Before publishing, the system must verify the actual destination page where a user would click/buy/compare.

## Why This Step Matters

The current pipeline has validated:

```text
live read-only evidence → product spec source → safety-reviewed copy → final internal draft
```

But it has not validated:

```text
final click destination → marketplace/seller facts → affiliate link/spec match → channel publish readiness
```

Without destination validation, publish copy can mismatch the actual product page.

## Validation Modes

### Mode A — User-provided URL

Preferred.

Doanh provides exact destination URL, for example:

```text
Amazon / Shopee / Lazada / TikTok Shop / brand checkout / affiliate redirect destination
```

Agent validates only the provided URL publicly, read-only.

### Mode B — Agent-discovered public URL

Allowed only if Doanh explicitly approves discovery.

Agent may use public search/fetch to find accessible destination pages matching the validated product. Agent must stop on bot wall, login, private access, CAPTCHA, or platform restrictions.

### Mode C — Manual screenshot evidence

Use when marketplace pages block automated fetch.

Doanh provides screenshots or copied visible facts from the destination page. Agent records facts as user-provided evidence, not independently verified web evidence.

## Strict Scope

Allowed:

- Public destination page fetch/read.
- Public search result read if discovery approved.
- Public product title/spec/price/rating/review text if visible without login.
- Screenshot/manual fact transcription if user provides it.

Forbidden:

- Login.
- Add to cart.
- Buy/order.
- Message seller.
- Follow/like/comment/share/save.
- Run ads.
- Post content.
- Use payment/API keys.
- Bypass CAPTCHA/bot checks.
- Scrape high-volume or behind auth.
- Claim personal use/testing.

## Stop Conditions

Stop and record blocker if:

- CAPTCHA or `Robot or human?` appears.
- Login required.
- Page asks for personal/payment data.
- Page blocks region/access.
- Product page content cannot be extracted reliably.
- Destination product name/specs conflict materially with current draft.
- Destination is not clearly same/similar product type.

## Data To Collect

| Field | Required? | Notes |
|---|---:|---|
| Destination URL | yes | Exact URL checked. |
| Access timestamp UTC | yes | Date-sensitive. |
| HTTP/fetch status | yes | Include blocker if any. |
| Page title/product name | yes | Exact visible title if possible. |
| Brand/model | if visible | Do not infer. |
| Price | if visible | Date-sensitive; must include timestamp. |
| Voucher/discount | if visible | Date-sensitive; risky; default omit from copy. |
| Stock/availability | if visible | Date-sensitive; default omit from copy. |
| Rating/review count | if visible | Platform signal only, not quality proof. |
| Sales count | if visible | Platform signal only; omit unless clearly visible and dated. |
| Seller/shop info | if visible | Do not claim reliability unless platform states. |
| Height/specs | yes if copy uses specs | Must match or copy must be edited. |
| Clamp/device compatibility | yes if copy uses specs | Watch conflict. |
| Remote included | yes if copy uses remote | Must be visible or remove remote claim. |
| Load capacity | if copy uses it | Must be visible or remove. |
| Folded size/weight/material | if copy uses it | Must be visible or remove. |
| Shipping/return | if visible | Do not overclaim. |
| Mismatch notes | yes | Compare destination vs Aureday source. |

## Spec Match Rules

### Pass

Destination page clearly matches final draft facts:

- Same product or same equivalent product type.
- Height around 50 inch visible if copy says 50 inch.
- Remote included if copy says remote.
- Phone/tablet holder visible if copy says holder.
- Load capacity visible if copy says 1KG.
- No major contradicting specs.

### Pass With Edits

Destination is close but needs copy changes:

- Product title differs but product type same.
- Height differs from 50 inch.
- Remote unclear or not included.
- Load capacity missing.
- Clamp width missing/inconsistent.
- Use cases like livestream/vlogging not visible.

Action: edit copy to only destination-visible facts.

### Fail

Destination conflicts with draft:

- Different product type.
- No remote but copy says remote.
- Not 50 inch but copy says 50 inch.
- Seller/page suggests unavailable or region-blocked and no alternative evidence.
- Bot/login wall prevents useful validation and no manual evidence is supplied.

Action: do not create publish pack.

## Output Artifact Template

When validation is executed, write:

```text
agent-system/tests/2026-05-27-live-readonly-validation-plan/outputs/live-validation-destination-page-source-check.md
```

Required structure:

```markdown
# Live Validation Destination Page Source Check

Date checked: <UTC timestamp>
Mode: A user-provided URL | B agent-discovered URL | C manual screenshot evidence
Status: PASS | PASS WITH EDITS | FAIL | BLOCKED

## Destination URL
<url>

## Access Result
<HTTP status / blocker / manual evidence note>

## Visible Product Identity
<title, brand, model>

## Visible Commercial Facts
- Price:
- Voucher/discount:
- Stock:
- Rating/reviews:
- Sales:
- Seller/shop:

## Visible Specs
- Height:
- Clamp/device fit:
- Remote:
- Load:
- Holder:
- Material:
- Folded size/weight:

## Match Against Current Final Draft
| Draft fact | Destination visible? | Result | Required edit |
|---|---:|---|---|

## Claim Safety Impact
- Allowed claims:
- Claims to remove:
- Claims requiring same-day recheck:

## Verdict
PASS / PASS WITH EDITS / FAIL / BLOCKED

## Next Step
- Create channel-specific publish pack / revise copy / request another URL / stop.
```

## Current Required Input From Business PM

Need one of these:

1. Provide exact destination/affiliate URL to validate.
2. Approve agent-discovered public URL search.
3. Provide screenshot/manual visible facts if destination page blocks fetch.

## Recommended Default

Ask Doanh for exact destination URL first.

If no URL is available, approve agent-discovered public URL search with low source count and public-read-only constraints.

## Readiness

After this plan:

```text
Ready to execute destination-page validation once URL/discovery mode is approved.
```
