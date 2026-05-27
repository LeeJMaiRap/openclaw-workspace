# Software Mini Flow Output

Validated skills:

- product-requirements
- project-planning
- frontend-react
- backend-api
- qa-verification

---

# PRD: Tiny Internal Task Board

## Summary

Small local-first task board for a 1-person team to create, list, update, and filter tasks.

## Problem

A solo user needs lightweight tracking without full project-management overhead.

## Target Users

- One-person builder/operator.
- Internal demo user.

## Goals

- Create tasks quickly.
- Track status and priority.
- Filter work by status.
- Keep MVP simple enough for local demo.

## Non-goals

- No authentication.
- No multi-user collaboration.
- No notifications.
- No cloud sync.
- No external API integration.

## Success Metrics

- User can create task in under 30 seconds.
- User can change status without page reload if implemented client-side.
- All MVP flows pass manual QA checklist.

## Scope

### MVP

- Task fields: `id`, `title`, `description`, `status`, `priority`, `createdAt`, `updatedAt`.
- Status values: `todo`, `doing`, `done`.
- Priority values: `low`, `medium`, `high`.
- Task creation form.
- Task list.
- Status filter.
- Status update action.

### Should Have

- Empty state.
- Form validation.
- Simple responsive layout.

### Later

- Auth.
- Persistence beyond local demo.
- Drag/drop board.
- Search.
- Due dates.

## User Stories

| Story | Priority | Acceptance Criteria |
|---|---|---|
| As a user, I can create task | P0 | Title required; new task appears in list |
| As a user, I can list tasks | P0 | Existing tasks render with title, status, priority |
| As a user, I can update status | P0 | Status changes to todo/doing/done and UI reflects change |
| As a user, I can filter by status | P0 | Selected filter shows matching tasks only |
| As a user, I see validation errors | P1 | Empty title blocks submit and shows error |

## Functional Requirements

- FR1: System stores task records in local in-memory state or local mock data for artifact-only demo.
- FR2: Create task requires non-empty title.
- FR3: Status update only accepts `todo`, `doing`, `done`.
- FR4: Filter can show all tasks or one status.

## Non-functional Requirements

- Type-safe models.
- Simple responsive UI.
- No external package installation in this test.

## UX Notes

- Top area: title + create form.
- Middle: status filter tabs.
- Main: task cards/list.
- Empty state: “No tasks for this filter.”

## Data / API Notes

- For local demo, backend can be mocked.
- API contract still defined below for future implementation.

## Risks and Assumptions

- Persistence unclear; assume local demo only.
- No auth means not production-ready.
- If using API later, need storage decision.

## QA Acceptance Checklist

- [ ] Create valid task.
- [ ] Reject empty title.
- [ ] Change status from todo → doing → done.
- [ ] Filter each status.
- [ ] Empty state visible for no matches.

## Handoff Recommendation

Send to PM Agent for task planning, then Frontend/Backend agents for artifact specs.

---

# Project Plan: Tiny Internal Task Board

## Goal

Create handoff-ready MVP artifacts for local task board.

## Success Criteria

- PRD has MVP/non-goals and acceptance criteria.
- Frontend spec has components, states, and validation.
- Backend spec has endpoints/contracts even if not implemented now.
- QA report marks readiness.

## Constraints / Non-goals

- Planning/design artifacts only.
- No dependency install.
- No production deployment.

## Milestones

| # | Milestone | Target | Owner | Done Criteria |
|---|---|---|---|---|
| 1 | Requirements ready | Same day | Product Agent | PRD complete |
| 2 | Technical specs ready | Same day | Frontend/Backend Agents | UI/API contracts complete |
| 3 | QA review complete | Same day | QA Agent | PASS/FAIL/BLOCKED with evidence |

## Phases and Tasks

| Task | Size/Effort | Owner | Depends On | Done Criteria | Verification |
|---|---|---|---|---|---|
| Draft PRD | S / 2h | Product Agent | - | Requirements and acceptance criteria written | PRD checklist |
| Define frontend components | S / 2h | Frontend Agent | PRD | Component/state spec done | UI spec review |
| Define API contract | S / 2h | Backend Agent | PRD | Endpoint request/response/errors done | API spec review |
| QA artifact review | XS / 1h | QA Agent | Specs | PASS/FAIL/BLOCKED report | QA report |

