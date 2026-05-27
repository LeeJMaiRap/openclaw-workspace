---
name: affiliate-strategy
description: Use when defining affiliate niche, channel strategy, positioning, content pillars, campaign goals, decision criteria, and safe execution roadmap.
source:
  - https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/awesome_agent_skills/strategy-advisor
  - https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/awesome_agent_skills/decision-helper
  - https://github.com/affaan-m/ECC/tree/main/.agents/skills/market-research
  - https://github.com/affaan-m/ECC/tree/main/.agents/skills/content-engine
license: mixed/unknown; awesome-llm-apps inspected skills report MIT
adapted_for: OpenClaw
status: reviewed
domain: affiliate
owner_agent:
  - Business PM Agent
  - Affiliate Strategy Agent
---

# Affiliate Strategy

## Purpose

Create safe, decision-oriented affiliate strategy: niche choice, channel focus, positioning, content pillars, campaign roadmap, experiment plan, metrics, risks, and human approval gates.

## When to Use

- Starting a new affiliate campaign.
- Choosing niche/channel/product direction.
- Comparing strategic options.
- Turning research/copy/metrics into weekly plan.
- Defining content pillars and testing roadmap.

## Do Not Use When

- Need raw market data collection only; use Market Research Agent.
- Need product shortlist/scoring only; use Product Hunter Agent.
- Need copy drafts only; use Content Copy Agent.
- Need metrics analysis only; use Performance Analyst Agent.
- User asks to post, message, run ads, buy, or use API/payment without explicit approval.

## Required Tools

- read
- write
- edit
- exec
- web_fetch

## Workflow

1. Define strategic question and success criteria.
2. Capture current state, resources, constraints, channels, audience, and time horizon.
3. Generate options: niche/channel/angle/content strategy.
4. Evaluate options with weighted criteria: demand, commission potential, content fit, competition, trust/risk, ease, evidence confidence.
5. Select recommended direction with rationale and caveats.
6. Define positioning and content pillars.
7. Create 1-4 week experiment roadmap.
8. Define metrics: views, CTR, CVR, orders, commission, refund/cancel, content velocity.
9. Add approval gates before external actions.
10. Hand off to Market Research, Product Hunter, Content Copy, or Performance Analyst.

## Decision Matrix Criteria

Default scoring 1-5:

| Criteria | Meaning |
|---|---|
| Audience pain | urgency and clarity of problem |
| Product-market fit | offer matches audience/context |
| Content fit | easy to demonstrate/explain on chosen channel |
| Commission potential | expected payout vs effort |
| Competition | lower score means harder competition |
| Trust/risk | claim/compliance/reputation risk |
| Execution ease | can create content with current resources |
| Evidence confidence | source/data confidence |

## Output Format

```markdown
# Affiliate Strategy Brief: <campaign/niche>

## Strategic Question

## Current State

## Goal

## Constraints / Non-goals

## Audience

## Options
| Option | Pros | Cons | Risk | Notes |

## Decision Matrix
| Criteria | Weight | Option A | Option B | Option C |

## Recommendation

## Positioning

## Content Pillars

## Campaign Roadmap
| Week | Focus | Outputs | Success Metric |

## Experiment Backlog
| Experiment | Hypothesis | Metric | Success Threshold |

## Metrics Plan

## Risks / Compliance Notes

## Approval Gates

## Handoffs
- Market Research Agent:
- Product Hunter Agent:
- Content Copy Agent:
- Performance Analyst Agent:

## Open Questions
```

## Safety

- Draft/strategy only; do not post, message, run ads, purchase, or use API/payment keys.
- Do not make fake personal-experience claims.
- Do not promise income, sales, ranking, approval, or platform performance.
- Mark assumptions and weak evidence clearly.
- Separate fact, inference, and recommendation.
- Require human approval before external action.

## Expected Output

- Strategy brief.
- Option evaluation.
- Roadmap and experiment plan.
- Metrics plan.
- Handoff instructions.
- Approval gates and risk notes.

## Verification

- Paper: strategy artifact review only.
- Local/Integration/Production do not normally apply unless tied to implemented tracking/reporting system.
- Strong business decisions require stronger data; weak sample means recommendation must be cautious.

## Adaptation Notes

- Reviewed first pass from strategy-advisor, decision-helper, market-research, and content-engine concepts.
- Optimized for Shopee/TikTok/Facebook affiliate workflows with strict no-external-action safety.
