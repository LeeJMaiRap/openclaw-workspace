# Task Board: Hệ thống quản lý công việc nội bộ

## Status Legend
- 🔴 Not Started
- 🟡 In Progress
- 🟢 Done
- ⚫ Blocked
- ⚪ Cancelled

## Backlog (Chưa bắt đầu)
| ID | Task | Assigned | Estimate | Priority | Status |
|----|------|----------|----------|----------|--------|
| TASK-004 | Build task form UI | Frontend dev | 16h | High | 🔴 |
| TASK-005 | Implement comments | Frontend dev | 12h | Medium | 🔴 |
| TASK-006 | Build dashboard summary | Frontend dev | 10h | Medium | 🔴 |

## In Progress (Đang làm)
| ID | Task | Assigned | Estimate | Actual | % Done | Blocker |
|----|------|----------|----------|--------|--------|---------|
| TASK-002 | Implement task CRUD | Backend dev | 20h | 12h | 60% | None |

## Done (Hoàn thành)
| ID | Task | Assigned | Estimate | Actual | Completed Date |
|----|------|----------|----------|--------|-----------------|
| TASK-001 | Implement auth module | Backend dev | 12h | 10h | 2026-05-13 |

## Blocked (Bị chặn)
| ID | Task | Assigned | Blocker | Since | Action |
|----|------|----------|---------|-------|--------|
| TASK-003 | Build task list UI | Frontend dev | API contract chưa chốt hoàn toàn | 2026-05-16 | Chốt response schema cho task list |

## Summary
- **Total tasks:** 6
- **Completed:** 1 (16.7%)
- **In Progress:** 1 (16.7%)
- **Blocked:** 1 (16.7%)
- **Not Started:** 3 (50%)
- **Cancelled:** 0 (0%)
- **On-time %:** 83%
- **Current phase:** Backend Foundation / Frontend handoff

## Next Actions
1. Hoàn thành TASK-002 và chốt API contract
2. Gỡ blocker của TASK-003 ngay sau khi API schema ổn
3. Chỉ mở dashboard sau khi task flow lõi ổn định
