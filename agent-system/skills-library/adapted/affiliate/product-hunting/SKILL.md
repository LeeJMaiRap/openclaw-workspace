---
name: product-hunting
description: Find, compare, and score affiliate product candidates by fit, evidence, offer quality, commission, reviews, risk, and content potential.
source_ideas: custom adapted from market-research, data-analysis, and affiliate workflow patterns
adapted_for: OpenClaw
status: reviewed-paper
verification_level: Paper
domain: affiliate
owner_agent:
  - Product Hunter Agent
---

# product-hunting

## Purpose

Create evidence-labeled affiliate product shortlists and scoring reports for campaign planning. Focus on product fit, offer quality, review signals, commission potential, content potential, claim risk, and approval needs.

## When to Use

Use when Business PM Agent or human needs:

- product/SKU shortlist for an affiliate campaign;
- comparison of available offers/products;
- buying checklist translated into product criteria;
- risk screen before content/campaign planning;
- recommendation of products to route into copy/testing.

## Do Not Use When

- Task is niche/trend/customer research only → Market Research Agent.
- Task is hooks/captions/scripts → Content Copy Agent.
- Task is campaign metric analysis → Performance Analyst Agent.
- User asks to buy/order product without explicit approval.
- User asks for fake personal experience, guaranteed income, or unsupported product claims.
- Product data would require login-gated/private scraping, payment/API usage, or prohibited external action.

## Required Inputs

- Product category or candidate product list.
- Target audience and campaign angle from Business PM / Market Research.
- Platform/marketplace constraints if known.
- Affiliate commission rules if known.
- Source links, screenshots, exports, or approved read-only research scope.
- Evaluation criteria and output path.

If data is missing, continue at Paper level and mark assumptions/unknowns.

## Allowed Sources

Prefer:

1. Provided candidate lists, screenshots, marketplace exports, source links.
2. Project research reports from Market Research Agent.
3. Public marketplace/product pages if read-only access is approved and available.
4. Public review summaries or specs accessible without login.
5. Existing campaign metric/product notes.

Do not bypass login/paywall, modify affiliate links, add to cart, purchase, contact sellers/customers, or use private APIs without approval.

## Workflow

1. **Define product criteria**
   - Translate campaign angle into product requirements.
   - Example criteria: price range, device fit, tripod height, clamp width, stability, portability, reviews, seller reliability, commission, shipping, return risk, content fit.

2. **Collect candidate data**
   - Use provided/approved sources.
   - Capture source path/URL, observed fields, missing fields, and date if available.
   - Keep unknowns as `unknown`; do not invent values.

3. **Screen safety and claim risk**
   - Flag products needing proof before claims.
   - Avoid “best”, “guaranteed”, “professional result”, medical/financial/income claims.
   - Mark counterfeit, low-review, misleading listing, price/voucher uncertainty, shipping/refund, and quality risks.

4. **Score candidates**
   - Score 1-5 for: audience fit, offer attractiveness, evidence strength, review/spec confidence, commission potential, content potential, risk, execution effort.
   - Risk score: 1 = low risk, 5 = high risk.
   - Explain major scoring decisions.

5. **Recommend shortlist**
   - Choose primary/secondary/avoid or `blocked: insufficient data`.
   - State exact evidence level and unknowns.
   - Recommend next handoff: Business PM, Content Copy, Market Research, Performance Analyst, or Human approval.

## Output Format

Use Markdown report:

```markdown
# Product Hunting Report: <category/campaign>

Verification Level: Paper
External Actions: none / <approved read-only research only>

## Decision Needed

## Inputs / Assumptions

## Product Criteria
| Criterion | Why It Matters | Required / Nice-to-have |

## Candidates Reviewed
| Candidate | Source | Price | Commission | Reviews | Key Specs | Unknowns |

## Risk Screen
| Candidate | Risk | Severity | Evidence | Mitigation |

## Scorecard
| Candidate | Audience Fit | Offer | Evidence | Review/Spec Confidence | Commission | Content Potential | Risk | Effort | Recommendation |

## Shortlist

## Claims Allowed / Not Allowed

## Open Questions

## Recommended Handoff
```

## Safety Rules

- Draft/report only.
- Do not purchase/order products.
- Do not add items to cart if platform action changes state.
- Do not post, message, run ads, change affiliate links, use payment/API keys, or contact sellers/customers.
- Do not fake ownership/use/testing.
- Do not claim product is best, safest, most durable, official, authentic, or guaranteed unless evidence supports it.
- Mark price/voucher/stock as time-sensitive and unverified unless live source checked.
- Escalate any product with high compliance, counterfeit, safety, or claim risk.

## Verification

Paper-level PASS requires:

- Report exists in assigned output path.
- Candidate data sources or input files are listed.
- Unknown fields are explicit.
- Scoring and risks are explained.
- External actions remain blocked unless human approved.
- Recommendation is evidence-labeled and does not exceed data.

Do not claim product was tested, purchased, verified authentic, or conversion-ready unless matching evidence exists.

## Handoff

Return Specialist Task Report with:

- files created/changed;
- candidates reviewed;
- evidence level;
- selected shortlist or blocker;
- high-risk claims to avoid;
- recommended next owner: Business PM Agent, Content Copy Agent, Performance Analyst Agent, Market Research Agent, or Human.
