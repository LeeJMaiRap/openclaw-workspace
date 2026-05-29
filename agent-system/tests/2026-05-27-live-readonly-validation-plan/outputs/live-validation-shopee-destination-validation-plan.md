# Kế hoạch kiểm tra trang đích Shopee cho thị trường Việt Nam

Ngày tạo: 2026-05-29 UTC
Vai trò phụ trách: Business PM + Product Hunter + Claim Safety
Trạng thái: Kế hoạch, chưa kiểm tra link Shopee cụ thể

## Mục tiêu

Kiểm tra xem Shopee có nên là trang đích chính cho nội dung tripod điện thoại tại thị trường Việt Nam hay không.

Lý do: người mua Việt Nam quen mua trên Shopee hơn Amazon, nên nếu làm nội dung affiliate hoặc nội dung bán hàng cho thị trường Việt, Shopee có khả năng phù hợp hơn.

## Vì sao không nên dùng Amazon làm trang đích chính cho Việt Nam

Link Amazon đã kiểm tra:

```text
https://www.amazon.com/Aureday-Extendable-Adjustable-Smartphone-Compatible/dp/B081CF1DMM
```

Kết quả Amazon:

```text
Currently unavailable.
We don't know when or if this item will be back in stock.
```

Ý nghĩa:

- Sản phẩm đang không có hàng trên trang Amazon đã kiểm tra.
- Không nên dùng lời kêu gọi mua ngay cho link này.
- Amazon chỉ nên dùng như bằng chứng nhận diện sản phẩm, không phải trang bán chính cho chiến dịch Việt Nam.

## Vì sao nên ưu tiên Shopee

Shopee phù hợp hơn với người mua Việt vì thường có:

- Giá bằng VNĐ.
- Phí vận chuyển nội địa.
- Voucher hoặc mã giảm giá theo nền tảng.
- Số lượng đã bán.
- Đánh giá sao.
- Bình luận/ảnh/video từ người mua.
- Thông tin shop trong nước hoặc shop có giao về Việt Nam.
- Chính sách hoàn hàng/đổi trả hiển thị theo nền tảng.

Những dữ liệu này giúp Product Hunter và Claim Safety kiểm tra sản phẩm thực tế hơn trước khi tạo nội dung đăng.

## Rủi ro khi kiểm tra Shopee bằng agent

Shopee có thể:

- Yêu cầu JavaScript.
- Chặn bot hoặc hiển thị trang rỗng.
- Yêu cầu đăng nhập để xem một số dữ liệu.
- Hiển thị nội dung khác nhau theo vùng/thiết bị.
- Tải dữ liệu động khiến công cụ đọc web không thấy đầy đủ thông tin.

Quy tắc an toàn:

- Không đăng nhập.
- Không thêm vào giỏ hàng.
- Không mua hàng.
- Không nhắn shop.
- Không follow/like/comment/share.
- Không bypass CAPTCHA/chống bot.
- Nếu bị chặn, ghi rõ là bị chặn và yêu cầu Doanh cung cấp link/screenshot.

## Cách kiểm tra đề xuất

### Cách A — Anh cung cấp link Shopee cụ thể

Đây là cách tốt nhất.

Anh gửi một hoặc vài link Shopee sản phẩm tripod điện thoại phù hợp.

Agent sẽ kiểm tra công khai, chỉ đọc thông tin hiển thị.

### Cách B — Agent tự tìm link Shopee công khai

Dùng khi anh chưa có link.

Từ khóa tìm kiếm gợi ý:

```text
tripod điện thoại 50 inch remote Shopee
```

```text
tripod điện thoại có remote 1m3 Shopee
```

```text
gậy tripod điện thoại bluetooth remote Shopee
```

Giới hạn:

- Tìm ít nguồn.
- Không quét hàng loạt.
- Dừng nếu Shopee chặn.
- Không cố vượt chặn.

### Cách C — Anh gửi ảnh chụp màn hình hoặc thông tin thủ công

Dùng khi Shopee chặn agent.

Anh có thể gửi ảnh hoặc copy các trường:

- Tên sản phẩm.
- Giá.
- Số đã bán.
- Đánh giá sao.
- Số đánh giá.
- Shop.
- Mô tả thông số: chiều cao, remote, kẹp, tải trọng.
- Link sản phẩm.

Agent sẽ ghi rõ: đây là bằng chứng do người dùng cung cấp, không phải agent tự kiểm chứng trực tiếp.

## Dữ liệu cần thu thập từ Shopee

