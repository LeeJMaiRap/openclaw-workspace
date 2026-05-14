# Work Breakdown Structure: Hệ thống quản lý công việc nội bộ

## Level 1: Hệ thống quản lý công việc nội bộ MVP

### Level 2: Backend Foundation
#### Level 3: Authentication
##### Level 4: TASK-001 - Implement auth module
- **ID:** TASK-001
- **Description:** Tạo đăng nhập/xác thực JWT
- **Estimated effort:** 12h
- **Dependencies:** None
- **Assigned to:** Backend dev
- **Status:** Done
- **Input:** Charter/requirements
- **Output:** Auth endpoints

#### Level 3: Task API
##### Level 4: TASK-002 - Implement task CRUD
- **ID:** TASK-002
- **Description:** Tạo API CRUD cho task
- **Estimated effort:** 20h
- **Dependencies:** TASK-001
- **Assigned to:** Backend dev
- **Status:** In Progress
- **Input:** Requirements/spec
- **Output:** Task API

### Level 2: Frontend Core
#### Level 3: Task UI
##### Level 4: TASK-003 - Build task list UI
- **ID:** TASK-003
- **Description:** Tạo màn hình danh sách task
- **Estimated effort:** 16h
- **Dependencies:** TASK-002
- **Assigned to:** Frontend dev
- **Status:** Blocked
- **Input:** Task API
- **Output:** Task list page

##### Level 4: TASK-004 - Build task form UI
- **ID:** TASK-004
- **Description:** Tạo form create/edit task
- **Estimated effort:** 16h
- **Dependencies:** TASK-003
- **Assigned to:** Frontend dev
- **Status:** Not Started
- **Input:** Task list UI
- **Output:** Task form

### Level 2: Collaboration & Dashboard
#### Level 3: Collaboration
##### Level 4: TASK-005 - Implement comments
- **ID:** TASK-005
- **Description:** Comment trong task
- **Estimated effort:** 12h
- **Dependencies:** TASK-004
- **Assigned to:** Frontend dev
- **Status:** Not Started
- **Input:** Task detail flow
- **Output:** Comment feature

##### Level 4: TASK-006 - Build dashboard summary
- **ID:** TASK-006
- **Description:** Dashboard cơ bản theo trạng thái task
- **Estimated effort:** 10h
- **Dependencies:** TASK-002
- **Assigned to:** Frontend dev
- **Status:** Not Started
- **Input:** Task data
- **Output:** Dashboard summary

## Summary
- **Total tasks:** 6
- **Estimated total time:** 86h
- **Critical path:** TASK-001 → TASK-002 → TASK-003 → TASK-004 → TASK-005
