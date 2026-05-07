# Final Spec - `markdown-to-pdf`

## 1. Mục tiêu
Chuyển **1 file Markdown có sẵn** thành **1 file PDF thật**, đẹp, đọc ổn, không lỗi font tiếng Việt, dùng để review hoặc bàn giao.

---

## 2. Vai trò
- Đây là **skill hạ tầng xuất bản cuối** cho toàn bộ hệ PM.
- Các skill PM khác tạo nội dung ở `.md`.
- File giao cho anh mặc định là `.pdf`.

Workflow chuẩn:

```text
PM skill -> .md -> markdown-to-pdf -> .pdf
```

---

## 3. Khi nào dùng
Dùng khi:
- đã có file `.md`
- cần xuất file `.pdf`
- cần file gửi review / gửi khách / gửi sếp

Không dùng khi:
- chưa có nội dung tài liệu
- user chỉ muốn giữ Markdown
- user đang yêu cầu sửa nội dung nghiệp vụ

---

## 4. Input bắt buộc
- đường dẫn file `.md`

## Input tùy chọn
- đường dẫn file `.pdf` output
- style xuất PDF
- tiêu đề tài liệu nếu cần

Nếu thiếu file nguồn thì phải hỏi lại.

---

## 5. Output bắt buộc
- 1 file `.pdf`

Quy tắc mặc định:
```text
input.md -> input.pdf
```

---

## 6. Yêu cầu chất lượng bắt buộc
PDF đầu ra phải:
- là file PDF thật
- không rỗng
- không lỗi font tiếng Việt
- giữ đúng nội dung gốc
- đọc rõ, format ổn

Markdown gốc phải được giữ nguyên.

---

## 7. Style bắt buộc
Skill phải hỗ trợ tối thiểu 3 style:
- `clean` = tối giản, business
- `modern` = hiện đại, dễ review
- `formal` = nghiêm túc, phù hợp tài liệu gửi khách/sếp

Nếu user không chọn style:
- mặc định dùng `formal`

---

## 8. Font / tiếng Việt
- Phải hỗ trợ Unicode tiếng Việt đúng.
- Phải có font fallback rõ ràng.
- Không được coi là hoàn thành nếu PDF bị vỡ dấu.

---

## 9. Hướng triển khai kỹ thuật
Skill nên có 2 tầng:

### Tầng 1 - baseline ổn định
- render Markdown -> PDF thật
- ưu tiên chạy được chắc chắn
- không lỗi font

### Tầng 2 - styled output
- thêm CSS / HTML renderer hoặc browser renderer
- tối ưu giao diện đẹp hơn

---

## 10. Quality checks bắt buộc
Trước khi kết luận xong phải kiểm tra:
- [ ] file PDF tồn tại
- [ ] file PDF > 0 byte
- [ ] header là `%PDF-`
- [ ] tiếng Việt hiển thị đúng
- [ ] file `.md` gốc còn nguyên

---

## 11. Cấu trúc skill chuẩn
```text
skills/
  PM/
    markdown-to-pdf/
      SKILL.md
      references/
        output-rules.md
        style-guide.md
      scripts/
        render-pdf-baseline.*
        render-pdf-styled.*
      assets/
        fonts/
```

---

## 12. File demo bắt buộc
### Input demo
```text
/root/.openclaw/workspace/Noi-Dung-Hop/Phan-Tich-TODO/DEMO-MARKDOWN-TO-PDF.md
```

### Output demo
```text
/root/.openclaw/workspace/Noi-Dung-Hop/Phan-Tich-TODO/DEMO-MARKDOWN-TO-PDF.pdf
```

---

## 13. Definition of Done
Skill `markdown-to-pdf` chỉ được coi là xong khi:
1. có folder skill đúng chuẩn
2. có `SKILL.md`
3. có script render baseline
4. có script hoặc cơ chế styled output
5. có font Unicode tiếng Việt ổn
6. có file demo `.md`
7. xuất được file demo `.pdf`
8. anh tải file demo và đọc được bình thường
