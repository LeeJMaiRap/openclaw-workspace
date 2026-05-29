# Kiểm tra an toàn bản nháp Shopee TSS PRO 1M80

Ngày kiểm tra: 2026-05-29 UTC
Vai trò: Claim Safety Agent
File được kiểm tra: `live-validation-shopee-source-specific-draft.md`
Nguồn bằng chứng: link Shopee + ảnh chụp màn hình do Doanh cung cấp
Trạng thái: ĐẠT NHƯNG CẦN SỬA NHỎ

## Kết luận nhanh

Bản nháp Shopee nhìn chung an toàn vì:

- Không dùng lại thông tin Aureday/Amazon.
- Không nói `50 inch`.
- Không nói `1KG`.
- Có cảnh báo giá/đánh giá có thể thay đổi.
- Có chặn các claim mạnh như `chống rung tối đa`, `ổn định tuyệt đối`, `giá rẻ nhất`.

Tuy nhiên cần sửa vài cụm để an toàn hơn trước khi tạo bản cuối.

## Các điểm cần sửa

### 1. Cụm `đặt máy cao hơn, gọn hơn`

Câu hiện tại:

```text
Quay video bằng điện thoại mà cần đặt máy cao hơn, gọn hơn? Mẫu TSS PRO 1M80 trên Shopee là một lựa chọn đáng kiểm tra nếu anh cần tripod/gậy chụp ảnh có remote Bluetooth.
```

Vấn đề:

- `gọn hơn` có thể hiểu là chắc chắn gọn hơn sản phẩm khác.
- An toàn hơn nếu nói theo nhu cầu: `dễ mang theo` dựa trên listing ghi gấp khoảng/hơn 30cm.

Câu nên sửa:

```text
Quay video bằng điện thoại mà cần đặt máy cao hơn hoặc cần gậy chụp ảnh dễ mang theo? Mẫu TSS PRO 1M80 trên Shopee là một lựa chọn đáng kiểm tra nếu anh cần tripod/gậy chụp ảnh có remote Bluetooth.
```

### 2. Cụm `đây là sản phẩm đáng kiểm tra`

Câu hiện tại:

```text
Nếu anh cần quay một mình hoặc livestream, đây là sản phẩm đáng kiểm tra — nhưng vẫn nên xem lại biến thể, giá, đánh giá và vận chuyển trực tiếp trên Shopee trước khi mua.
```

Vấn đề:

- Câu này ổn, nhưng nên nhấn mạnh `theo listing` để tránh nghe như đánh giá độc lập.

Câu nên sửa:

```text
Nếu anh cần quay một mình hoặc livestream, đây là sản phẩm đáng kiểm tra theo thông tin listing — nhưng vẫn nên xem lại biến thể, giá, đánh giá và vận chuyển trực tiếp trên Shopee trước khi mua.
```

### 3. Cụm `có remote Bluetooth`

Câu hiện tại:

```text
TSS PRO 1M80 là mẫu tripod/gậy chụp ảnh điện thoại trên Shopee có remote Bluetooth, chiều cao tối đa 1m80 và nhiều biến thể để chọn.
```

Vấn đề:

- An toàn hơn nếu nói `listing ghi có remote Bluetooth`, vì bằng chứng là ảnh listing.

Câu nên sửa:

```text
Theo ảnh chụp listing Shopee ngày 2026-05-29, TSS PRO 1M80 là mẫu tripod/gậy chụp ảnh điện thoại được ghi có remote Bluetooth, chiều cao tối đa 1m80 và nhiều biến thể để chọn.
```

### 4. Giá và đánh giá

Câu hiện tại:

```text
Trong ảnh chụp Shopee ngày 2026-05-29, sản phẩm hiển thị giá 199.000đ - 379.000đ và 4.9/5 với 56 đánh giá.
```

Đánh giá:

- Câu này dùng được trong bản nội bộ.
- Nếu đưa ra công khai, cần kiểm tra lại đúng ngày đăng.

Câu an toàn hơn cho bản công khai:

```text
Trong ảnh chụp Shopee ngày 2026-05-29, sản phẩm hiển thị giá và đánh giá; các thông tin này cần kiểm tra lại trực tiếp trên Shopee trước khi đăng hoặc trước khi mua.
```

Nếu Business PM muốn giữ số cụ thể, phải kèm ngày:

```text
Trong ảnh chụp Shopee ngày 2026-05-29, sản phẩm hiển thị giá 199.000đ - 379.000đ và 4.9/5 với 56 đánh giá; các thông tin này có thể thay đổi, nên cần kiểm tra lại trực tiếp trên Shopee trước khi đăng hoặc trước khi mua.
```

## Rà soát từng phần

