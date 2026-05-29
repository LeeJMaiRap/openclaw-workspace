# Gói quyết định Business PM cho Shopee TSS PRO 1M80

Ngày tạo: 2026-05-29 UTC
Vai trò quyết định: Business PM
Trạng thái: Chờ quyết định của Business PM

## Mục tiêu

Tóm tắt toàn bộ quá trình kiểm chứng sản phẩm Shopee `TSS PRO 1M80` và đưa ra lựa chọn tiếp theo cho Business PM.

Bản này không phải nội dung đăng công khai. Đây là tài liệu để quyết định có tiếp tục dùng sản phẩm/link Shopee này hay không.

## Sản phẩm đang xét

Tên sản phẩm theo ảnh Shopee:

```text
Gậy chụp ảnh 4 chân Tripod điện thoại TSS PRO 1M80 Cây chụp hình Selfie cầm tay 3 chân Quadpod - Quay Video - Livestream
```

Link Shopee:

```text
https://shopee.vn/G%E1%BA%ADy-ch%E1%BB%A5p-%E1%BA%A3nh-4-ch%C3%A2n-Tripod-%C4%91i%E1%BB%87n-tho%E1%BA%A1i-TSS-PRO-1M80-C%C3%A2y-ch%E1%BB%A5p-h%C3%ACnh-Selfie-c%E1%BA%A7m-tay-3-ch%C3%A2n-Quadpod-Quay-Video-Livestream-i.84235092.51155387146?extraParams=%7B%22display_model_id%22%3A310491648259%2C%22model_selection_logic%22%3A3%7D&sp_atk=d81fa69f-1d9b-400b-9a0b-57394c084903&xptdk=d81fa69f-1d9b-400b-9a0b-57394c084903
```

Nguồn bằng chứng:

```text
Link Shopee + ảnh chụp màn hình do Doanh cung cấp ngày 2026-05-29.
```

## Quá trình đã làm

1. Ban đầu hệ thống kiểm tra sản phẩm Aureday/Amazon.
2. Amazon xác nhận đúng sản phẩm nhưng báo không có hàng.
3. Business PM đặt câu hỏi đúng: thị trường Việt nên ưu tiên Shopee hơn Amazon.
4. Agent thử tìm/đọc Shopee trực tiếp nhưng công cụ không trích xuất được nội dung trang.
5. Doanh cung cấp link Shopee và ảnh chụp màn hình.
6. Agent ghi bằng chứng thủ công từ ảnh.
7. Agent viết bản nháp riêng cho Shopee, không dùng lại nội dung Aureday/Amazon.
8. Claim Safety rà soát bản nháp.
9. Agent tạo bản cuối nội bộ cho Shopee.

## Artifacts đã tạo

```text
live-validation-shopee-destination-validation-plan.md
live-validation-shopee-destination-source-check.md
live-validation-shopee-manual-evidence-source-check.md
live-validation-shopee-source-specific-draft.md
live-validation-shopee-draft-safety-review.md
live-validation-shopee-final-draft.md
```

## Điểm mạnh của sản phẩm/link này

Dựa trên ảnh Shopee do Doanh cung cấp:

- Phù hợp thị trường Việt hơn Amazon.
- Có giá VNĐ hiển thị.
- Có đánh giá hiển thị: `4.9/5` với `56 đánh giá` tại thời điểm ảnh chụp.
- Có mô tả đúng nhu cầu: selfie, quay video, livestream.
- Có remote Bluetooth theo listing.
- Có chiều cao tối đa 1m80 theo listing.
- Có xoay 360° theo listing.
- Có nhiều biến thể để chọn.
- Có review người mua hiển thị trong ảnh.

## Rủi ro còn lại

### 1. Dữ liệu từ ảnh, không phải agent đọc trực tiếp

Shopee không đọc được bằng công cụ web fetch. Vì vậy hệ thống đang dựa vào ảnh do Doanh cung cấp.

Ý nghĩa:

- Dùng được cho kiểm chứng nội bộ.
- Trước khi đăng thật nên kiểm tra lại trực tiếp trên thiết bị của Doanh.

### 2. Giá và đánh giá thay đổi theo thời gian

Ảnh hiển thị:

```text
199.000đ - 379.000đ
4.9/5 với 56 đánh giá
```

Nhưng thông tin này có thể thay đổi.

Quy tắc:

- Nếu đăng nội dung có giá/đánh giá, phải kiểm tra lại đúng ngày đăng.
- Nếu không kiểm tra lại, nên bỏ số giá/đánh giá khỏi nội dung công khai.

### 3. Vận chuyển có điểm cần chú ý

Ảnh hiển thị trường:

```text
Không hỗ trợ
```

Ý nghĩa chưa rõ hoàn toàn, nhưng không được claim giao hàng/ship nếu chưa kiểm tra lại.

### 4. Shop chưa đủ cơ sở để gọi là uy tín

Ảnh có thông tin shop, nhưng không đủ để nói:

```text
shop uy tín
shop chính hãng
shop đảm bảo
```

Tỉ lệ phản hồi trong ảnh là `41%`, cần chú ý nếu đánh giá rủi ro shop.

### 5. Listing có claim quảng cáo mạnh

Không được dùng lại nguyên văn các cụm:

- `chống rung tối đa`.
- `ổn định tuyệt đối`.
- `vững chắc` như bảo chứng.
- `cực kỳ đáng giá`.

Nên chuyển thành thông tin trung tính:

