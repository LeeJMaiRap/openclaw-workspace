# Delegation Protocol

## Purpose

Define how PM Orchestrator assigns work to specialist agents.

## Required Task Packet

Every delegated task must include:

```md
# Agent Task

## Task ID

## Assigned Agent

## Objective

## Context

## Inputs

## Owned Paths

## Forbidden Paths

## Acceptance Criteria

## Verification Required

## Constraints

## Return Format
```

## Task ID Format

Use short stable IDs:

```text
REQ-001  requirements
ARCH-001 architecture
API-001  API contract
FE-001   frontend
BE-001   backend
QA-001   QA/test
INT-001  integration
SEC-001  security
PERF-001 performance
DOC-001  documentation
CHAL-001 challenge
```

## Owned Paths

Owned paths are write permissions for that task only.

Rules:

- Keep owned paths narrow.
- Do not give whole-repo ownership unless impossible to avoid.
- If multiple agents need same path, sequence tasks instead of parallelizing.

## Forbidden Paths

Forbidden paths are explicit no-edit areas.

Agent must report blocker if forbidden path is needed.

## Acceptance Criteria

Acceptance criteria must be observable.

Bad:

```text
Make UI good.
```

Good:

```text
Product list shows loading, empty, error, and success states on mobile and desktop.
```

## Verification Required

Specify exact verification expected:

- lint/build/test command
- manual route check
- screenshot
- file inspection
- API call result
- report-only review

## Delegation Safety Checklist

Before sending a task, PM Orchestrator checks:

```text
[ ] Objective clear
[ ] Inputs listed
[ ] Owned paths listed
[ ] Forbidden paths listed
[ ] Acceptance criteria testable
[ ] Verification specified
[ ] Parallel conflicts checked
[ ] Return format specified
```