## Dependency Map

```text
PRD -> Frontend Spec -> QA Review
PRD -> Backend Spec  -> QA Review
```

## Risks and Mitigations

| Risk | Impact | Probability | Mitigation |
|---|---|---|---|
| Persistence expectation unclear | Medium | Medium | Mark local-only demo; ask before implementation |
| Scope creep into full PM app | High | Medium | Keep non-goals explicit |
| API over-design | Medium | Low | Define minimal CRUD/status endpoints only |

## Open Questions

- Should MVP persist tasks after refresh?
- Should UI be list or kanban board?

## Next Actions

- Confirm persistence decision.
- If approved, implement frontend-only local state prototype first.

---

# Frontend Spec: Tiny Internal Task Board

## Files Proposed

```text
app/tasks/page.tsx
components/tasks/TaskForm.tsx
components/tasks/TaskFilters.tsx
components/tasks/TaskList.tsx
components/tasks/TaskCard.tsx
lib/tasks/types.ts
```

## Components

- `TaskForm`: title, description, priority, submit button, validation error.
- `TaskFilters`: all/todo/doing/done tabs.
- `TaskList`: renders filtered list or empty state.
- `TaskCard`: displays title, description, priority, status selector/action.

## UI States

- Empty all tasks.
- Empty filtered result.
- Validation error for missing title.
- Normal list.
- Status update reflected in list.

## Type Model

```ts
type TaskStatus = 'todo' | 'doing' | 'done';
type TaskPriority = 'low' | 'medium' | 'high';

type Task = {
  id: string;
  title: string;
  description?: string;
  status: TaskStatus;
  priority: TaskPriority;
  createdAt: string;
  updatedAt: string;
};
```

## Verification Command

Not run. This test creates artifacts only; no codebase/package exists under test folder.

---

# Backend API Spec: Tiny Internal Task Board

## Endpoint: List Tasks

`GET /api/tasks?status=todo|doing|done`

Response `200`:

```json
{
  "tasks": []
}
```

## Endpoint: Create Task

`POST /api/tasks`

Request:

```json
{
  "title": "Write PRD",
  "description": "Draft MVP requirements",
  "priority": "medium"
}
```

Response `201`:

```json
{
  "task": {
    "id": "task_123",
    "title": "Write PRD",
    "description": "Draft MVP requirements",
    "status": "todo",
    "priority": "medium",
    "createdAt": "2026-05-26T00:00:00.000Z",
    "updatedAt": "2026-05-26T00:00:00.000Z"
  }
}
```

## Endpoint: Update Task Status

`PATCH /api/tasks/:id/status`

Request:

```json
{ "status": "doing" }
```

Response `200`:

```json
{ "task": {} }
```

## Errors

| Status | Code | Meaning |
|---|---|---|
| 400 | VALIDATION_ERROR | Invalid/missing title/status/priority |
| 404 | TASK_NOT_FOUND | Task id not found |
| 500 | INTERNAL_ERROR | Unexpected server failure |

## Auth / Permissions

None for MVP.

## Data / Side Effects

Creates and updates task records. Storage not selected for artifact-only test.

## Tests

- Create valid task.
- Reject empty title.
- List all tasks.
- Filter by status.
- Update status.
- Reject invalid status.

---

# QA / Review Report

## Scope

Reviewed generated artifacts only. No app code exists in test run.

## Critical Issues

None in artifact scope.

## High Priority Issues

1. Persistence decision unresolved.
   - Impact: implementation approach differs between local state, localStorage, DB, or API.
   - Recommendation: choose frontend-only local state for first prototype unless persistence required.

## Medium Priority Issues

1. UI layout not wireframed.
   - Recommendation: add simple wireframe before frontend implementation.

## Test Plan

- PRD completeness check.
- Frontend component/state check.
- Backend contract check.
- Acceptance checklist check.

## Acceptance Status

PASS for planning artifact readiness.

BLOCKED for implementation readiness until persistence decision confirmed.

## Evidence

- Input file: `inputs/software-mini-flow-input.md`
- Output file: `outputs/software-mini-flow.md`
- No install/build/test command run because this validation creates documents only.

## Recommendations

- Add implementation spike later.
- Create agent profiles after this validation if affiliate flow also passes.