- có 4 chân đế;
- có đế cao su;
- có remote Bluetooth;
- có xoay 360°;
- cao tối đa 1m80;
- gấp khoảng/hơn 30cm.

## Trạng thái nội dung hiện tại

Bản cuối nội bộ:

```text
live-validation-shopee-final-draft.md
```

Trạng thái:

```text
Sẵn sàng cho Business PM xem.
Chưa được phép đăng công khai.
```

Nội dung đã tránh:

- Không claim `giá rẻ nhất`.
- Không claim `chống rung tối đa`.
- Không claim `ổn định tuyệt đối`.
- Không claim `shop uy tín`.
- Không claim `đã test`.
- Không claim `phù hợp mọi điện thoại`.
- Không claim `tải trọng 1KG`.

## 3 lựa chọn cho Business PM

### Lựa chọn 1 — Giữ làm mẫu nội bộ

Nghĩa là:

- Không đăng.
- Dùng case này để chứng minh agent-system biết kiểm chứng Shopee và sửa copy an toàn.

Khi nào chọn:

- Nếu mục tiêu hiện tại là kiểm thử hệ thống, chưa cần chạy nội dung thật.
- Nếu chưa chắc sản phẩm/shop/link đủ tốt để dùng.

Ưu điểm:

- An toàn nhất.
- Không có rủi ro publish sai.
- Dùng tốt làm ví dụ huấn luyện pipeline.

Nhược điểm:

- Chưa kiểm tra được bước tạo gói đăng thật.

### Lựa chọn 2 — Kiểm tra lại Shopee đúng ngày rồi tạo gói đăng

Nghĩa là:

- Doanh mở lại link Shopee đúng ngày muốn đăng.
- Kiểm tra giá, biến thể, đánh giá, vận chuyển.
- Nếu vẫn phù hợp, agent tạo gói đăng theo kênh cụ thể.

Khi nào chọn:

- Nếu Business PM muốn dùng sản phẩm này thật cho nội dung Việt Nam.
- Nếu link còn mở được, giá/đánh giá/vận chuyển ổn.

Ưu điểm:

- Tiến gần publish thật nhất.
- Phù hợp thị trường Việt hơn Amazon.
- Kiểm tra được pipeline gần đầy đủ.

Nhược điểm:

- Cần kiểm tra lại thủ công vì agent không đọc được Shopee trực tiếp.
- Nếu giá/ship/biến thể thay đổi, phải sửa lại nội dung.

### Lựa chọn 3 — Tìm sản phẩm khác tốt hơn

Nghĩa là:

- Không dùng TSS PRO 1M80 ngay.
- Tìm thêm sản phẩm Shopee khác có tín hiệu tốt hơn: nhiều đánh giá hơn, shop rõ hơn, vận chuyển rõ hơn, mô tả ít claim phóng đại hơn.

Khi nào chọn:

- Nếu Business PM thấy rủi ro shop/vận chuyển chưa ổn.
- Nếu muốn sản phẩm có số bán/review mạnh hơn.
- Nếu muốn tránh listing có quá nhiều claim quảng cáo mạnh.

Ưu điểm:

- Có thể tìm được sản phẩm tốt hơn cho chiến dịch.
- Giảm rủi ro dùng link chưa tối ưu.

Nhược điểm:

- Tốn thêm thời gian.
- Vẫn có khả năng Shopee bị chặn, cần ảnh chụp/manual facts.

## Đề xuất của agent

Chọn **Lựa chọn 2** nếu mục tiêu là kiểm tra pipeline gần với thực tế nhất.

Lý do:

- Sản phẩm đã có đủ dữ liệu cơ bản để đi tiếp.
- Nội dung đã được viết lại riêng cho Shopee.
- Safety review đã chặn các claim nguy hiểm.
- Chỉ còn cần Business PM kiểm tra lại Shopee đúng ngày để tránh sai giá/đánh giá/vận chuyển.

Nếu mục tiêu chỉ là kiểm thử hệ thống, chọn **Lựa chọn 1** cũng hợp lý.

Không nên chọn Lựa chọn 3 ngay trừ khi Business PM không hài lòng với shop, vận chuyển, hoặc tín hiệu sản phẩm hiện tại.

## Quyết định cần từ Business PM

Business PM cần chọn một trong ba:

```text
1. Giữ làm mẫu nội bộ.
2. Kiểm tra lại Shopee đúng ngày rồi tạo gói đăng.
3. Tìm sản phẩm khác tốt hơn.
```

## Bước tiếp theo nếu chọn Lựa chọn 2

Tạo kế hoạch kiểm tra lại trước khi đăng:

```text
agent-system/tests/2026-05-27-live-readonly-validation-plan/outputs/live-validation-shopee-prepublish-recheck-plan.md
```

Bước đó làm gì:

- Liệt kê chính xác Doanh cần kiểm tra gì trên Shopee trước ngày đăng.
- Gồm giá, biến thể, đánh giá, vận chuyển, mô tả remote/1m80.
- Xác định nếu dữ liệu đổi thì phải sửa nội dung nào.

Vì sao cần:

- Giá/đánh giá/vận chuyển thay đổi rất nhanh.
- Shopee không đọc được trực tiếp bằng agent.
- Cần một checklist ngắn để Doanh kiểm tra thủ công trước khi tạo gói đăng.

Ảnh hưởng hệ thống:

- Không sửa code.
- Không đăng bài.
- Không mua hàng.
- Chỉ tạo thêm file kế hoạch kiểm tra trước khi đăng.
