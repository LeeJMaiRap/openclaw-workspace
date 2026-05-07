# Bước 3 - Thiết kế nhóm skill lõi cho PM Agent

## Mục tiêu
Thiết kế các nhóm skill lõi cho PM Agent theo hướng nhỏ, rõ đầu vào - đầu ra, dễ kiểm chứng, dễ mở rộng.

Bước này chưa vội code skill ngay. Trước hết cần chốt:
- nhóm skill nào cần có
- mỗi skill xử lý việc gì
- input/output là gì
- skill nào nên làm thử đầu tiên

---

## 1) Nguyên tắc thiết kế skill

### 1.0. Cấu trúc thư mục skill
Trước khi bắt đầu tạo skill thật, phải chuẩn bị **folder skill** rõ ràng.

Quy tắc chốt:
- Mỗi skill phải nằm trong **một thư mục riêng**.
- Mỗi skill phải có file `SKILL.md` riêng.
- Không dồn nhiều skill khác nhau vào chung một thư mục.
- Khi bắt đầu hiện thực hóa ở bước sau, phải tạo cấu trúc thư mục skill trước rồi mới viết nội dung skill.

Ví dụ:

```text
skills/
  meeting-notes-summary/
    SKILL.md
  action-items-extractor/
    SKILL.md
  meeting-minutes-generator/
    SKILL.md
```

### 1.1. Skill phải nhỏ
Không tạo một skill quá rộng kiểu “làm mọi việc PM”.

Nên chia thành các skill nhỏ như:
- tóm tắt ghi chú họp
- tạo action items
- tạo meeting minutes
- bóc tách yêu cầu
- tạo user stories
- cập nhật decision log

### 1.2. Skill phải có input rõ
Mỗi skill cần biết nó nhận gì.

Ví dụ:
- ghi chú họp thô
- transcript cuộc họp
- đoạn chat mô tả yêu cầu
- brief dự án
- note nghiệp vụ
- file Markdown có sẵn

### 1.3. Skill phải có output rõ
Mỗi skill cần biết nó trả về gì.

Ví dụ:
- file Markdown meeting minutes
- danh sách action items
- PRD draft
- BRD draft
- user stories
- decision log entry

### 1.4. Ưu tiên Markdown trước
Output chính nên là Markdown.
PDF/export chỉ làm sau khi nội dung Markdown đã ổn.

### 1.5. Có bước hỏi lại nếu thiếu thông tin
Skill không nên tự bịa khi input thiếu.
Nếu thiếu thông tin quan trọng, skill phải tạo danh sách câu hỏi cần làm rõ.

---

## 2) Nhóm skill lõi đề xuất

## Nhóm A - Skill tài liệu cuộc họp
Mục tiêu: biến ghi chú họp thô thành tài liệu có cấu trúc.

### A1. Meeting Notes Summary
**Input:** ghi chú họp thô / transcript / đoạn chat sau họp  
**Output:** bản tóm tắt ngắn gồm:
- bối cảnh
- nội dung chính
- quyết định
- việc cần làm
- điểm còn mơ hồ

### A2. Action Items Extractor
**Input:** ghi chú họp thô hoặc meeting summary  
**Output:** danh sách action items gồm:
- việc cần làm
- người phụ trách nếu có
- deadline nếu có
- trạng thái
- ghi chú liên quan

### A3. Meeting Minutes Generator
**Input:** ghi chú họp thô + thông tin cuộc họp  
**Output:** biên bản họp Markdown gồm:
- tiêu đề
- thời gian
- người tham gia
- mục tiêu cuộc họp
- nội dung thảo luận
- quyết định
- action items
- follow-up

---

## Nhóm B - Skill phân tích yêu cầu
Mục tiêu: giúp bóc tách yêu cầu sản phẩm/phần mềm từ input thô.

### B1. Requirement Clarifier
**Input:** mô tả yêu cầu ban đầu  
**Output:**
- yêu cầu đã hiểu
- điểm rõ
- điểm mơ hồ
- câu hỏi cần hỏi lại

### B2. User Story Generator
**Input:** yêu cầu đã rõ hoặc brief tính năng  
**Output:** user stories theo format:
- As a...
- I want...
- So that...
- acceptance criteria

### B3. Acceptance Criteria Generator
**Input:** user story hoặc mô tả tính năng  
**Output:** acceptance criteria rõ ràng, có thể test được.

---

## Nhóm C - Skill tài liệu sản phẩm/PM
Mục tiêu: tạo bản nháp tài liệu PM chuẩn từ thông tin đầu vào.

### C1. PRD Draft Generator
**Input:** ý tưởng sản phẩm / yêu cầu / brief  
**Output:** PRD draft Markdown gồm:
- mục tiêu
- người dùng
- vấn đề cần giải quyết
- scope
- functional requirements
- non-functional requirements
- assumptions
- open questions

### C2. BRD Draft Generator
**Input:** ghi chú nghiệp vụ / mô tả business process  
**Output:** BRD draft Markdown gồm:
- business context
- objectives
- stakeholders
- current process
- proposed process
- business rules
- constraints

### C3. Status Report Generator
**Input:** tiến độ hiện tại / task list / notes  
**Output:** status report gồm:
- việc đã xong
- việc đang làm
- blockers
- rủi ro
- kế hoạch tiếp theo

