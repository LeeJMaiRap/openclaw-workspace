# state

Workspace-level runtime state nhỏ, dùng khi state không thuộc riêng project/app nào.

## Quy tắc

- Chỉ lưu snapshot nhỏ, có ích qua nhiều session.
- Không lưu cache lớn, build output, dependency, hoặc secret.
- Nếu state thuộc PM Agent runtime, ưu tiên `ops/state/pm-agent/`.
- Nếu là source of truth project, đặt trong `projects/`.
