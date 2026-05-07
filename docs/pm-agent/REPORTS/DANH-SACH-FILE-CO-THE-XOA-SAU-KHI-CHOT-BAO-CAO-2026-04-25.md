# DANH SÁCH FILE CÓ THỂ XÓA SAU KHI CHỐT BÁO CÁO

## Nguyên tắc
Danh sách này chỉ liệt kê các file **có thể xóa** sau khi anh đã:
- chốt nội dung báo cáo
- không cần nghiên cứu sâu thêm
- không cần dùng PM Agent framework để tiếp tục phát triển ngay

Các file dưới đây không nên xóa vội nếu anh còn muốn tiếp tục mở rộng PM Agent hoặc Web Bán Hàng.

---

## A. File có thể xóa mà KHÔNG ảnh hưởng trực tiếp đến demo Web Bán Hàng

### 1. `docs/pm-agent/ANALYSIS/PHAN-1-So-sanh-tai-lieu-tham-khao.md`
**Lý do có thể xóa:**
- chỉ phục vụ nghiên cứu nền
- không ảnh hưởng đến việc chạy PM Agent hiện tại
- không ảnh hưởng đến demo Web Bán Hàng

### 2. `docs/pm-agent/ANALYSIS/PHAN-2-Quy-trinh-PM-chuan.md`
**Lý do có thể xóa:**
- là tài liệu nền về PM truyền thống
- không phải file runtime hay file demo

### 3. `docs/pm-agent/ANALYSIS/PHAN-3-Kien-truc-PM-Agent.md`
**Lý do có thể xóa:**
- phục vụ giải thích kiến trúc
- không ảnh hưởng chạy demo
- chỉ nên giữ nếu anh muốn báo cáo sâu hơn về kiến trúc

### 4. `docs/pm-agent/ANALYSIS/PHAN-4-Thiet-ke-tai-lieu.md`
**Lý do có thể xóa:**
- là tài liệu phân tích về artifacts
- không ảnh hưởng đến bản demo hiện tại

### 5. `docs/pm-agent/ANALYSIS/PHAN-5-Workflow-chi-tiet.md`
**Lý do có thể xóa:**
- là tài liệu phân tích sâu workflow
- không ảnh hưởng đến code hay demo đã hoàn thành

### 6. `docs/pm-agent/ANALYSIS/PHAN-6-Prompt-va-Instruction.md`
**Lý do có thể xóa:**
- chỉ cần nếu còn tiếp tục phát triển PM Agent
- không ảnh hưởng đến demo web hiện tại

### 7. `docs/pm-agent/ANALYSIS/PHAN-7-Vi-du-thuc-te.md`
**Lý do có thể xóa:**
- là tài liệu minh họa
- không ảnh hưởng đến web demo hoặc báo cáo cuối nếu đã có file tổng hợp

### 8. `docs/pm-agent/ANALYSIS/PHAN-8-Cach-trien-khai-tren-OpenClaw.md`
**Lý do có thể xóa:**
- là tài liệu hướng dẫn triển khai
- chỉ cần nếu tiếp tục dựng PM Agent mới từ đầu

### 9. `docs/pm-agent/ANALYSIS/CAI-DAT-MOI-TRUONG-VA-THONG-TIN-NGUOI-DUNG.md`
**Lý do có thể xóa:**
- là tài liệu nền môi trường/cấu hình
- không ảnh hưởng đến demo web

### 10. `docs/pm-agent/ANALYSIS/README.md`
**Lý do có thể xóa:**
- chỉ là file mục lục cho thư mục ANALYSIS
- nếu xóa cả ANALYSIS thì file này cũng không cần giữ

---

## B. File có thể xóa nếu anh không tiếp tục phát triển PM Agent framework

### 11. `docs/pm-agent/PROMPTS/01-initiate.md`
### 12. `docs/pm-agent/PROMPTS/02-planning.md`
### 13. `docs/pm-agent/PROMPTS/03-task-board.md`
### 14. `docs/pm-agent/PROMPTS/04-execute.md`
### 15. `docs/pm-agent/PROMPTS/05-monitor.md`
### 16. `docs/pm-agent/PROMPTS/06-closure.md`
**Lý do có thể xóa:**
- đây là prompt framework cho PM Agent
- không ảnh hưởng trực tiếp đến bản demo web đã tạo xong
- chỉ nên giữ nếu còn muốn dùng PM Agent tiếp tục quản lý các dự án khác

### 17. Toàn bộ `docs/pm-agent/TEMPLATES/`
**Lý do có thể xóa:**
- chỉ là bộ template tạo tài liệu PM
- bản demo hiện tại đã có tài liệu cụ thể rồi
- xóa không làm hỏng demo web hiện tại

