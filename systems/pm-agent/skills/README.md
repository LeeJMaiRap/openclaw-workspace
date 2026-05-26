# PM Agent Skills

Bộ skill lõi cho PM Agent, chia thành 4 nhóm chức năng.

## Cấu trúc

- `input-normalization/` — chuẩn hóa đầu vào thô.
- `document-generation/` — sinh tài liệu PM chuẩn.
- `project-operations/` — vận hành và cập nhật dự án.
- `infrastructure/` — hạ tầng và xuất bản.

## Skill boundary / Ranh giới skill

PM Agent skills trong folder này phục vụ PM/core operations:
- intake and clarification;
- document generation;
- task board and project operation updates;
- reporting and export support;
- evidence and acceptance review.

Các mô hình specialist team cũ đã được bỏ khỏi workspace hiện tại để thiết kế lại sau. File này không routing sang branch team/specialist-agent cũ.

## Verification rule

Khi skill tạo kết quả có claim về trạng thái (`tested`, `working`, `integrated`, `production-ready`, v.v.), skill phải tuân theo:

```text
systems/pm-agent/runtime/policies/verification-level-policy.md
```

Tóm tắt:
- `Paper` / `Simulated` chỉ chứng minh artifact hoặc reasoning.
- `Local` cần command/test/log local.
- `Integration` cần evidence nhiều phần hoạt động cùng nhau.
- `Production` cần approval và production/staging evidence phù hợp.
- Thiếu evidence thì mark `Needs Review` hoặc `Blocked`, không nâng lên `Done`.

## Task templates

Dùng các template này cho task broad, technical, risky, hoặc cần evidence rõ:

```text
systems/pm-agent/templates/task-packet-template.md
systems/pm-agent/templates/task-report-template.md
```

## Danh sách skill

Xem từng thư mục con để biết chi tiết.
