# Spec - Skill `periodic-project-report-generator`

## 1) Mục tiêu

`periodic-project-report-generator` dùng để tạo **báo cáo dự án định kỳ** từ dữ liệu thật trong folder project.

Skill này phục vụ các trường hợp như:
- báo cáo tuần
- báo cáo 2 tuần/lần
- báo cáo tháng
- báo cáo tiến độ theo kỳ

Output cuối mặc định là **PDF**.

---

## 2) Nguồn dữ liệu bắt buộc

Skill này **không được tự bịa nội dung**.
Nó phải lấy dữ liệu từ **folder project thật** hoặc danh sách file nguồn thật.

### Nguồn chính với project demo hiện tại
```text
/root/.openclaw/workspace/projects/web-ban-hang/
```

### Thứ tự ưu tiên đọc file
1. `04-monitoring/status-dashboard.md`
2. `03-execution/task-board.md`
3. `03-execution/issue-log.md`
4. `03-execution/change-log.md`
5. `02-planning/plan.md`
6. `02-planning/schedule.md`
7. `02-planning/risk-register.md`
8. `01-initiation/charter.md`
9. `01-initiation/requirements.md`

Nếu không có đủ dữ liệu, phải ghi rõ là thiếu dữ liệu nguồn.

---

## 3) Khi nào dùng

Dùng khi:
- cần báo cáo tiến độ định kỳ cho cấp trên / khách hàng / đơn vị quản lý
- cần so sánh kế hoạch và kết quả thực hiện theo kỳ
- cần tài liệu báo cáo chính thức dạng PDF

Không dùng khi:
- chưa có dữ liệu thực tế trong project files
- chỉ muốn update ngắn qua chat
- chỉ muốn status report ngắn 1 trang kiểu executive update

---

## 4) Input bắt buộc

### Bắt buộc
- đường dẫn folder project hoặc danh sách file nguồn
- kỳ báo cáo (tuần / 2 tuần / tháng)
- tên dự án

### Tùy chọn
- đơn vị chủ trì / đơn vị tham gia
- người lập báo cáo
- ngày báo cáo
- format kỳ (ví dụ: tháng 4, tuần 1-2, kỳ 2 tuần đầu tháng 5)

---

## 5) Output bắt buộc

### Output nội bộ
- 1 file Markdown báo cáo định kỳ

### Output cuối
- 1 file PDF báo cáo định kỳ

Workflow:
```text
periodic-project-report-generator -> markdown-to-pdf -> final PDF
```

---

## 6) Cấu trúc output chuẩn

```markdown
# <Tên dự án> - Báo cáo định kỳ [Kỳ báo cáo]

## 1. Thông tin dự án
- Tên dự án: ...
- Thời gian thực hiện: ...
- Phạm vi dự án: ...
- Đơn vị chủ trì / tham gia: ...

## 2. Phương hướng / mục tiêu chính
- ...

## 3. Kế hoạch và kết quả thực hiện trong kỳ
| Phân loại | Kế hoạch chính | Kết quả thực hiện chính | Tỷ lệ tiến độ | Ghi chú |
|---|---|---|---|---|

## 4. Kết quả thực hiện theo từng mốc / từng tuần
### Tuần / Mốc 1
- Kết quả thực hiện: ...
- So với kế hoạch: ...
- Ghi chú: ...

### Tuần / Mốc 2
- ...

## 5. Kế hoạch kỳ tiếp theo
- ...

## 6. Vấn đề / rủi ro / tồn đọng
- ...

## 7. Kiến nghị / đề xuất (nếu có)
- ...

## 8. Minh chứng / đính kèm
- ...
```

---

## 7) Quy tắc xử lý

### 7.1. Không bịa dữ liệu tiến độ
Không tự tạo:
- % tiến độ
- số lượng công việc hoàn tất
- milestone done
- blocker
- số buổi họp
- số liệu deliverables

nếu file nguồn không có.

### 7.2. Phải bám nguồn project thật
Mỗi kết luận trong báo cáo phải dựa trên file trạng thái thật trong project.

### 7.3. Nếu dữ liệu thiếu, phải nói rõ
Ví dụ:
```text
Chưa có thông tin trong file nguồn
```

### 7.4. Phân biệt kế hoạch và kết quả
Không trộn lẫn:
- cái dự kiến làm
- cái đã làm

### 7.5. Format báo cáo phải nghiêm túc
- đọc được
- rõ mục
- phù hợp gửi cấp trên / đơn vị quản lý / khách hàng

---

## 8) Quality checks

- [ ] Có nêu rõ nguồn dữ liệu project
- [ ] Có tách phần kế hoạch và kết quả
- [ ] Không có số liệu tự bịa
- [ ] Có phần kỳ tiếp theo
- [ ] Có phần vấn đề/tồn đọng nếu source có dấu hiệu
- [ ] Có thể export sạch sang PDF

---

## 9) Cấu trúc thư mục skill

```text
skills/
  PM/
    periodic-project-report-generator/
      SKILL.md
      references/
        output-template.md
        source-rules.md
```

---

## 10) File demo bắt buộc

### Input demo
Dùng trực tiếp folder project thật:
```text
/root/.openclaw/workspace/projects/web-ban-hang/
```

### Output demo Markdown
```text
/root/.openclaw/workspace/Noi-Dung-Hop/Phan-Tich-TODO/DEMO-PERIODIC-PROJECT-REPORT.md
```

### Output demo PDF
```text
/root/.openclaw/workspace/Noi-Dung-Hop/Phan-Tich-TODO/DEMO-PERIODIC-PROJECT-REPORT.pdf
```