### 18. `docs/pm-agent/SYSTEM-PROMPT.md`
**Lý do có thể xóa:**
- là file lõi để vận hành PM Agent framework
- nếu chỉ còn mục tiêu giữ web demo thì có thể xóa
- nếu còn muốn tiếp tục PM Agent thì không nên xóa

### 19. `docs/pm-agent/WORKFLOW.md`
**Lý do có thể xóa:**
- tương tự SYSTEM-PROMPT, chỉ cần nếu tiếp tục duy trì PM Agent

### 20. `docs/pm-agent/PROJECT-SUMMARY.md`
**Lý do có thể xóa:**
- là file tổng kết framework, không ảnh hưởng demo web

### 21. `docs/pm-agent/EXAMPLES/example-project-workflow.md`
**Lý do có thể xóa:**
- là ví dụ minh họa, không phải file runtime

---

## C. File thuyết trình / báo cáo có nội dung trùng nhau, có thể xem xét giữ 1 số file chính

### 22. `docs/pm-agent/REPORTS/TONG-HOP-BAO-CAO-PM-AGENT-2026-04-24.md`
**Lý do có thể xóa:**
- nội dung đã bị trùng một phần với báo cáo cuối cùng
- nếu đã có báo cáo cuối cùng thì file này không còn là file quan trọng nhất

### 23. `docs/pm-agent/REPORTS/TASK-017-DEMO-PREP.md`
**Lý do có thể xóa:**
- chứa script demo, FAQ, test prep rất chi tiết
- nếu anh chỉ cần bản báo cáo cuối cùng và kịch bản thuyết trình ngắn, file này có thể bỏ
- tuy nhiên nên giữ đến sau buổi họp

### 24. `docs/pm-agent/DEMO-QUICK-START.md`
**Lý do có thể xóa:**
- chỉ là quick guide hỗ trợ demo
- không bắt buộc nếu đã có báo cáo cuối + kịch bản thuyết trình
- nhưng nên giữ đến sau buổi họp

### 25. `docs/pm-agent/REPORTS/KICH-BAN-THUYET-TRINH-NGAN-GON-2026-04-25.md`
**Lý do có thể xóa sau buổi họp:**
- chỉ dùng để nói miệng trong buổi trình bày
- không ảnh hưởng hệ thống

---

## D. File có thể xóa để giảm dung lượng, không ảnh hưởng source logic

### 26. `projects/web-ban-hang/frontend/dist/`
**Lý do có thể xóa:**
- là output build
- có thể build lại bất cứ lúc nào bằng `npm run build`
- không phải source code gốc

### 27. `projects/web-ban-hang/backend/node_modules/`
**Lý do có thể xóa:**
- là dependency cài đặt
- có thể phục hồi bằng `npm install`
- không phải source code

### 28. `projects/web-ban-hang/frontend/node_modules/`
**Lý do có thể xóa:**
- tương tự backend node_modules
- có thể phục hồi bằng `npm install`

---

## E. File KHÔNG nên xóa

### Nhóm cần giữ cho báo cáo và demo
- `docs/pm-agent/REPORTS/BAO-CAO-CUOI-CUNG-PM-AGENT-WEB-BAN-HANG-2026-04-24.md`
- `projects/web-ban-hang/` (toàn bộ source chính)
- `projects/web-ban-hang/final-report.md`
- `projects/web-ban-hang/lessons-learned.md`

### Nhóm nên giữ nếu còn muốn phát triển PM Agent
- `memory/`
- `docs/pm-agent/PROMPTS/`
- `docs/pm-agent/TEMPLATES/`
- `docs/pm-agent/SYSTEM-PROMPT.md`
- `docs/pm-agent/WORKFLOW.md`

---

## Kết luận ngắn
Nếu mục tiêu hiện tại là:
> **giữ bản demo web bán hàng + báo cáo cuối cùng + kịch bản thuyết trình**

thì nhóm file ưu tiên xem xét xóa trước là:
1. `docs/pm-agent/ANALYSIS/`
2. `docs/pm-agent/REPORTS/TONG-HOP-BAO-CAO-PM-AGENT-2026-04-24.md`
3. `docs/pm-agent/REPORTS/TASK-017-DEMO-PREP.md`
4. `docs/pm-agent/DEMO-QUICK-START.md`
5. `projects/web-ban-hang/frontend/dist/`
6. `node_modules/` của backend/frontend

---

**Lưu ý:** Chưa nên xóa trước buổi họp. Tốt nhất là xóa sau khi anh đã báo cáo xong.
