---
name: daily-project-report-generator
description: Tạo file báo cáo hằng ngày cho một dự án vào cuối ngày hoặc theo lịch định kỳ; dùng khi cần snapshot thay đổi trong ngày, ai đã làm gì (human / agent / subagent), tiến độ, issue/risk chính và next actions. Output mặc định vào `projects/active/[project-name]/reports/daily/YYYY-MM-DD.md`.
---

# Daily Project Report Generator

## Mục tiêu

Tạo báo cáo hằng ngày ngắn gọn nhưng đủ giá trị vận hành để:
- nhìn lại thay đổi của dự án trong ngày
- truy được ai đã thực hiện thay đổi
- tổng hợp task progress / issues / changes
- chuẩn bị handoff cho ngày hôm sau

## Dùng khi nào

Dùng skill này khi:
- cần report định kỳ mỗi ngày (ví dụ 19:00)
- cần daily digest cho owner / PM
- cần snapshot thay đổi dự án theo từng ngày
- cần log hoạt động human / agent / subagent

## Không dùng khi nào

Không dùng skill này khi:
- cần final report khi closure
- cần status dashboard điều hành tổng thể nhiều ngày
- chưa có đủ dữ liệu tối thiểu từ project files

## Input chính

Đọc tối thiểu các nguồn sau nếu có:
- `project.yaml`
- `03-execution/task-board.md`
- `03-execution/change-log.md`
- `03-execution/issue-log.md`
- `04-monitoring/status-dashboard.md`
- `decisions/decision-log.md`
- `approvals/`
- git log trong thư mục project (nếu cần xác định actor)

## Output

Output là file:
`projects/active/[project-name]/reports/daily/YYYY-MM-DD.md`

Format chuẩn xem ở `template-output.md`.

## Nội dung bắt buộc

1. Project info + reporting date
2. Summary ngắn trong ngày
3. Thay đổi trong ngày
4. Actor attribution
5. Task progress snapshot
6. Issues / risks cần chú ý
7. Decisions / approvals mới (nếu có)
8. Next actions cho ngày sau

## Quy tắc quan trọng

### 1. Phân biệt rõ nguồn thay đổi
Dùng các nhãn actor sau khi có thể xác định:
- `human:[name]`
- `agent:main`
- `subagent:[label-or-session]`
- `unknown`

### 2. Không bịa actor
Nếu không xác định chắc chắn ai làm, ghi `unknown` và nêu lý do ngắn.

### 3. Report là snapshot, không thay thế logs chi tiết
Daily report chỉ tóm tắt thông tin quan trọng nhất. Không chép nguyên task board hay change log vào report.

### 4. Luôn có next actions
Ngay cả khi ngày đó ít thay đổi, vẫn phải chốt ngày mai cần làm gì.

### 5. Nếu không có thay đổi đáng kể
Vẫn tạo report, nhưng ghi rõ:
- không có thay đổi lớn
- dự án đang chờ gì / bị chặn gì

## Heuristic gợi ý

Khi tổng hợp, rà theo câu hỏi:
- Hôm nay dự án có tiến lên không?
- Có deliverable nào thay đổi?
- Ai tạo thay đổi đó?
- Có blocker nào mới?
- Có quyết định/approval nào phát sinh?
- Ngày mai phải làm gì ngay?

## Nguồn xác định actor

Ưu tiên theo thứ tự:
1. explicit actor trong project docs
2. decision/change log
3. handoff notes
4. git commit author
5. session knowledge nếu có

## Liên hệ với workflow PM

Skill này thuộc monitoring/operations định kỳ.

Nó thường chạy sau:
- `task-board-builder`
- `change-log-updater`
- `issue-log-updater`
- `status-dashboard-updater`

## Cấu trúc output

- `template-output.md` - mẫu đầu ra
- `examples/` - ví dụ report mẫu
- `scripts/generate_daily_report.py` - script dựng khung report từ project files

## Cách dùng ngắn gọn

1. Xác định project path
2. Xác định ngày report
3. Đọc project files chính
4. Tóm tắt thay đổi trong ngày
5. Gán actor attribution khi có thể
6. Ghi next actions
7. Xuất file vào `reports/daily/`