| Nhóm dữ liệu | Cần lấy gì | Cách dùng |
|---|---|---|
| Danh tính sản phẩm | Tên sản phẩm, link, shop | Xác nhận đúng loại sản phẩm. |
| Giá | Giá VNĐ đang hiển thị | Chỉ dùng nếu kiểm tra cùng ngày đăng. |
| Voucher/khuyến mãi | Nếu thấy rõ | Mặc định không dùng trong copy nếu không cần. |
| Số đã bán | Nếu thấy rõ | Có thể dùng làm tín hiệu nền tảng, nhưng cần cẩn thận. |
| Đánh giá | Sao, số đánh giá | Không biến thành cam kết chất lượng. |
| Thông số | Chiều cao, remote, kẹp, tải trọng, chất liệu | Dùng để so với nội dung copy. |
| Hình ảnh/video review | Nếu công khai thấy được | Dùng làm tín hiệu phụ, không claim cá nhân đã test. |
| Vận chuyển/hoàn hàng | Nếu thấy rõ | Không overclaim. |
| Rủi ro | Thiếu thông số, shop ít đánh giá, mô tả mâu thuẫn | Dùng để quyết định có nên publish không. |

## Quy tắc so khớp với bản nội dung hiện tại

Bản nội dung hiện tại đang nói về nhóm sản phẩm:

```text
tripod điện thoại khoảng 50 inch, có kẹp điện thoại/tablet, có remote, dùng để đặt máy cố định khi quay một mình.
```

### Đạt

Shopee link phù hợp nếu thấy rõ:

- Là tripod điện thoại.
- Chiều cao khoảng 50 inch hoặc tương đương.
- Có remote hoặc điều khiển Bluetooth nếu copy nói remote.
- Có kẹp điện thoại.
- Giá/đánh giá/số bán rõ nếu muốn dùng làm tín hiệu thương mại.

### Đạt nhưng cần sửa nội dung

Nếu sản phẩm Shopee:

- Không phải 50 inch nhưng vẫn là tripod điện thoại.
- Có remote không rõ ràng.
- Không ghi tải trọng.
- Chỉ phù hợp để bàn, không phải đặt sàn.
- Không có thông tin kẹp điện thoại rõ.

Khi đó phải sửa copy để chỉ nói đúng thông tin Shopee hiển thị.

### Không đạt

Không dùng link Shopee nếu:

- Không đúng loại tripod điện thoại.
- Không có remote nhưng copy nói remote.
- Mô tả quá thiếu, không xác nhận được thông số chính.
- Trang bị chặn và không có ảnh/thông tin do anh cung cấp.
- Shop/trang có dấu hiệu rủi ro cao mà không đủ dữ liệu kiểm tra.

## Kết quả cần tạo khi kiểm tra thật

Sau khi có link Shopee hoặc agent tìm được link công khai, tạo file:

```text
agent-system/tests/2026-05-27-live-readonly-validation-plan/outputs/live-validation-shopee-destination-source-check.md
```

Cấu trúc file:

```markdown
# Kiểm tra trang đích Shopee

Ngày kiểm tra: <UTC>
Trạng thái: ĐẠT / ĐẠT NHƯNG CẦN SỬA / KHÔNG ĐẠT / BỊ CHẶN

## Link Shopee
<link>

## Kết quả truy cập
- Đọc được hay bị chặn:
- Có cần đăng nhập không:
- Có CAPTCHA/bot wall không:

## Thông tin sản phẩm thấy được
- Tên sản phẩm:
- Shop:
- Giá:
- Số đã bán:
- Đánh giá:
- Số đánh giá:

## Thông số thấy được
- Chiều cao:
- Remote:
- Kẹp điện thoại:
- Tải trọng:
- Chất liệu:
- Kích thước gấp gọn:

## So với nội dung hiện tại
| Nội dung đang định nói | Shopee có chứng minh không? | Cần sửa gì? |
|---|---:|---|

## Kết luận
- Có dùng làm trang đích chính không:
- Nếu có, copy cần sửa gì:
- Nếu không, cần tìm link khác hay dừng:
```

## Bước tiếp theo sau kế hoạch này

Cần thực hiện một trong hai cách:

1. Doanh gửi link Shopee cụ thể để kiểm tra.
2. Doanh cho phép agent tự tìm link Shopee công khai với số lượng thấp.

Vì Doanh đã chọn hướng agent tự tìm công khai, bước tiếp theo hợp lý là:

```text
Tìm 1-3 link Shopee công khai cho tripod điện thoại khoảng 50 inch có remote, dừng nếu bị chặn, rồi ghi kết quả vào live-validation-shopee-destination-source-check.md.
```

Ảnh hưởng hệ thống:

- Không sửa code.
- Không sửa agent config.
- Không đăng bài.
- Không mua hàng.
- Chỉ tạo thêm file kiểm tra trong thư mục test.
