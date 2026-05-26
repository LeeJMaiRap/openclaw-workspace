# Shared

Vùng tài nguyên dùng chung giữa systems/projects.

## Cấu trúc

```text
shared/
├── assets/              # ảnh/icon/static assets dùng chung
├── schemas/             # schema dùng chung
├── templates/           # template dùng chung ngoài PM Agent core
└── utilities/           # utility có thể tái sử dụng
```

## Quy tắc

- Chỉ đặt thứ dùng chung thật sự ở đây.
- Template riêng của PM Agent nằm trong `systems/pm-agent/templates/`.
- Script vận hành nằm trong `ops/scripts/`.
- Artifact/runtime output nằm trong `ops/exports/` hoặc `ops/tmp/`.

Hiện folder này là skeleton, sẵn sàng cho phần dùng chung sau này.
