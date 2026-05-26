# OpenClaw Workspace

Workspace gọn sau cleanup lớn ngày 2026-05-26. Mục tiêu hiện tại: giữ khung sườn PM Agent hoạt động tốt, loại bỏ project/app/cache cũ khỏi cây chính.

## Cấu trúc hiện tại

```text
workspace/
├── systems/             # Agent systems; hiện giữ PM Agent là core
├── projects/            # Portfolio index/skeleton, chưa chứa project code active
├── ops/                 # Scripts vận hành, exports, tmp, logs, state
├── shared/              # Assets/templates/schemas/utilities dùng chung
├── memory/              # Daily/operational memory notes
├── state/               # Workspace-level runtime state nhỏ
├── tmp/                 # Scratch tạm, có thể dọn định kỳ
├── AGENTS.md            # Workspace operating guide
├── SOUL.md              # Persona/tone
├── USER.md              # Thông tin người dùng
└── README.md            # File này
```

`.git/` và `.trash/` không thuộc cây vận hành chính. `.trash/cleanup-20260526-013600` đang giữ dữ liệu đã dọn để rollback thủ công nếu cần.

## Quick Navigation

### PM Agent
- Path: `systems/pm-agent/`
- Trạng thái: giữ nguyên, không xoá trong cleanup.
- Bắt đầu đọc:
  1. `systems/pm-agent/README.md`
  2. `systems/pm-agent/STATUS.md`
  3. `systems/pm-agent/architecture/WORKFLOW.md`

### Projects
- Path: `projects/`
- Hiện chỉ giữ `_index/` để làm portfolio skeleton.
- Project folders cũ đã được dọn khỏi cây chính. Khi có project mới, tạo lại theo lifecycle PM Agent.

### Ops
- Path: `ops/`
- Chứa scripts/tooling vận hành và output không thuộc source framework.
- Document/PDF tooling nằm tại `ops/scripts/document/`.
- Voice sample exports nằm tại `ops/exports/voice/samples/`.

### Shared / Memory / State / Tmp
- `shared/`: vùng dùng chung, hiện là skeleton.
- `memory/`: ghi chú continuity.
- `state/`: state nhỏ cấp workspace.
- `tmp/`: scratch tạm; không dùng làm nơi lưu artifact dài hạn.

## Quy tắc vận hành

1. **Không xoá PM Agent**: `systems/pm-agent/**` là core.
2. **Source of truth theo folder**:
   - PM Agent framework: `systems/pm-agent/`
   - Project index/skeleton: `projects/`
   - Runtime/export/tooling: `ops/`
   - Scratch: `tmp/`
3. **Không để output runtime trong `systems/`** trừ khi là artifact framework có chủ đích.
4. **Không commit cache/dependency/build output** như `node_modules/`, `.venv*`, `.next/`, `dist/`, `build/`, `__pycache__/`.
5. **Dọn bằng trash trước khi xoá vĩnh viễn** nếu còn khả năng cần rollback.

## Git Hygiene

- Baseline trước update hệ thống: `300527a`
- Cleanup PM Agent skeleton: `c33a17d`
- Snapshot lớn trước cleanup: `1217b2d`

## Current Cleanup Notes

- Workspace chính đã giảm còn khung gọn.
- File root PDF tooling đã chuyển vào `ops/scripts/document/`.
- Voice output sample đã chuyển vào `ops/exports/voice/samples/`.
- README files đang phản ánh cấu trúc sau dọn dẹp.
