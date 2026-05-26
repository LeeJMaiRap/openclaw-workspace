# PM Agent - Hướng dẫn sử dụng

## Giới thiệu

PM Agent (Lệ) là PM framework chạy trên OpenClaw. Vai trò chính: quản lý dự án bằng tài liệu, task board, policy, evidence, và báo cáo.

Sau cleanup 2026-05-26, PM Agent v1 được giữ như **core framework sạch**. Các mô hình team/specialist-agent cũ đã được bỏ khỏi workflow hiện tại để thiết kế lại sau.

## Mục tiêu

PM Agent có khả năng:
- nhận yêu cầu dự án;
- phân tích và chuẩn hóa yêu cầu;
- tạo bộ tài liệu PM;
- chia task và theo dõi task board;
- kiểm tra evidence trước khi nhận task done;
- theo dõi tiến độ, issue, risk, change;
- tạo báo cáo tổng kết và lessons learned.

## Cấu trúc thư mục

```text
systems/pm-agent/
├── architecture/
│   ├── SYSTEM-PROMPT.md
│   ├── WORKFLOW.md
│   ├── STATE-SCHEMA.md
│   └── STORAGE-RULES.md
├── prompts/
├── templates/
│   ├── task-packet-template.md
│   └── task-report-template.md
├── skills/
├── runtime/
│   ├── config/
│   ├── policies/
│   │   └── verification-level-policy.md
│   ├── registries/
│   └── runbooks/
├── eval/
├── reports/
├── scripts/
├── README.md
└── STATUS.md
```

Project source of truth, khi có project active mới, dùng cấu trúc:

```text
projects/active/[project-name]/
├── project.yaml
├── 01-initiation/
├── 02-planning/
├── 03-execution/
├── 04-monitoring/
├── 05-closure/
├── decisions/
├── approvals/
├── handoffs/
└── evidence/
```

## Cách sử dụng

### 1. Khởi động PM Agent
Load hoặc tham chiếu:

```text
systems/pm-agent/architecture/SYSTEM-PROMPT.md
systems/pm-agent/architecture/WORKFLOW.md
```

### 2. Gửi yêu cầu dự án

Ví dụ:

```text
Hãy quản lý dự án: Xây dựng một PM Agent bằng OpenClaw.
```

### 3. PM Agent thực hiện
- Phân tích yêu cầu.
- Tạo charter.
- Hỏi làm rõ nếu cần.
- Lập kế hoạch.
- Tạo task-board.
- Thực thi task trong scope đã duyệt.
- Review evidence theo Verification Level.
- Cập nhật trạng thái.
- Tạo final report.

### 4. Luồng vận hành
1. Initiation.
2. Planning.
3. Execution.
4. Monitoring.
5. Closure.

## Core policies

- `runtime/policies/verification-level-policy.md` — chuẩn evidence và claim.
- `runtime/policies/approval-policy.md` — approval gate.
- `runtime/policies/acceptance-verification-policy.md` — acceptance verification.
- `runtime/policies/project-lifecycle-path-policy.md` — lifecycle path.
- `runtime/policies/stale-project-detection-policy.md` — stale project detection.

## Core templates

- `templates/task-packet-template.md` — chuẩn mô tả task trước khi làm.
- `templates/task-report-template.md` — chuẩn báo cáo kết quả task.
- `templates/*-template.md` — template artifact PM.

## Verification rule ngắn

PM Agent không được claim `tested`, `working`, `deployed`, `secure`, `performant`, `accessible`, `integrated`, hoặc `production-ready` nếu thiếu evidence tương ứng.

Nếu evidence thấp hơn claim, status phải là:

```text
Needs Review / Blocked / Lower Verification Level
```

## Ghi chú vận hành

- Project state phải lưu bằng file.
- Human-in-the-loop dùng cho quyết định quan trọng, rủi ro cao, approval, deploy, cloud/DNS/billing, secret, hoặc destructive action.
- `memory/pm-agent-observations.md` dùng cho observations dài hạn.
- `ops/state/pm-agent/` dùng cho runtime state nhỏ.
- Historical reports trong `systems/pm-agent/reports/` là audit trail; không sửa nếu không có lý do rõ.
