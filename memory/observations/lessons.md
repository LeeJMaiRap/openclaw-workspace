# Lessons - Bài Học & Kinh Nghiệm

## 2026-04-24: Khởi tạo & Thiết lập bộ nhớ

### Bài học
1. **Cấu trúc bộ nhớ quan trọng:** Thay vì chỉ dùng một file `MEMORY.md` đơn giản, việc tổ chức bộ nhớ theo cấu trúc (daily logs, observations, curated memory) giúp quản lý thông tin hiệu quả hơn.

2. **Học từ các dự án tốt:** Claude-mem là một ví dụ tốt về cách xây dựng hệ thống bộ nhớ bền vững cho AI agent. Mô hình của họ:
   - Progressive disclosure (tiết lộ dần)
   - Phân tách raw logs vs curated memory
   - Search index cho tìm kiếm nhanh
   - Web viewer UI cho visualization

3. **Đơn giản hóa khi cần:** Không cần áp dụng 100% mô hình phức tạp. Với OpenClaw, dùng markdown files thay vì SQLite/Chroma vẫn đủ hiệu quả và dễ maintain.

### Best Practices
- Ghi chép hàng ngày vào `daily/YYYY-MM-DD.md`
- Review định kỳ và cập nhật `observations/*.md`
- Curate `MEMORY.md` từ observations
- Giữ `index.json` để tìm kiếm nhanh

### Anti-Patterns
- ❌ Ghi tất cả vào một file duy nhất
- ❌ Không có cấu trúc rõ ràng
- ❌ Không phân biệt raw logs vs curated memory
- ❌ Không có metadata cho tìm kiếm

---

_File này sẽ được cập nhật khi em học được điều gì mới._
