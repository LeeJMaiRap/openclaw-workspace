# Projects

Vùng này là skeleton cho các project do PM Agent quản lý.

Sau cleanup 2026-05-26, project code/artifact cũ đã được đưa khỏi cây chính. Hiện `projects/` chỉ giữ `_index/` để duy trì portfolio view và làm điểm bắt đầu cho project mới.

## Cấu trúc hiện tại

```text
projects/
├── _index/              # Registry và dashboard portfolio
└── README.md
```

## Khi tạo project mới

Dùng cấu trúc chuẩn:

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

## Quy tắc

1. Mỗi project phải có `project.yaml`.
2. Status trong `project.yaml` phải khớp lifecycle path.
3. Approval và decision quan trọng phải được ghi file.
4. Output build/cache/dependency không commit vào project folder.
5. Project đã dừng hoặc chỉ dùng tham chiếu thì không chạy daily report mặc định.

## Index files

- `_index/projects-registry.md` — danh sách project/portfolio snapshot.
- `_index/active-projects.md` — active dashboard.
- `_index/archived-projects.md` — archived dashboard.
- `_index/portfolio-dashboard.md` — portfolio summary.
- `_index/cross-project-risk-view.md` — risk pattern view.

Lưu ý: index hiện là snapshot lịch sử trước cleanup. Khi anh mở project mới, cần cập nhật index theo trạng thái mới.
