# Issue Log: Hệ thống quản lý công việc nội bộ

## Active Issues (Vấn đề đang mở)

### ISS-001: API contract cho task list chưa ổn định
- **Severity:** Medium
- **Status:** Open
- **Reported by:** Frontend dev
- **Reported date:** 2026-05-16
- **Description:** Frontend chưa thể khóa UI task list vì response schema của task list API còn thay đổi.
- **Impact:** Chặn TASK-003 và có thể kéo chậm frontend core.
- **Root cause:** Chưa chốt contract giữa backend và frontend đủ sớm.
- **Resolution:** Chốt response schema và document ví dụ response.
- **Assigned to:** Backend dev
- **Target resolution:** 2026-05-17

## Resolved Issues (Vấn đề đã giải quyết)

### ISS-002: Lỗi JWT config ban đầu
- **Severity:** Medium
- **Status:** Resolved
- **Reported by:** Backend dev
- **Reported date:** 2026-05-12
- **Resolved by:** Backend dev
- **Resolved date:** 2026-05-13
- **Resolution:** Chuẩn hóa env config và token settings.

## Issue Statistics
- **Total issues:** 2
- **Open:** 1
- **Resolved:** 1
- **Average resolution time:** ~1 ngày
