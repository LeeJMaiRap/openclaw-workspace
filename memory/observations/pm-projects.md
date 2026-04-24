# PM Projects - Quan sát về các dự án PM Agent

## 2026-04-24 - Khởi tạo dự án PM Agent
- **Owner:** Nguyễn Thành Doanh
- **Bối cảnh:** Bài tập thực tập tại HUECIT
- **Mục tiêu:** Nghiên cứu và xây dựng Project Manager Agent bằng OpenClaw
- **Loại dự án:** Dự án cá nhân, Vibe Code / No Code
- **Kết quả mong muốn:** PM Agent có thể nhận yêu cầu dự án, tạo tài liệu PM, chia task, điều phối thực thi, theo dõi tiến độ, và tạo báo cáo tổng kết

## Kiến trúc đề xuất
- 1 PM Agent chính
- 1 hoặc nhiều Worker Agent
- Project state lưu bằng file
- Human-in-the-loop ở các quyết định quan trọng

## Các artifacts cốt lõi
- charter.md
- requirements.md
- spec.md
- plan.md
- rules.md
- wbs.md
- schedule.md
- risk-register.md
- task-board.md
- issue-log.md
- change-log.md
- status-dashboard.md
- final-report.md
- lessons-learned.md

## Ghi chú
- Mô hình được xây dựng qua 8 phần phân tích
- Dùng OpenClaw làm nền tảng triển khai
- Có thể mở rộng thành skill hoặc SOP trong tương lai
