---
name: product-requirements
description: Use when turning product ideas into PRD, user stories, acceptance criteria, MVP scope, constraints, risks, and handoff-ready requirements.
source:
  - https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/awesome_agent_skills/project-planner
license: MIT
adapted_for: OpenClaw
status: reviewed
domain: software
owner_agent:
  - Product Agent
  - PM Agent
---

# Product Requirements

## Purpose

Convert rough product intent into clear, testable requirements that PM, Architecture, Frontend, Backend, and QA agents can use without guessing.

## When to Use

- New product/feature idea needs PRD.
- Scope is unclear or too broad.
- Acceptance criteria, user stories, or MVP boundaries are missing.
- PM needs handoff material before implementation planning.

## Do Not Use When

- Task is already implementation-ready.
- User only needs code review/debugging.
- Business decision depends on missing market/legal/compliance input.

## Required Tools

- read
- write
- edit
- exec
- web_fetch

## Workflow

1. Capture product goal, target user, problem, and desired outcome.
2. Define success criteria and measurable signals.
3. Split MVP, should-have, later/backlog.
4. Write user stories with acceptance criteria.
5. Identify data/API/UI needs without prescribing final implementation too early.
6. List constraints, assumptions, dependencies, risks, and open questions.
7. Add QA-ready acceptance test checklist.
8. Hand off to PM Agent for planning or Architect Agent for design.

## Output Format

```markdown
# PRD: <feature/product>

## Summary

## Problem

## Target Users

## Goals

## Non-goals

## Success Metrics

## Scope
### MVP
### Should Have
### Later

## User Stories
| Story | Priority | Acceptance Criteria |

## Functional Requirements

## Non-functional Requirements

## UX Notes

## Data / API Notes

## Risks and Assumptions

## Open Questions

## QA Acceptance Checklist

## Handoff Recommendation
```

## Safety

- Do not invent business facts; mark assumptions.
- Do not promise revenue, conversion, legal compliance, or platform approval without evidence.
- Preserve role boundaries: PRD defines what/why; Architecture/Frontend/Backend define how.
- Do not perform external posting, messaging, purchases, API writes, or deployments.

## Expected Output

- PRD Markdown.
- Clear MVP scope.
- Testable acceptance criteria.
- Open questions separated from assumptions.

## Verification

- Each MVP requirement has acceptance criteria.
- Non-goals are explicit.
- Handoff target is named.
- Missing decisions are marked, not hidden.
