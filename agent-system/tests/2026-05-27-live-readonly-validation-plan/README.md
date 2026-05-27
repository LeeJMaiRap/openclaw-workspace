# Live Read-Only Validation Plan: 2026-05-27

Purpose: define safe scope for moving affiliate campaign validation beyond Paper level without performing external writes or state-changing marketplace/platform actions.

Status: planning only. No live web/marketplace research performed in this folder.

Target flow after approval:

```text
Business PM Agent
  -> Market Research Agent live read-only source check
  -> Product Hunter Agent live read-only product/SKU check
  -> Content Copy Agent claim-limited copy update
  -> Performance Analyst Agent evidence review if metrics available
  -> Human approval gate
```

Verification Level target: Read-only evidence review, still not production/execution ready.

External writes remain blocked.
