---
name: market-research
description: Research affiliate niches, trends, competitors, customer pain points, keywords, channels, and evidence quality before campaign planning.
source_ideas: awesome-llm-apps deep-research/fact-checker
adapted_for: OpenClaw
status: reviewed-paper
verification_level: Paper
domain: affiliate
owner_agent:
  - Market Research Agent
---

# market-research

## Purpose

Create evidence-labeled affiliate market research for campaign planning: niche context, audience pain points, search/social trends, competitor patterns, content angles, keywords, risks, and open questions.

## When to Use

Use when Business PM Agent or human needs:

- niche or audience research before campaign strategy;
- competitor/content landscape scan;
- customer pain-point synthesis;
- keyword/topic/angle shortlist;
- research assumptions and evidence limits for affiliate decisions.

## Do Not Use When

- Task is product scoring/comparison only → Product Hunter Agent.
- Task is copywriting/scripts/captions → Content Copy Agent.
- Task is metric analysis from campaign data → Performance Analyst Agent.
- External posting, messaging, ads, purchases, API writes, scraping behind login, or paid tool usage would be needed without approval.
- User asks for guaranteed income, fake personal experience, or unsupported product claims.

## Required Inputs

- Campaign/niche goal.
- Target audience and geography if known.
- Product or product category if known.
- Channels to inspect: e.g. TikTok, Facebook, Shopee, Google, YouTube.
- Allowed source types and whether live web lookup is approved/available.
- Output format and decision needed.

If inputs are missing, state assumptions and keep output Paper-level.

## Allowed Sources

Prefer sources available inside task scope:

1. Project files and previous research.
2. Public web pages via approved tools.
3. Public marketplace/category pages.
4. Public social/content examples accessible without login.
5. Provided screenshots, exports, tables, or notes.

Do not bypass paywalls/logins, automate platform writes, harvest private data, or scrape at high volume.

## Workflow

1. **Frame research question**
   - Define niche, audience, geography, platform, and decision to support.
   - Separate facts, inferences, and recommendations.

2. **Collect small evidence set**
   - Use 3-7 relevant sources when live research is available.
   - If web search unavailable, use provided/project sources and mark limitation.
   - Record source title/URL/date or file path.

3. **Extract market signals**
   - Audience pain points.
   - Desired outcomes.
   - Objections/barriers.
   - Repeated phrases/keywords.
   - Competitor/content patterns.
   - Offer/channel constraints.

4. **Synthesize angles**
   - Propose 3-5 content/campaign angles.
   - For each angle include audience, pain point, proof needed, claim risk, and draft-safe positioning.

5. **Score opportunities**
   - Use simple 1-5 scoring for: audience pain, content fit, evidence strength, differentiation, compliance risk, execution effort.
   - Explain scoring briefly.

6. **Produce handoff-ready report**
   - Include assumptions, sources, confidence, risks, and next recommended handoff.
   - Never present weak evidence as certainty.

## Output Format

Use Markdown report:

```markdown
# Market Research Report: <niche/category>

Verification Level: Paper
External Actions: none / <approved read-only research only>

## Research Question

## Inputs / Assumptions

## Sources Checked
| Source | Type | Useful Signal | Limitation |

## Audience Pain Points

## Keywords / Phrases

## Competitor & Content Patterns

## Opportunity Angles
| Angle | Audience | Pain Point | Proof Needed | Risk |

## Opportunity Scorecard
| Opportunity | Pain | Content Fit | Evidence | Differentiation | Compliance Risk | Effort | Recommendation |

## Risks / Compliance Notes

## Open Questions

## Recommended Handoff
```

## Safety Rules

- Draft/report only.
- No posting, messaging, ads, purchases/orders, payment use, API-key use, or affiliate-link changes.
- No fake personal experience.
- No medical, financial, guaranteed income, or exaggerated product claims without strong evidence and human approval.
- Mark rumors, comments, and social anecdotes as weak evidence.
- Attribute source-derived claims.
- Escalate to Business PM/human before external action or high-risk claims.

## Verification

Paper-level PASS requires:

- Report exists in assigned output path.
- Sources or input files are listed.
- Assumptions and limitations are explicit.
- Recommendations are evidence-labeled.
- External actions remain blocked unless human approved.

Do not claim validated market demand unless backed by adequate data and verification policy.

## Handoff

Return Specialist Task Report with:

- files created/changed;
- sources checked;
- confidence level;
- blockers/open questions;
- recommended next owner: Business PM Agent, Product Hunter Agent, Content Copy Agent, or Performance Analyst Agent.
