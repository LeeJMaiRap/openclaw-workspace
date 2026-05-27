# Performance Analysis: Full Affiliate Team Simulation

Verification Level: Paper
External Actions: none
Data Source: sample metrics from `../inputs/full-affiliate-team-input.md`

## Computed Metrics

| content_id | platform | hook_angle | product_candidate | views | clicks | orders | commission_vnd | CTR | CVR | Commission/1k views |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| T1 | TikTok | shaky-video-problem | P2 | 1200 | 48 | 3 | 18000 | 4.00% | 6.25% | 15000 |
| T2 | TikTok | cheap-setup | P1 | 900 | 27 | 1 | 6000 | 3.00% | 3.70% | 6667 |
| F1 | Facebook | beginner-guide | P1 | 600 | 24 | 2 | 12000 | 4.00% | 8.33% | 20000 |
| F2 | Facebook | deal-alert | P4 | 500 | 10 | 0 | 0 | 2.00% | 0.00% | 0 |

## Formulas

```text
CTR = clicks / views
CVR = orders / clicks
Commission/1k views = commission_vnd / views * 1000
```

## Findings

- T1/P2 has best total commission and supports Product Hunter primary shortlist.
- F1/P1 has best CVR and commission per 1k views in sample.
- Deal-alert/P4 underperforms and matches Product Hunter avoid-primary recommendation.
- Problem/guide angles look safer and stronger than deal-first in sample.

## Limitations

- Only 4 rows.
- Synthetic/sample context only.
- No spend, watch time, refunds, date range, audience segment, SKU link, or content creative quality.
- Cannot claim product winner or validated demand.
- Cannot make budget/ad decisions from this data alone.

## Recommended Next Experiments

1. Draft TikTok variant for P2 with shaky-video fix hook.
2. Draft Facebook/checklist variant for P1 or P2.
3. Pause deal-alert/P4 until live offer proof and better product fit exist.
4. If live validation approved, collect marketplace/source proof before external posting.

## Status

PASS: Paper-level metric analysis completed.
BLOCKED: strong performance claims, ad spend, posting, and external execution require approval and stronger evidence.
