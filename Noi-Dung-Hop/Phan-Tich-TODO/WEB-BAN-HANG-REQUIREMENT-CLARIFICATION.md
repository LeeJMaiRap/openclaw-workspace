# Requirement Clarification - Dự án demo Web Bán Hàng cho PM Agent

## 1. Tóm tắt yêu cầu đang hiểu
- Dự án demo đầu tiên được dùng để kiểm thử cách PM Agent hỗ trợ quản lý một dự án thực tế.
- Project demo là một website bán hàng có frontend và backend riêng.
- PM Agent không chỉ theo dõi code mà còn phải hỗ trợ tạo tài liệu PM, kế hoạch, task board, risk log, status monitoring và closure artifacts cho dự án này.
- Demo này được dùng như một case study thực tế để kiểm tra năng lực PM Agent trên OpenClaw.

## 2. Phạm vi bước đầu
### 2.1. Trong phạm vi
- Website bán hàng có frontend và backend
- Hướng dẫn chạy demo
- Tài liệu PM cho toàn bộ vòng đời dự án
- Tracking trạng thái dự án qua các file PM
- Dùng project làm dữ liệu thật để test skill PM

### 2.2. Ngoài phạm vi / chưa thấy đề cập
- Tích hợp thanh toán thật
- Hạ tầng production/deploy hoàn chỉnh
- Multi-user workflow thực tế
- SLA vận hành sau triển khai
- Quy mô khách hàng thực tế ngoài bài demo

## 3. Điểm đã rõ
- Dự án demo có tên `web-ban-hang`.
- Có backend và frontend tách riêng.
- Có tài liệu initiation, planning, execution và monitoring trong `projects/web-ban-hang/`.
- Có file `DEMO_GUIDE.md` hướng dẫn chạy demo.
- PM Agent được định hướng dùng dự án này để thử nghiệm workflow PM end-to-end.
- Dự án phù hợp làm case thực hành cho PM Agent và bài thực tập.

## 4. Điểm còn mơ hồ
- Chưa rõ mục tiêu kinh doanh chính của website bán hàng demo là gì ngoài mục đích làm project thực hành.
- Chưa rõ ai là người dùng mục tiêu chính của sản phẩm demo.
- Chưa rõ mức độ hoàn thiện mong muốn: demo kỹ thuật, demo PM workflow, hay sản phẩm gần production.
- Chưa rõ tiêu chí thành công của demo này được đo bằng tài liệu PM, tính năng chạy được, hay cả hai.
- Chưa rõ phần nào trong project sẽ được dùng làm ưu tiên chính để huấn luyện PM Agent trước.

## 5. Câu hỏi cần hỏi lại
1. Mục tiêu chính của project demo `web-ban-hang` là để kiểm thử PM workflow, để demo sản phẩm, hay để vừa demo sản phẩm vừa demo PM Agent?
2. Ở giai đoạn hiện tại, anh muốn PM Agent ưu tiên hỗ trợ phần nào nhất của dự án này: tài liệu, planning, status reporting hay follow-up task?
3. Tiêu chí review của anh cho dự án demo này là gì: tài liệu PM đầy đủ, chức năng web chạy ổn, hay cả hai?
4. Với project này, tài liệu nào anh muốn nhận đầu ra đầu tiên ở dạng PDF: status report, meeting minutes, project plan hay final review?
5. Dự án demo này có được xem như mẫu chuẩn để xây các skill PM tiếp theo hay chỉ là một case test tạm thời?

## 6. Giả định tạm thời
- Project `web-ban-hang` hiện được dùng như dự án mẫu để PM Agent luyện workflow thực tế.
- Mục tiêu ngắn hạn là tạo ra tài liệu PM usable hơn là đưa web bán hàng lên production hoàn chỉnh.
- Tài liệu xuất ra dưới dạng PDF là một phần quan trọng của việc review chất lượng PM Agent.

## 7. Rủi ro nếu hiểu sai
- Dễ xây PM skill lệch trọng tâm nếu không rõ dự án demo ưu tiên PM workflow hay ưu tiên sản phẩm chạy thật.
- Dễ tạo sai loại tài liệu nếu không chốt artifact đầu tiên cần review.
- Dễ đánh giá sai tiến độ nếu không thống nhất tiêu chí hoàn thành của project demo.
- Dễ mở rộng skill PM theo hướng quá rộng nếu coi project demo như production project ngay từ đầu.

## 8. Đề xuất bước tiếp theo
- Chốt mục tiêu chính của project demo `web-ban-hang`.
- Chốt artifact PDF đầu tiên cần review cho project này.
- Chốt phần workflow PM nào sẽ được dùng để huấn luyện skill tiếp theo từ dự án demo này.