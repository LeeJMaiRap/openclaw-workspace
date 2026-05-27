# Live Read-Only Validation Scope

## Objective

Define approved/forbidden live read-only validation boundaries before checking public marketplace/web sources for budget phone tripod affiliate campaign.

## Current Paper-Level Inputs

Market Research validation:

```text
agent-system/tests/2026-05-27-market-research-validation/outputs/market-research-report.md
```

Product Hunter validation:

```text
agent-system/tests/2026-05-27-product-hunter-validation/outputs/product-hunting-report.md
```

Full affiliate simulation:

```text
agent-system/tests/2026-05-27-full-affiliate-team-simulation/test-report.md
```

## Candidate Validation Questions

Market Research Agent:

- Are the core angles visible in public content/search/marketplace language?
- Are there public examples of shaky-video, beginner setup, one-person filming, or desk setup needs?
- What keywords/phrases appear repeatedly?

Product Hunter Agent:

- Do candidate product types exist on public marketplaces?
- What real price range appears?
- What specs are visible: height, clamp, remote, material, load, ring light details?
- What public review/rating/sales signals are visible?
- What risks appear: low reviews, unclear specs, exaggerated listing claims, shipping/refund issues?

Content Copy Agent:

- Which claims are allowed after source check?
- Which claims remain blocked?
- Which copy should avoid price/voucher/live-stock claims?

## Allowed Read-Only Sources

Allowed only after Doanh approves this scope:

- Public marketplace product/search pages accessible without login.
- Public product pages linked by Doanh.
- Public search results/snippets.
- Public review/spec text visible without login.
- Public social/content pages accessible without login and without interaction.
- Existing project files and prior validation artifacts.

## Forbidden Actions

Always forbidden unless separate explicit approval exists:

- Login to marketplace/social accounts.
- Add to cart.
- Buy/order products.
- Message sellers/customers.
- Follow/like/comment/share/save.
- Run ads.
- Post content.
- Change affiliate links/tracking.
- Use payment/API keys.
- Scrape behind login/paywall/private pages.
- High-volume scraping or automation.
- Bypass bot protections.
- Claim personal use/testing/authenticity.
- Claim current price/voucher/stock after time passes without re-check.

## Data Fields To Collect

Market Research evidence:

| Field | Required? | Notes |
|---|---|---|
| Source title | yes | page/search/content title |
| Source URL | yes | public URL only |
| Access date UTC | yes | when checked |
| Source type | yes | marketplace/search/social/article |
| Relevant phrase/keyword | yes | exact observed text when possible |
| Signal | yes | pain point, angle, objection, competitor pattern |
| Limitation | yes | weak source, unclear context, login needed, etc. |

Product Hunter evidence:

| Field | Required? | Notes |
|---|---|---|
| Product/source URL | yes | public URL only |
| Product name | yes | exact visible name |
| Price shown | if visible | mark date-sensitive |
| Rating/review count | if visible | mark unverified platform signal |
| Sales count | if visible | mark unverified platform signal |
| Key specs | if visible | height, clamp, remote, material, ring light |
| Seller/shop signal | if visible | rating/followers/etc. only if public |
| Shipping/refund notes | if visible | do not infer |
| Commission | if visible/provided | otherwise unknown |
| Risk notes | yes | missing specs, exaggerated claims, low reviews |

## Evidence Storage

If approved and executed later, save outputs under:

```text
agent-system/tests/2026-05-27-live-readonly-validation-plan/outputs/live-market-research-evidence.md
agent-system/tests/2026-05-27-live-readonly-validation-plan/outputs/live-product-hunting-evidence.md
agent-system/tests/2026-05-27-live-readonly-validation-plan/outputs/live-readonly-validation-report.md
```

## Stop Conditions

Stop immediately if:

- login required;
- platform action could change state;
- CAPTCHA/bot protection appears;
- source requires payment/private access;
- page asks for personal data;
- evidence conflicts with current claim;
- Product Hunter needs purchase/testing/authenticity proof;
- user asks for posting, messaging, ads, purchase, or API/payment action.

## Approval Needed

Before running live read-only validation, Doanh must approve:

1. allowed source domains/platforms;
2. max number of pages/sources;
3. whether web search/fetch tools may be used;
4. whether product URLs will be provided by Doanh or discovered by agent;
5. exact output folder;
6. no external writes.
