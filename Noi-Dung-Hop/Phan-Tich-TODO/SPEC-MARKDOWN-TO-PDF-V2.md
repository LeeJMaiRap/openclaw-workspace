# Spec v2 - Skill `markdown-to-pdf`

## 1) Mục tiêu

`markdown-to-pdf` dùng để chuyển **một file Markdown đã có sẵn** thành **một file PDF** dùng để review, gửi khách hàng, gửi cấp trên hoặc lưu hồ sơ.

Đây là skill **xuất bản cuối** trong hệ PM.

---

## 2) Khi nào dùng

Dùng khi:
- đã có file `.md`
- cần file `.pdf` để bàn giao / review / gửi đi
- output cuối mặc định của tài liệu PM cần là PDF

Không dùng khi:
- chưa có nội dung tài liệu
- user chỉ muốn nội dung text/Markdown
- user đang yêu cầu chỉnh nội dung nghiệp vụ, không phải xuất bản file

---

## 3) Input bắt buộc

### Bắt buộc
- đường dẫn file `.md` nguồn

### Nếu có thì tốt hơn
- đường dẫn file `.pdf` output mong muốn
- tên tài liệu
- yêu cầu format đặc biệt nếu có

### Nếu thiếu input
Skill phải hỏi lại, không tự đoán bừa file nguồn.

---

## 4) Output bắt buộc

### Output chính
- 1 file `.pdf`

### Output phụ (nội bộ, nếu cần)
- file `.md` gốc vẫn được giữ nguyên
- có thể có file `.html` trung gian nếu workflow render cần

### Quy tắc output
- `.md` là source of truth để chỉnh sửa
- `.pdf` là file xuất bản cuối

---

## 5) Cấu trúc output chuẩn

Nếu input là:
```text
/path/to/file.md
```

thì output mặc định là:
```text
/path/to/file.pdf
```

Nếu user yêu cầu path khác thì dùng path đó.

---

## 6) Quy tắc xử lý

### 6.1. Không sửa nội dung nghiệp vụ
Skill này không tự thay đổi meaning của nội dung Markdown.
Nó chỉ làm nhiệm vụ xuất bản.

### 6.2. Ưu tiên PDF thật, không phải giả lập
Kết quả phải là file PDF thật có thể tải/xem được.

### 6.3. Hỗ trợ tiếng Việt đúng
PDF output phải hiển thị tiếng Việt đúng.
Nếu renderer không hỗ trợ Unicode/font phù hợp thì phải xử lý font trước khi coi là hoàn thành.

### 6.4. Nếu môi trường thiếu tool
Skill phải:
- kiểm tra tool sẵn có
- dùng script/bundled tool phù hợp
- nếu không thể xuất PDF thật thì báo blocker kỹ thuật rõ ràng

### 6.5. Ưu tiên bản xuất ổn định trước bản đẹp
Bản đầu tiên cần:
- đúng nội dung
- đọc được
- không lỗi font
- không hỏng file

Styling đẹp hơn có thể nâng cấp sau.

---

## 7) Quality checks bắt buộc

Trước khi kết luận xong, phải kiểm tra:
- [ ] file PDF tồn tại
- [ ] file PDF không rỗng
- [ ] header file là `%PDF-`
- [ ] tiếng Việt không bị vỡ font
- [ ] file nguồn `.md` không bị mất

---

## 8) Workflow chuẩn

```text
Input: file.md
-> kiểm tra khả năng render PDF
-> xuất file.pdf
-> kiểm tra file.pdf hợp lệ
-> gửi file PDF cho user review
```

---

## 9) Cấu trúc thư mục skill

```text
skills/
  PM/
    markdown-to-pdf/
      SKILL.md
      references/
        output-rules.md
        tool-options.md
      scripts/
        render-markdown-pdf.js
      assets/
        <font nếu cần>
```

---

## 10) File demo bắt buộc

Skill này bắt buộc phải có file demo/test để chứng minh dùng được.

### Input demo đề xuất
```text
/root/.openclaw/workspace/Noi-Dung-Hop/Phan-Tich-TODO/DEMO-MARKDOWN-TO-PDF.md
```

### Output demo đề xuất
```text
/root/.openclaw/workspace/Noi-Dung-Hop/Phan-Tich-TODO/DEMO-MARKDOWN-TO-PDF.pdf
```

---

## 11) Vai trò trong hệ PM

Skill này không phải skill tạo nội dung PM.
Nó là skill **in ấn/xuất bản cuối** để phục vụ tất cả skill PM khác.

Workflow mục tiêu:

```text
skill PM tạo nội dung
-> file .md
-> markdown-to-pdf
-> file .pdf cho anh review
```
