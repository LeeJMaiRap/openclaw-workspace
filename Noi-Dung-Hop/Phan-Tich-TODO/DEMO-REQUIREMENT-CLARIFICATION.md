# Requirement Clarification - PM Agent dùng qua Telegram

## 1. Tóm tắt yêu cầu đang hiểu
- Cần xây dựng một PM Agent hoạt động qua Telegram.
- Agent được kỳ vọng hỗ trợ các công việc PM thực tế như ghi chú cuộc họp, tạo tài liệu PM, quản lý tri thức dự án và follow-up công việc.
- Về lâu dài có thể mở rộng hỗ trợ voice.
- Tài liệu đầu ra cuối cùng cần dùng thực tế và ưu tiên ở dạng PDF.

## 2. Phạm vi bước đầu
### 2.1. Trong phạm vi
- PM Agent dùng qua Telegram
- Ghi chú cuộc họp
- Tạo tài liệu PM
- Quản lý tri thức dự án
- Follow-up công việc
- PDF là định dạng đầu ra cuối cho tài liệu bàn giao

### 2.2. Ngoài phạm vi / chưa thấy đề cập
- Nhiều người dùng hay một người dùng chính
- Dashboard quản trị riêng
- Tích hợp CRM hoặc hệ thống ngoài khác
- Mức độ tự động hóa của voice

## 3. Điểm đã rõ
- Telegram là kênh sử dụng chính.
- PM Agent là hướng phát triển chính.
- Các nhóm chức năng mong muốn gồm ghi chú họp, tài liệu PM, tri thức dự án và follow-up.
- Đầu ra tài liệu cuối cần ưu tiên PDF.
- Voice là nhu cầu có thể làm về sau.

## 4. Điểm còn mơ hồ
- Chưa rõ 2-3 chức năng PM cần ưu tiên đầu tiên.
- Chưa rõ loại tài liệu PM nào là output quan trọng nhất ở giai đoạn đầu.
- Chưa rõ follow-up chỉ là nhắc việc hay có cả theo dõi trạng thái.
- Chưa rõ quản lý tri thức dự án giai đoạn đầu tập trung vào note, decision log hay project summary.
- Chưa rõ voice ở giai đoạn sau là voice-to-text, text-to-voice hay cả hai.

## 5. Câu hỏi cần hỏi lại
1. Ba chức năng PM quan trọng nhất anh muốn ưu tiên ở giai đoạn đầu là gì?
2. Trong các loại tài liệu PM, loại nào cần làm đầu tiên: biên bản họp, action items, PRD, BRD hay báo cáo tiến độ?
3. Phần follow-up anh muốn dừng ở mức nhắc việc hay cần cả theo dõi trạng thái công việc?
4. Quản lý tri thức dự án ở giai đoạn đầu cần tập trung vào note, decision log hay project summary?
5. Voice ở giai đoạn sau anh muốn ưu tiên voice-to-text, text-to-voice hay cả hai?

## 6. Giả định tạm thời
- Hệ thống trước mắt phục vụ một người dùng chính.
- Giai đoạn đầu nên ưu tiên tài liệu họp và workflow PM cơ bản trước khi mở rộng sang voice.

## 7. Rủi ro nếu hiểu sai
- Dễ làm phạm vi quá rộng ngay từ đầu.
- Dễ ưu tiên sai loại tài liệu hoặc sai workflow PM.
- Dễ đầu tư vào voice quá sớm trong khi phần PM lõi chưa ổn.
- Dễ hiểu sai mức độ kỳ vọng của phần follow-up và quản lý tri thức.

## 8. Đề xuất bước tiếp theo
- Chốt 2-3 chức năng PM ưu tiên đầu tiên.
- Chốt loại tài liệu PM đầu tiên cần dùng thực tế.
- Chốt phạm vi giai đoạn 1 trước khi đi tiếp sang kế hoạch chi tiết hoặc user stories.
