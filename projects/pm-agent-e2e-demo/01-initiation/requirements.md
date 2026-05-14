# Requirements Document: Hệ thống quản lý công việc nội bộ

## 1. Business Requirements
### BR-001: Quản lý công việc tập trung
- **Mô tả:** Tạo một nền tảng nội bộ để team quản lý task tại một nơi.
- **Lý do:** Giảm rối do dùng chat và file rời.
- **Priority:** High
- **Status:** Approved

### BR-002: Cộng tác nội bộ rõ ràng hơn
- **Mô tả:** Hỗ trợ giao việc, deadline và comment để cộng tác tốt hơn.
- **Lý do:** Team cần theo dõi trách nhiệm và tiến độ rõ ràng.
- **Priority:** High
- **Status:** Approved

## 2. Functional Requirements
### FR-001: Tạo task
- **Mô tả:** Người dùng có thể tạo task mới.
- **Input:** Form tạo task.
- **Process:** Lưu task vào hệ thống.
- **Output:** Task xuất hiện trong danh sách.
- **Acceptance Criteria:**
  - [ ] Có thể nhập title và description
  - [ ] Có thể lưu task thành công
  - [ ] Task hiển thị ngay sau khi tạo

### FR-002: Giao người phụ trách và deadline
- **Mô tả:** Gán owner và deadline cho task.
- **Input:** Chọn user và ngày deadline.
- **Process:** Cập nhật task.
- **Output:** Task hiển thị owner và deadline.
- **Acceptance Criteria:**
  - [ ] Có thể chọn owner
  - [ ] Có thể đặt deadline
  - [ ] Dữ liệu được lưu đúng

### FR-003: Cập nhật trạng thái
- **Mô tả:** Người dùng có thể chuyển trạng thái task.
- **Input:** Thay đổi trạng thái task.
- **Process:** Cập nhật trạng thái.
- **Output:** Task hiển thị trạng thái mới.
- **Acceptance Criteria:**
  - [ ] Có trạng thái Todo/In Progress/Done
  - [ ] Có thể đổi trạng thái
  - [ ] Trạng thái hiển thị rõ

### FR-004: Comment trong task
- **Mô tả:** Người dùng có thể trao đổi trong task.
- **Input:** Nội dung comment.
- **Process:** Lưu comment theo task.
- **Output:** Comment hiển thị trong task.
- **Acceptance Criteria:**
  - [ ] Có thể thêm comment
  - [ ] Comment hiển thị đúng task
  - [ ] Có thời gian và người viết

### FR-005: Dashboard đơn giản
- **Mô tả:** Hiển thị tổng quan số task theo trạng thái.
- **Input:** Dữ liệu task hiện tại.
- **Process:** Tổng hợp theo trạng thái.
- **Output:** Dashboard cơ bản.
- **Acceptance Criteria:**
  - [ ] Hiển thị tổng task
  - [ ] Hiển thị số task theo trạng thái
  - [ ] Dễ đọc trên web nội bộ

## 3. Non-Functional Requirements
### NFR-001: Usability
- **Mô tả:** Hệ thống cần dễ dùng cho team nhỏ.
- **Metric:** Người dùng nội bộ có thể sử dụng mà không cần đào tạo phức tạp.

### NFR-002: Responsive Design
- **Mô tả:** Dùng được trên laptop và mobile browser cơ bản.
- **Metric:** Hiển thị ổn ở mobile 375px và desktop 1024px+.

### NFR-003: Security
- **Mô tả:** Phải có xác thực và phân quyền cơ bản.
- **Metric:** Chỉ người dùng hợp lệ mới truy cập được hệ thống.

## 4. User Stories (nếu dùng Agile)
### US-001: Là thành viên team, tôi muốn tạo task để theo dõi việc cần làm
- **Acceptance Criteria:**
  - [ ] Tạo task được
  - [ ] Thấy task trong danh sách
- **Priority:** High
- **Estimate:** 2h

### US-002: Là quản lý, tôi muốn giao người phụ trách để rõ trách nhiệm
- **Acceptance Criteria:**
  - [ ] Chọn được owner
  - [ ] Lưu được deadline
- **Priority:** High
- **Estimate:** 2h

## 5. Traceability Matrix
| Requirement ID | Type | Priority | Status | Linked Tasks |
|----------------|------|----------|--------|--------------|
| BR-001 | Business | High | Approved | TASK-001, TASK-002 |
| BR-002 | Business | High | Approved | TASK-003, TASK-004 |
| FR-001 | Functional | High | Approved | TASK-001 |
| FR-002 | Functional | High | Approved | TASK-002 |
| FR-003 | Functional | High | Approved | TASK-003 |
| FR-004 | Functional | Medium | Approved | TASK-004 |
| FR-005 | Functional | Medium | Approved | TASK-005 |
