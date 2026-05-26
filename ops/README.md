# Ops

Vùng vận hành: scripts, state, tmp, exports, logs. Không phải source framework chính.

## Cấu trúc

```text
ops/
├── scripts/
│   ├── document/        # PDF/document utility scripts
│   ├── image/           # Image processing scripts
│   ├── maintenance/     # Cleanup/maintenance scripts
│   └── voice/           # Voice processing scripts nếu cần tách khỏi systems/voice
├── state/
│   ├── cache/
│   ├── pm-agent/
│   └── sessions/
├── tmp/
│   ├── image/
│   ├── pm-agent/
│   └── voice/
├── exports/
│   ├── pm-agent/
│   ├── projects/
│   └── voice/
│       └── samples/
└── logs/
```

## Hiện có

### Document tooling
- `ops/scripts/document/md_to_pdf.js` — Node PDF fallback/tool.
- `ops/scripts/document/md_to_pdf_root_legacy.py` — legacy root Python PDF script được di chuyển khỏi root.
- `ops/scripts/document/package.json` / `package-lock.json` — dependency manifest cho document tooling.

### Voice exports
- `ops/exports/voice/samples/` — audio sample đã tạo trước cleanup.

## Quy tắc

1. `ops/scripts/` chứa tooling vận hành, không phải PM Agent source of truth.
2. `ops/tmp/` có thể xoá định kỳ.
3. `ops/exports/` chứa artifact xuất ra; tránh commit binary lớn trừ khi là sample có chủ đích.
4. `ops/state/` chỉ dùng cho state nhỏ; source of truth vẫn nằm ở `systems/` hoặc `projects/`.
5. Nếu script trở thành phần chính thức của PM Agent, chuyển vào `systems/pm-agent/scripts/` hoặc skill tương ứng.