| Phần | Kết quả | Ghi chú |
|---|---|---|
| Dữ liệu được phép dùng | ĐẠT | Phân biệt rõ dùng được và không dùng. |
| Bản nháp 1 hook | CẦN SỬA NHỎ | Sửa `gọn hơn`. |
| Bản nháp 1 thân bài | ĐẠT | Có cảnh báo claim mạnh. |
| Bản nháp 1 kêu gọi hành động | ĐẠT | Yêu cầu kiểm tra lại trên Shopee. |
| Bản nháp 2 hook | CẦN SỬA NHỎ | Thêm `theo ảnh chụp listing`. |
| Bản nháp 2 thân bài | ĐẠT | Có cảnh báo dữ liệu thay đổi. |
| Bản nháp 2 kêu gọi hành động | ĐẠT | Không có mua ngay quá mạnh. |
| Checklist ngắn | ĐẠT | Dạng câu hỏi, an toàn. |
| Caption ngắn | CẦN SỬA NHỎ | Thêm `theo thông tin listing`. |
| Caption rất ngắn | ĐẠT | Có `listing ghi`, an toàn. |
| Câu cần tránh | ĐẠT | Đã chặn claim rủi ro. |
| Checklist trước khi đăng | ĐẠT | Có kiểm tra giá, biến thể, vận chuyển. |

## Bản sửa an toàn đề xuất

### Hook 1 sửa

```text
Quay video bằng điện thoại mà cần đặt máy cao hơn hoặc cần gậy chụp ảnh dễ mang theo? Mẫu TSS PRO 1M80 trên Shopee là một lựa chọn đáng kiểm tra nếu anh cần tripod/gậy chụp ảnh có remote Bluetooth.
```

### Hook 2 sửa

```text
Theo ảnh chụp listing Shopee ngày 2026-05-29, TSS PRO 1M80 là mẫu tripod/gậy chụp ảnh điện thoại được ghi có remote Bluetooth, chiều cao tối đa 1m80 và nhiều biến thể để chọn.
```

### Caption ngắn sửa

```text
TSS PRO 1M80 trên Shopee là mẫu tripod/gậy chụp ảnh điện thoại được listing mô tả có remote Bluetooth, xoay 360° và chiều cao tối đa 1m80. Nếu anh cần quay một mình hoặc livestream, đây là sản phẩm đáng kiểm tra theo thông tin listing — nhưng vẫn nên xem lại biến thể, giá, đánh giá và vận chuyển trực tiếp trên Shopee trước khi mua.
```

### Câu giá/đánh giá an toàn

Bản nội bộ có thể giữ số:

```text
Trong ảnh chụp Shopee ngày 2026-05-29, sản phẩm hiển thị giá 199.000đ - 379.000đ và 4.9/5 với 56 đánh giá; các thông tin này có thể thay đổi, nên cần kiểm tra lại trực tiếp trên Shopee trước khi đăng hoặc trước khi mua.
```

Bản công khai nên dùng câu mềm hơn nếu không kiểm tra lại ngay ngày đăng:

```text
Trong ảnh chụp Shopee ngày 2026-05-29, sản phẩm hiển thị giá và đánh giá; các thông tin này cần kiểm tra lại trực tiếp trên Shopee trước khi đăng hoặc trước khi mua.
```

## Claim bị chặn tiếp tục

Không dùng:

- `chống rung tối đa`.
- `ổn định tuyệt đối`.
- `vững chắc` như kết luận.
- `remote ổn định`.
- `shop uy tín/chính hãng`.
- `giá rẻ nhất`.
- `đáng tiền nhất`.
- `đã test`.
- `mình đang dùng`.
- `phù hợp mọi điện thoại`.
- `tải trọng 1KG`.
- `bảo đảm giao hàng` vì ảnh có trường vận chuyển `Không hỗ trợ`.

## Kết luận

```text
ĐẠT NHƯNG CẦN SỬA NHỎ
```

Bản nháp đủ tốt để tạo bản cuối nội bộ sau khi áp dụng các sửa nhỏ ở trên.

## Bước tiếp theo đề xuất bằng tiếng Việt

Tạo bản cuối nội bộ cho Shopee:

```text
agent-system/tests/2026-05-27-live-readonly-validation-plan/outputs/live-validation-shopee-final-draft.md
```

Bước đó làm gì:

- Áp dụng các câu đã sửa an toàn.
- Tạo bản nội dung cuối để Business PM xem.
- Vẫn ghi rõ chưa được đăng công khai nếu chưa kiểm tra lại giá, đánh giá, vận chuyển đúng ngày đăng.

Vì sao cần:

- Bản hiện tại là bản nháp.
- Safety review đã yêu cầu sửa vài câu.
- Cần một bản cuối sạch hơn để dùng làm mẫu chuẩn cho hệ thống.

Ảnh hưởng hệ thống:

- Không sửa code.
- Không đăng bài.
- Không mua hàng.
- Chỉ tạo thêm file bản cuối trong thư mục test.
