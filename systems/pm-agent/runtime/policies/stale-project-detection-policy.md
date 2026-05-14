# Stale Project Detection Policy

Quy định chuẩn để PM Agent phát hiện project, task, approval hoặc workflow đang bị `stale` (chết mềm / nằm im quá lâu mà không được xử lý đúng mức).

## Mục tiêu

Policy này giúp:
- phát hiện project không còn tiến triển nhưng chưa được đánh dấu rõ
- phát hiện approval/task/issue nằm im quá lâu
- hỗ trợ escalation đúng lúc
- giảm tình trạng owner tưởng dự án còn active nhưng thực tế đã đứng yên

---

# 1. Định nghĩa `stale`

`Stale` nghĩa là:
- vẫn còn mở / active trên giấy tờ
- nhưng không có tiến triển đủ ý nghĩa trong một khoảng thời gian đã định
- hoặc có dependency/approval đang treo quá lâu mà chưa được escalate

---

# 2. Các loại stale cần phát hiện

## A. Stale Task
Một task bị coi là stale khi:
- status là `In Progress` nhưng không có update đáng kể quá lâu
- status là `Blocked` nhưng không có escalation/action tiếp theo
- task được assign nhưng không có output/evidence mới

## B. Stale Approval
Một approval bị coi là stale khi:
- đã request nhưng quá timeout mà chưa có quyết định
- không có follow-up hoặc escalation

## C. Stale Issue
Một issue bị coi là stale khi:
- vẫn open nhưng không có update/resolution attempt trong một khoảng thời gian đáng kể
- severity cao nhưng không có owner action rõ

## D. Stale Project
Một project bị coi là stale khi:
- `status: active` nhưng không có thay đổi meaningful trong nhiều ngày
- source-of-truth không được cập nhật
- không có decision mới, task progress mới, approval mới, issue update mới
- project thực tế đã dừng nhưng metadata vẫn ghi active

---

# 3. Ngưỡng stale đề xuất

## Task stale
- `In Progress` không update quá **3 ngày** → stale
- `Blocked` không có action/escalation quá **2 ngày** → stale

## Approval stale
- scope/change approval quá **24 giờ** không phản hồi → stale nhẹ
- plan/closure approval quá **48 giờ** không phản hồi → stale
- quá timeout nhiều lần → stale nặng

## Issue stale
- issue severity High không update quá **2 ngày** → stale
- issue Medium/Low không update quá **5 ngày** → stale

## Project stale
- project active không có update meaningful quá **3 ngày** → stale nhẹ
- quá **7 ngày** → stale rõ ràng
- quá **14 ngày** mà vẫn `active` → phải xem lại status hoặc escalate

**Lưu ý:** Đây là default heuristic. Có thể tinh chỉnh theo loại project sau này.

---

# 4. Tín hiệu để xét có update meaningful hay không

Các tín hiệu được tính là meaningful update:
- task status thay đổi có bằng chứng
- issue được update/resolved
- change log có mục mới
- approval mới hoặc approval được giải quyết
- decision mới
- handoff mới có result
- report mới phản ánh tiến triển thật
- git/change evidence gắn với project có giá trị thực

Không tính là meaningful update nếu chỉ có:
- chào hỏi
- note ngắn vô nghĩa
- rename nhẹ không ảnh hưởng trạng thái thật
- report auto tạo nhưng không có thay đổi nội dung thực tế

---

# 5. Cách xử lý khi phát hiện stale

## Mức 1 — stale nhẹ
- ghi vào report
- thêm next action
- gắn nhãn cần follow-up

## Mức 2 — stale rõ
- escalate trong status dashboard hoặc daily report
- yêu cầu chốt lại owner action
- kiểm tra lại có nên giữ `active` không

## Mức 3 — stale nặng
- đề xuất đổi status thành `on-hold` / `stopped`
- yêu cầu owner xác nhận tiếp tục hay dừng
- không tiếp tục coi là active bình thường

---

# 6. Rule cứng

1. Không để project `active` quá lâu nếu không có tiến triển meaningful
2. Không để approval pending quá timeout mà không log stale
3. Không để blocked task đứng yên quá lâu mà không escalation
4. Khi stale nặng, phải xem lại metadata status chứ không chỉ viết report cho có

---

# 7. Output mong muốn khi stale được phát hiện

Khi phát hiện stale, PM Agent nên tạo ít nhất một trong các dấu vết sau:
- section trong daily report
- note trong status dashboard
- next action rõ ràng
- đề xuất đổi status project
- escalation message cho owner (nếu policy notify cho phép)

---

# 8. Kết luận ngắn

Nguyên tắc cứng:
- `active` mà không tiến triển đủ lâu → phải bị coi là stale
- stale không chỉ để quan sát, mà phải dẫn tới follow-up / escalation / status change
