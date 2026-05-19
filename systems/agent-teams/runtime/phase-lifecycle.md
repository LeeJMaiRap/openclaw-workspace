# Phase Lifecycle

## Purpose

Define the default project flow for Agent-Teams.

## Lifecycle

```text
0. Intake
1. Requirements
2. Architecture
3. API Contract
4. Planning
5. Execution
6. Integration
7. QA / Review
8. Ship / Handoff
9. Retrospective
```

## 0. Intake

Goal: understand user request and project context.

Required output:

- project goal
- known constraints
- unknowns/questions
- initial risks
- proposed next phase

Gate:

- user confirms direction or answers blocking questions

## 1. Requirements

Owner: Product/Requirements Agent.

Required output:

- PRD or requirement brief
- user stories
- acceptance criteria
- non-functional requirements
- out-of-scope list

Gate:

- PM Orchestrator confirms requirements are clear enough to design architecture

## 2. Architecture

Owner: Technical Architecture Agent.

Required output:

- architecture proposal
- stack recommendation
- module boundaries
- data flow
- major tradeoffs
- ADRs if needed

Gate:

- PM Orchestrator confirms architecture is feasible and not overbuilt

## 3. API Contract

Owner: API Contract Agent.

Required output:

- endpoints
- request/response schemas
- error format
- auth/authz rules
- pagination/filter/sort rules if needed
- contract change process

Gate:

- Frontend and Backend can work without guessing each other's shape

## 4. Planning

Owner: PM Orchestrator.

Required output:

- task breakdown
- dependency map
- ownership map
- parallel wave plan if applicable
- verification plan

Gate:

- every task has owner, inputs, acceptance criteria, verification, and owned paths

## 5. Execution

Owners: specialist agents.

Required output per task:

- agent report
- files changed
- verification evidence
- blockers if any

Gate:

- PM Orchestrator accepts only evidence-backed reports

## 6. Integration

Owner: Integration Agent.

Required output:

- integration report
- conflict resolution notes
- full-app verification result
- remaining blockers

Gate:

- system runs as one whole, not just isolated parts

## 7. QA / Review

Owners: QA/Test Agent and optional review agents.

Required output:

- test result
- acceptance checklist
- bug reports
- security/performance/code review findings if used

Gate:

- acceptance criteria verified or blockers documented

## 8. Ship / Handoff

Owners: PM Orchestrator, DevOps/Deployment Agent, Documentation Agent.

Required output:

- release/handoff summary
- setup/deploy instructions
- known issues
- rollback path

Gate:

- user can review, deploy, or continue from documented state

## 9. Retrospective

Owner: PM Orchestrator.

Required output:

- what worked
- what failed
- improvements for Agent-Teams
- memory/docs updates if needed
