# PM Agent Workflow

## Tổng thể
```
User request
    ↓
PM Agent analyzes
    ↓
Create charter + requirements
    ↓
Ask clarifying questions
    ↓
Create planning docs (spec/plan/rules/wbs/schedule/risks)
    ↓
Create task-board
    ↓
Execute tasks (loop):
    - Choose task
    - Execute or delegate to worker
    - Review result
    - Update project state
    - Handle issues/risks/changes
    ↓
Close project
    ↓
Create final report + lessons learned
```

## Chi tiết từng giai đoạn

### Giai đoạn 1: Initiation
- **Input:** User request
- **Output:** charter.md, requirements.md
- **Duration:** 1-2 interactions
- **Key activities:**
  - Phân tích yêu cầu
  - Trích xuất thông tin cốt lõi
  - Phát hiện khoảng trống
  - Tạo danh sách câu hỏi làm rõ
  - Tạo charter nháp

### Giai đoạn 2: Planning
- **Input:** Approved charter
- **Output:** spec.md, plan.md, rules.md, wbs.md, schedule.md, risk-register.md
- **Duration:** 1-2 interactions
- **Key activities:**
  - Tạo Spec (xây cái gì)
  - Tạo Plan (triển khai thế nào)
  - Tạo Rules (nguyên tắc làm việc)
  - Phân rã công việc (WBS)
  - Lập lịch trình
  - Xác định rủi ro

### Giai đoạn 3: Execution
- **Input:** Task board
- **Output:** Completed tasks, updated project state
- **Duration:** Multiple interactions
- **Key activities:**
  - Chọn task tiếp theo
  - Quyết định tự làm hay giao worker
  - Thực thi task
  - Review kết quả
  - Cập nhật tài liệu dự án
  - Xử lý blockers

### Giai đoạn 4: Monitoring
- **Input:** Project state
- **Output:** Status dashboard, alerts, reports
- **Duration:** Periodic
- **Key activities:**
  - Kiểm tra tiến độ
  - Theo dõi issue
  - Theo dõi risk
  - Quản lý change
  - Tạo báo cáo định kỳ

### Giai đoạn 5: Closure
- **Input:** All tasks completed
- **Output:** final-report.md, lessons-learned.md
- **Duration:** 1 interaction
- **Key activities:**
  - Kiểm tra deliverables
  - Xác nhận với user
  - Tạo final report
  - Tạo lessons learned
  - Archive tài liệu
  - Đánh dấu đóng dự án

## Chu trình thực thi task

```
Choose Task
    ↓
Self or Worker?
    ↓
Execute
    ↓
Review Output
    ↓
Update Docs
    ↓
Next Action?
    ↓
Done / Rework / Escalate / Continue
```

## Quy tắc ra quyết định

### Khi nào tự làm?
- Task quản trị
- Task tài liệu
- Task phân tích
- Task đánh giá
- Task cập nhật trạng thái

### Khi nào giao worker?
- Task triển khai kỹ thuật
- Task tạo/sửa nhiều file
- Task cần thao tác chuyên biệt
- Task cần ngữ cảnh cục bộ riêng

### Khi nào hỏi user?
- Yêu cầu mơ hồ
- Thay đổi phạm vi lớn
- Có nhiều phương án chiến lược
- Chuẩn bị chốt kết quả cuối
- Có rủi ro cao hoặc hành động nhạy cảm

## Files cần cập nhật sau mỗi execution

1. **task-board.md** - Update task status, % completion
2. **issue-log.md** - Add new issues, update issue status
3. **change-log.md** - Add new changes, update change status
4. **status-dashboard.md** - Update metrics, timeline, risk status
5. **memory/observations/pm-projects.md** - Log project progress, key decisions
