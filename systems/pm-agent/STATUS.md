# PM Agent Status

## Mục đích

File này phân biệt rõ giữa:
1. **PM Agent** — framework/agent quản lý dự án.
2. **Project được PM Agent quản lý** — project data nằm trong `projects/` khi có project active.

Không được trộn lẫn trạng thái framework với trạng thái project.

---

## 1. Trạng thái hiện tại của PM Agent

### Giai đoạn hiện tại

**Framework hardening after workspace cleanup**

### Diễn giải

PM Agent đã đi qua các giai đoạn:
- ✅ Khởi tạo danh tính và vai trò.
- ✅ Thiết kế workflow, prompts, templates.
- ✅ Triển khai framework PM Agent trong workspace.
- ✅ Kiểm chứng bằng dự án thực tế đầu tiên trong giai đoạn trước.
- ✅ Tái cấu trúc workspace và chuẩn hóa runtime nền.
- ✅ Bổ sung governance layers: actor tracking / acceptance verification / stale detection / rollback-recovery.
- ✅ Bổ sung reporting layers: framework vs project reporting, source conflict detection, portfolio dashboards.
- ✅ Cleanup workspace lớn ngày 2026-05-26, giữ PM Agent core.
- ✅ Loại bỏ branch team/specialist-agent cũ khỏi active PM Agent workflow để thiết kế lại sau.
- 🟡 Đang hardening framework core: verification levels, task packet/report templates, state/memory path.

### Tiến độ PM Agent

| Hạng mục | Trạng thái |
|---|---|
| Identity / bootstrap | ✅ Hoàn thành |
| Workflow PM Agent core | ✅ Hoàn thành, đang hardening |
| Prompt framework | ✅ Hoàn thành, đang hardening |
| Template framework | ✅ Hoàn thành, mở rộng task/report templates |
| Runtime foundation | ✅ Hoàn thành mức nền |
| Governance layers | ✅ Hoàn thành mức nền |
| Verification Level policy | ✅ Đã thêm |
| Reporting foundation | ✅ Hoàn thành mức nền |
| Portfolio/project skeleton | ✅ Đã chuẩn hóa sau cleanup |
| Old team/specialist-agent branch | 🛑 Removed from active workflow |
| Rebuilt team/delegation system | ⏳ Future design |
| Production-grade PM Agent | ⏳ Chưa hoàn thành |

### Đánh giá tiến độ tổng thể PM Agent

- **Framework core readiness:** ~85-90%.
- **Controlled pilot readiness:** ~80-85%.
- **Production-grade readiness:** chưa hoàn tất.

### Kết luận ngắn

PM Agent hiện là framework core đủ tốt cho pilot/internal use có kiểm soát. Branch team/specialist-agent cũ không còn là một phần của active workflow; hệ team/delegation sẽ được thiết kế lại sau.

---

## 2. Trạng thái project do PM Agent quản lý

Sau cleanup 2026-05-26, workspace chính hiện không có active project folder trong `projects/active/`.

Project cũ chỉ còn dưới dạng historical report/audit trail hoặc có thể phục hồi từ rollback/trash nếu cần. Khi bắt đầu project mới, tạo lại theo chuẩn:

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

---

## 3. Quy tắc ghi nhớ để tránh nhầm lẫn

### Không được làm sai

- Không dùng trạng thái của một project để kết luận trực tiếp giai đoạn của PM Agent.
- Không nói PM Agent production-ready nếu chưa có evidence production-grade.
- Không trộn lẫn framework PM Agent với project do PM Agent quản lý.
- Không khôi phục branch team/specialist-agent cũ trong active workflow khi chưa có design mới được duyệt.

### Luôn trả lời theo 2 lớp nếu cần

1. **PM Agent framework đang ở đâu?**
2. **Project mà PM Agent đang quản lý đang ở đâu?**

---

## 4. Câu trả lời chuẩn ngắn gọn

### Nếu hỏi: PM Agent đang ở đâu?

> PM Agent đang ở giai đoạn hardening framework core sau cleanup workspace. Branch team/specialist-agent cũ đã được loại khỏi active workflow và sẽ được thiết kế lại sau.

### Nếu hỏi: hiện có project active không?

> Hiện workspace chính chưa có project active trong `projects/active/`. Khi có project mới, PM Agent sẽ tạo cấu trúc project chuẩn và quản lý theo workflow hiện tại.
