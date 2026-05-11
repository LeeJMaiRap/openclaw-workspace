---
name: project-spec-generator
description: Tạo file `02-planning/spec.md` - đặc tả kỹ thuật chi tiết từ requirements document, charter hoặc requirement clarification; dùng khi cần tạo tài liệu spec với architecture, features, technical stack, data model và quality standards để làm cơ sở cho implementation.
---

# Project Spec Generator

## Mục tiêu

Tạo tài liệu Specification (đặc tả kỹ thuật) chi tiết để định nghĩa rõ kiến trúc hệ thống, các tính năng, công nghệ sử dụng và tiêu chuẩn chất lượng, làm cơ sở cho giai đoạn execution.

Skill này giúp:
- chuyển requirements document thành đặc tả kỹ thuật có cấu trúc
- định nghĩa kiến trúc hệ thống (system architecture, data architecture)
- mô tả chi tiết từng feature với user flow và technical approach
- xác định technical stack cụ thể
- đặt ra quality standards cho implementation

## Dùng khi nào

Dùng skill này khi:
- đã có requirements document hoặc charter
- cần tạo đặc tả kỹ thuật chi tiết trước khi bắt đầu code
- cần định nghĩa kiến trúc và công nghệ sử dụng
- cần làm rõ cách triển khai từng feature

## Không dùng khi nào

Không dùng skill này khi:
- yêu cầu còn quá mơ hồ, chưa có requirements document
- mục tiêu là tạo kế hoạch triển khai (dùng `project-plan-generator`)
- mục tiêu là tạo WBS hoặc schedule (dùng `wbs-generator`, `schedule-generator`)
- chỉ cần cập nhật một vài chi tiết kỹ thuật, không cần tạo spec mới

## Input bắt buộc

Ít nhất phải có:
- requirements document hoặc charter
- danh sách features chính
- phạm vi MVP đã được xác định

## Input tùy chọn

- technical stack đã được chọn
- architecture diagram nếu đã có
- data model nếu đã được thiết kế
- quality standards đã được thảo luận
- constraints kỹ thuật

## Output

Output là file `spec.md` theo cấu trúc chuẩn với 5-7 phần:

1. **Overview**
2. **Architecture**
3. **Features**
4. **Technical Stack**
5. **Quality Standards**
6. **Data Requirements** (tùy chọn)
7. **MVP Scope Confirmation** (tùy chọn)

## Format output chuẩn

Xem `template-output.md` để biết format đầy đủ.

Output phải tuân thủ template có sẵn trong `docs/pm-agent/TEMPLATES/spec-template.md`.

## Quy tắc xử lý

### 1. Architecture phải rõ ràng và đầy đủ
Architecture cần bao gồm:
- **System Architecture:** components, modules, integrations
- **Data Architecture:** entities, relationships, storage

Nếu có thể, nên có diagram đơn giản (ASCII art hoặc mô tả text).

### 2. Mỗi feature phải có 4 phần
Mỗi feature cần mô tả:
- **Description:** mô tả ngắn gọn
- **User Flow:** các bước người dùng thực hiện
- **Technical Approach:** cách triển khai kỹ thuật
- **Dependencies:** phụ thuộc vào feature nào khác

### 3. Technical stack phải cụ thể
Không viết chung chung như "web framework", mà phải cụ thể:
- Frontend: React.js hoặc Vue.js
- Backend: Node.js + Express
- Database: MongoDB hoặc MySQL

### 4. Quality standards phải đo lường được
Mỗi tiêu chuẩn phải rõ ràng:
- Code quality: clean code principles, component-based
- Testing: manual testing cho MVP, unit tests cho production
- Documentation: README, API docs, code comments

### 5. Phân biệt rõ MVP scope
Nếu dự án có phạm vi MVP, phải liệt kê rõ:
- ✅ Included in MVP
- ❌ Not included in MVP

### 6. Data model phải đầy đủ entities
Nếu có phần data requirements, phải liệt kê:
- các entities chính
- fields quan trọng
- relationships giữa các entities

### 7. Spec phải technical nhưng vẫn dễ hiểu
Spec không phải code, nhưng phải đủ chi tiết để developer hiểu và triển khai.

## Heuristic gợi ý khi phân tích

Khi đọc đầu vào, rà theo các câu hỏi ngầm sau:
- Kiến trúc hệ thống như thế nào? (client-server, microservices, monolith?)
- Các components chính là gì?
- Data model có những entities nào?
- Mỗi feature triển khai như thế nào về mặt kỹ thuật?
- Technical stack nào phù hợp với yêu cầu?
- Quality standards nào cần đặt ra?
- Phạm vi MVP bao gồm những gì?

## Liên hệ với workflow PM

Skill này thường chạy sau:
- `requirements-document-generator`
- `project-charter-generator`

Và là đầu vào cho:
- `project-plan-generator`
- `wbs-generator`
- `task-board-builder`

Spec là tài liệu kỹ thuật quan trọng nhất trong giai đoạn Planning.

## Liên hệ với cấu trúc dự án

Skill này tạo file:
```
projects/[project-name]/02-planning/spec.md
```

File này là cơ sở kỹ thuật cho toàn bộ implementation.

## Tiêu chí hoàn thành tốt

Một spec tốt khi:
- kiến trúc hệ thống rõ ràng, dễ hình dung
- mỗi feature có đủ 4 phần (description, user flow, technical approach, dependencies)
- technical stack cụ thể, không mơ hồ
- quality standards đo lường được
- developer đọc xong có thể bắt đầu code
- phạm vi MVP được xác định rõ ràng

## Lỗi thường gặp cần tránh

- kiến trúc quá chung chung, không cụ thể
- feature thiếu user flow hoặc technical approach
- technical stack không rõ ràng
- quality standards quá mơ hồ
- không phân biệt MVP và full scope
- spec quá ngắn, thiếu chi tiết
- spec quá dài, đi vào code implementation

## Cách dùng ngắn gọn

1. Đọc requirements document hoặc charter
2. Thiết kế kiến trúc hệ thống (system + data)
3. Mô tả chi tiết từng feature
4. Xác định technical stack cụ thể
5. Đặt ra quality standards
6. Xác nhận phạm vi MVP
7. Xuất file `spec.md` vào đúng thư mục dự án

## Tài nguyên đi kèm

- `template-output.md` - mẫu đầu ra chuẩn
- `examples/` - ví dụ spec thực tế
- Tham khảo: `docs/pm-agent/TEMPLATES/spec-template.md`
- Tham khảo: `projects/web-ban-hang/02-planning/spec.md`