### C4. Client Contract Draft Generator
**Input:** thông tin công ty, thông tin khách hàng, phạm vi công việc, thời gian, chi phí, điều khoản thanh toán, điều khoản trách nhiệm  
**Output:** bản nháp hợp đồng giữa công ty và khách hàng ở dạng Markdown, gồm:
- thông tin hai bên
- phạm vi công việc/dịch vụ
- thời gian thực hiện
- chi phí và thanh toán
- quyền và nghĩa vụ các bên
- bảo mật
- nghiệm thu/bàn giao
- chấm dứt hợp đồng
- điều khoản chung
- danh sách điểm còn thiếu cần xác nhận

**Lưu ý:**
- Skill này chỉ nên tạo **bản nháp hợp đồng** để anh rà lại.
- Không tự khẳng định giá trị pháp lý cuối cùng nếu chưa được kiểm tra theo mẫu/luật áp dụng thực tế.

---

## Nhóm D - Skill quản lý tri thức dự án
Mục tiêu: đưa thông tin quan trọng vào cấu trúc tri thức dự án.

### D1. Decision Log Updater
**Input:** quyết định đã chốt trong chat/họp  
**Output:** entry decision log gồm:
- quyết định
- lý do
- ngày
- tác động
- người liên quan nếu có

### D2. Project Summary Updater
**Input:** các thay đổi lớn / trạng thái mới  
**Output:** cập nhật project summary ngắn gọn.

### D3. Knowledge Note Creator
**Input:** đoạn chat/nội dung có giá trị lưu lại  
**Output:** note Markdown có tiêu đề, tag, nội dung tóm tắt, nguồn/context.

---

## Nhóm E - Skill điều phối công việc PM
Mục tiêu: hỗ trợ theo dõi việc cần làm, pending, follow-up.

### E1. Task List Builder
**Input:** ghi chú họp / đoạn chat / brief  
**Output:** task list có nhóm việc, ưu tiên, trạng thái.

### E2. Follow-up Reminder Planner
**Input:** danh sách pending/action items  
**Output:** đề xuất nhắc việc/follow-up theo thời gian.

### E3. Roadmap Progress Summarizer
**Input:** TODO/roadmap hiện tại  
**Output:** tóm tắt tiến độ:
- đã xong
- đang làm
- bị hoãn
- bước tiếp theo

---

## 3) Ghi chú bổ sung về skill hợp đồng

Skill tạo hợp đồng giữa công ty với khách hàng là skill có giá trị thực tế cao, nhưng nên xếp sau các skill nền như summary cuộc họp và bóc tách yêu cầu.

Lý do:
- hợp đồng cần độ chính xác cao
- thường phụ thuộc mẫu chuẩn của công ty
- có yếu tố pháp lý và điều khoản cần rà thủ công
- phù hợp để tạo **draft đầu tiên**, không nên coi là bản cuối tự động

---

## 4) Thứ tự ưu tiên đề xuất

## Ưu tiên 1 - Meeting Notes Summary
Lý do:
- input dễ có sẵn
- sát nhu cầu PM
- dễ kiểm thử
- là nền cho Meeting Minutes và Action Items

## Ưu tiên 2 - Action Items Extractor
Lý do:
- output rõ
- dễ kiểm chứng
- có giá trị thực tế sau họp

## Ưu tiên 3 - Meeting Minutes Generator
Lý do:
- là tài liệu PM phổ biến
- có thể dùng lại output từ Summary + Action Items

## Ưu tiên 4 - Requirement Clarifier
Lý do:
- giúp tránh hiểu sai yêu cầu
- phù hợp với workflow phân tích nghiệp vụ/phần mềm

## Ưu tiên 5 - User Story Generator
Lý do:
- cần khi chuyển yêu cầu sang backlog/dev task

## Ưu tiên 6 - Client Contract Draft Generator
Lý do:
- có giá trị kinh doanh thực tế
- giúp tiết kiệm thời gian soạn hợp đồng ban đầu
- nhưng cần để sau vì đòi hỏi mẫu chuẩn và rà soát pháp lý cẩn thận hơn

---

## 5) Skill đầu tiên nên làm thử

### Đã chốt chọn
```text
meeting-notes-summary
```

### Vì sao chọn skill này trước
- Dễ test với ghi chú cuộc họp thật đã có.
- Không cần tích hợp Obsidian ngay.
- Có thể chạy trong workflow hiện tại.
- Output tạo nền cho các skill sau.

### Input mẫu
```text
Ghi chú cuộc họp thô dạng Markdown hoặc text.
```

### Output mẫu
```markdown
# Summary - <Tên cuộc họp>

## Bối cảnh
...

## Nội dung chính
- ...

## Quyết định
- ...

## Action Items
- [ ] ...

## Điểm còn mơ hồ / cần hỏi lại
- ...
```

---

## 6) Tiêu chí hoàn thành Bước 3

Bước 3 hoàn thành khi:
- [ ] Chốt danh sách nhóm skill lõi.
- [ ] Chốt skill đầu tiên để làm thử.
- [ ] Chốt input/output của skill đầu tiên.
- [ ] Chốt nơi lưu skill/spec/template.
- [ ] Có kế hoạch sang Bước 4: chọn skill đầu tiên để hiện thực hóa.

---

## 7) Gợi ý bước tiếp theo

Sau note này, nên làm tiếp:
1. anh duyệt danh sách nhóm skill lõi
2. chốt skill đầu tiên: `Meeting Notes Summary`
3. thiết kế spec chi tiết cho skill đó
4. test với file ghi chú cuộc họp ngày 2026-04-25
