# Biên bản họp - Khởi động PM Agent

## 1. Thông tin cuộc họp
- Ngày họp: 2026-05-07
- Thời gian: Chưa có thông tin
- Kênh/Địa điểm: Telegram
- Người tham gia: Anh Doanh, Lệ
- Người ghi chú: Lệ

## 2. Mục tiêu cuộc họp
- Chốt lại hướng xây hệ skill PM từ đầu theo một chuẩn mới.
- Xác định skill nền ưu tiên đầu tiên để phục vụ toàn bộ workflow về sau.

## 3. Nội dung thảo luận
### 3.1. Reset hướng skill cũ
- Hai bên thống nhất không dùng lại các đánh giá skill cũ.
- Hệ skill PM sẽ được phân tích lại từ đầu dựa trên nhu cầu thực tế và output tài liệu PM.

### 3.2. Ưu tiên skill nền đầu tiên
- Skill `markdown-to-pdf` được xác định là skill hạ tầng cần làm trước.
- Lý do là mọi skill PM khác về sau đều cần có file PDF để review.

### 3.3. Hướng đi tiếp theo
- Sau khi `markdown-to-pdf` ổn định, skill tiếp theo sẽ là `requirement-clarifier`.
- Các skill PM khác sẽ tiếp tục được build theo chuẩn mới và đều phải có file demo.

## 4. Quyết định / Kết luận
- Không sử dụng lại các đánh giá skill cũ.
- Ưu tiên đầu tiên là build `markdown-to-pdf`.
- Mọi tài liệu PM đầu ra cuối mặc định là PDF.

## 5. Action Items
| STT | Việc cần làm | Người phụ trách | Deadline | Ghi chú |
|---|---|---|---|---|
| 1 | Thiết kế lại skill `markdown-to-pdf` từ số 0 | Lệ | Chưa có thông tin | Skill hạ tầng đầu tiên |
| 2 | Tạo file demo PDF cho `markdown-to-pdf` | Lệ | Chưa có thông tin | Dùng để anh review |
| 3 | Build tiếp demo cho `requirement-clarifier` | Lệ | Chưa có thông tin | Skill PM thứ hai |

## 6. Vấn đề còn mở
- Chưa chốt ngay skill thứ ba sẽ là gì.
- Chưa xác định thứ tự đầy đủ cho toàn bộ các skill PM còn lại.

## 7. Bước tiếp theo
- Hoàn tất bản build đầu tiên của `markdown-to-pdf`.
- Sau đó tiếp tục build `requirement-clarifier` và các skill PM tiếp theo theo cùng chuẩn demo + PDF review.
