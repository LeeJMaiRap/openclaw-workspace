# Specification: Hệ thống quản lý công việc nội bộ

## 1. Overview
Xây dựng một hệ thống web nội bộ cho team nhỏ để tạo task, giao người phụ trách, đặt deadline, comment và theo dõi trạng thái. Dashboard chỉ ở mức cơ bản cho MVP.

## 2. Architecture
### System Architecture
Browser -> Frontend React -> Backend Node.js/Express -> MongoDB

### Components
- **Frontend:** React SPA
- **Backend:** REST API Node.js/Express
- **Database:** MongoDB
- **Authentication:** JWT

### Data Architecture
#### Entities
1. **User**
   - id
   - name
   - email
   - role
2. **Task**
   - id
   - title
   - description
   - ownerId
   - deadline
   - status
3. **Comment**
   - id
   - taskId
   - userId
   - content

## 3. Features
### Feature 1: Task management
- **Description:** Tạo, sửa, theo dõi task
- **User Flow:** Tạo task -> assign owner -> cập nhật trạng thái
- **Technical Approach:** CRUD API + React forms
- **Dependencies:** Auth

### Feature 2: Comment system
- **Description:** Comment trong task
- **User Flow:** Mở task -> nhập comment -> submit
- **Technical Approach:** Task detail + comment API
- **Dependencies:** Feature 1

### Feature 3: Basic dashboard
- **Description:** Tổng hợp task theo trạng thái
- **User Flow:** Mở dashboard -> xem số liệu tổng quan
- **Technical Approach:** Aggregate task counts
- **Dependencies:** Feature 1

## 4. Technical Stack
### Frontend
- React.js
- Tailwind CSS
- React Router
- Axios

### Backend
- Node.js
- Express.js
- JWT

### Database
- MongoDB

### Development Tools
- npm
- Vite
- Git

## 5. Quality Standards
### Code Quality
- Clean code
- Reusable components
- Error handling

### Testing Requirements
- Manual testing cho MVP
- Test form validation và permission

### Documentation Requirements
- README
- API notes

## 6. MVP Scope Confirmation
### Included in MVP
✅ Tạo task
✅ Assign owner
✅ Deadline
✅ Status tracking
✅ Comment
✅ Dashboard cơ bản

### Not Included in MVP
❌ Attachment
❌ Analytics nâng cao
❌ Mobile app
