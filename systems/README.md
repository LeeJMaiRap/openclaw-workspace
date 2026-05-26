# Systems

Vùng chứa các hệ thống agent/framework đang được xây dựng và vận hành.

## Hiện có

### PM Agent

Path: `systems/pm-agent/`

PM Agent là core của workspace hiện tại. Tuyệt đối không xoá folder này trong các đợt cleanup/tái cấu trúc.

PM Agent có khả năng:
- Tiếp nhận và phân tích yêu cầu dự án.
- Tạo bộ tài liệu PM chuẩn.
- Chia task và điều phối thực thi.
- Theo dõi tiến độ, rủi ro, thay đổi.
- Tạo báo cáo và checklist vận hành.

Cấu trúc chính:

```text
systems/pm-agent/
├── README.md
├── STATUS.md
├── architecture/
├── prompts/
├── templates/
├── skills/
├── runtime/
├── eval/
├── reports/
├── scripts/
└── changelog/
```

### Voice IO

Path: `systems/voice/`

Voice IO giữ script STT/TTS nhỏ và README. Runtime output không để trong `systems/voice/output/`; output/sample nên nằm ở `ops/exports/voice/`.

## Quy ước system

Mỗi system nên có:
- `README.md` — giới thiệu và hướng dẫn.
- `STATUS.md` — trạng thái nếu system đủ lớn.
- `architecture/` — thiết kế.
- `runtime/` — vận hành thực tế.
- `eval/` — kiểm chứng chất lượng.

## Ranh giới

- `systems/` chứa framework/source của hệ thống.
- `ops/` chứa tooling vận hành, tmp, exports, logs.
- `projects/` chứa project data do PM Agent quản lý.
- `shared/` chứa tài nguyên dùng chung.
