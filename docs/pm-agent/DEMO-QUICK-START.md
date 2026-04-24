# 🚀 DEMO QUICK START - Web Bán Hàng

**Thời gian:** 2026-04-24  
**Trạng thái:** ✅ Sẵn sàng demo

---

## 1. Chuẩn bị trước demo (5 phút)

### 1.1 Kiểm tra môi trường
```bash
# Terminal 1: Frontend dev server
cd projects/web-ban-hang/frontend
npm run dev
# → http://localhost:3000

# Terminal 2: Backend server (optional, nếu có)
cd projects/web-ban-hang/backend
npm run dev
# → http://localhost:5000
```

### 1.2 Chuẩn bị browser
- Mở Chrome/Firefox
- Truy cập: http://localhost:3000
- Clear cache: Ctrl+Shift+Delete → Clear all
- Mở DevTools: F12 → Toggle device toolbar (Ctrl+Shift+M)

### 1.3 Chuẩn bị slides
- Mở PowerPoint/Google Slides
- Copy nội dung từ section 4 của báo cáo chính
- Hoặc dùng script text-based (section 3)

---

## 2. Demo Flow (10-15 phút)

### 2.1 Intro (1 phút)
```
"Xin chào mọi người! Hôm nay mình sẽ demo Web Bán Hàng - 
một nền tảng e-commerce hiện đại được xây dựng với React, 
Vite, và Tailwind CSS.

Chúng ta sẽ đi qua luồng mua hàng hoàn chỉnh từ trang chủ 
cho đến khi đặt hàng thành công."
```

### 2.2 Home Page (2 phút)
```
[Truy cập http://localhost:3000]

"Đây là trang chủ. Chúng ta có:

1. Hero slider - tự động chuyển slide mỗi 5 giây
   [Chỉ vào hero section]
   
2. Featured Products - 4 sản phẩm nổi bật
   [Scroll xuống, chỉ vào product cards]
   
3. Categories - 4 danh mục chính
   [Scroll xuống, chỉ vào category cards]
   
Toàn bộ giao diện sử dụng Tailwind CSS với gradient, 
shadow, và animation mượt mà.

[Click 'Shop Now' hoặc 'View Products']"
```

### 2.3 Products Page (3 phút)
```
[Trang Products]

"Đây là trang danh sách sản phẩm với 1200 sản phẩm mock data.

Tính năng:
1. Tìm kiếm - gõ 'Tai nghe'
   [Gõ vào search box]
   Kết quả lọc ngay lập tức.

2. Lọc danh mục - chọn 'Thời trang'
   [Click category button]
   URL tự động cập nhật: /products?category=fashion
   
3. Phân trang - có 100 trang (12 sản phẩm/trang)
   [Click trang 2, 3, 10]
   Pagination hoạt động mượt mà.

4. Responsive - resize window xuống mobile
   [Ctrl+Shift+M hoặc resize]
   Layout tự động điều chỉnh, hamburger menu xuất hiện.

[Click vào một sản phẩm]"
```

### 2.4 Product Detail (2 phút)
```
[Trang Product Detail]

"Chi tiết sản phẩm hiển thị:

1. Gallery hình ảnh - 4 ảnh, click để xem
   [Click vào các ảnh nhỏ]
   
2. Thông tin sản phẩm:
   - Giá & giá cũ (có discount)
   - Rating ⭐ & số lượng đã bán
   - Số lượng còn hàng
   
3. Chọn số lượng & thêm giỏ hàng
   [Chọn số lượng 2]
   [Click 'Thêm vào giỏ hàng']
   Alert: 'Đã thêm 2 sản phẩm vào giỏ hàng!'
   
4. Mô tả chi tiết & đánh giá từ khách hàng
   [Scroll xuống]
   3 reviews mẫu với rating & comment.

[Click icon giỏ hàng ở header]"
```

### 2.5 Cart Page (2 phút)
```
[Trang Cart]

"Giỏ hàng của bạn có 3 sản phẩm:

1. Mỗi item hiển thị:
   - Hình ảnh, tên, giá
   - Số lượng (có nút +/-)
   - Nút xóa
   
2. Tóm tắt đơn hàng bên phải:
   - Tạm tính: 82.470.000₫
   - Phí vận chuyển: 30.000₫
   - Tổng cộng: 82.500.000₫
   
3. Promo: Miễn phí vận chuyển cho đơn từ 500k
   [Chỉ vào promo box]
   
4. Nút 'Thanh toán' & 'Tiếp tục mua sắm'
   [Click 'Thanh toán']"
```

### 2.6 Checkout Page (2 phút)
```
[Trang Checkout]

"Form thanh toán với các trường:

1. Thông tin khách hàng:
   - Họ tên, Email, SĐT
   
2. Địa chỉ giao hàng:
   - Địa chỉ, Tỉnh/Thành phố
   
3. Phương thức thanh toán:
   - COD (Thanh toán khi nhận hàng)
   - Chuyển khoản ngân hàng
   - Thẻ tín dụng/ghi nợ
   - Ví điện tử MoMo
   
4. Ghi chú đơn hàng (optional)

5. Sidebar hiển thị tóm tắt đơn hàng

[Điền form]
[Chọn phương thức thanh toán]
[Click 'Đặt hàng']"
```

### 2.7 Success Page (1 phút)
```
[Trang Success]

"Đặt hàng thành công! 🎉

Hiển thị:
1. Icon check xanh với animation
2. Mã đơn hàng: #ORD12345678
3. Thông tin đầy đủ:
   - Địa chỉ giao hàng
   - SĐT & Email
   - Phương thức thanh toán
4. Danh sách sản phẩm đã đặt
5. Các bước tiếp theo:
   - Xác nhận đơn hàng (1 giờ)
   - Chuẩn bị & gửi (24 giờ)
   - Giao hàng & thông báo
6. Nút 'Tiếp tục mua sắm' & 'Về trang chủ'

Vậy là hoàn thành luồng mua hàng!"
```

### 2.8 Admin Panel (2 phút - optional)
```
[Truy cập http://localhost:3000/admin]

"Đây là trang quản trị dành cho admin.

Desktop view:
- Sidebar cố định bên trái
- Dashboard hiển thị 4 thống kê:
  * Tổng sản phẩm: 1200
  * Tổng đơn hàng: 458
  * Doanh thu: 125.000.000₫
  * Người dùng: 892
- Biểu đồ doanh thu 12 tháng

Mobile view:
[Resize xuống mobile]
- Hamburger menu xuất hiện
- Click menu → sidebar slide in
- Responsive layout tự động điều chỉnh

Các tab:
- Dashboard (thống kê)
- Sản phẩm (quản lý - đang phát triển)
- Đơn hàng (quản lý - đang phát triển)
- Người dùng (đang phát triển)
- Cài đặt (đang phát triển)"
```

### 2.9 Responsive Demo (2 phút)
```
[Mở DevTools: F12]
[Toggle device toolbar: Ctrl+Shift+M]

"Bây giờ mình sẽ demo responsive design.

[Chọn iPhone SE]
- Layout tự động điều chỉnh
- Text size phù hợp
- Buttons dễ click (min 44px)
- Navigation collapse thành hamburger menu

[Chọn iPad]
- Grid: 2 cột
- Sidebar có thể ẩn/hiện

[Chọn Desktop]
- Grid: 3-4 cột
- Sidebar cố định

Tất cả đều sử dụng Tailwind CSS responsive breakpoints:
- sm (640px), md (768px), lg (1024px), xl (1280px)"
```

---

## 3. Q&A Handling

### Q: Tại sao dùng mock data?
**A:** Để frontend team phát triển độc lập. Backend sẽ được integrate trong sprint tiếp theo. Mock data giúp test UI/UX flow hoàn chỉnh.

### Q: Performance như thế nào?
**A:** 
- Build time: 633ms (cực nhanh)
- Bundle size: 4.40 kB (rất nhỏ)
- Vite HMR: Dev experience tuyệt vời
- Pagination: Giảm DOM nodes

### Q: Có accessibility không?
**A:** Đã có cơ bản (semantic HTML, alt text, keyboard nav). Cần audit thêm với Lighthouse, axe DevTools.

### Q: Deploy như thế nào?
**A:**
- Frontend: Vercel/Netlify (free)
- Backend: Railway/Render (free)
- Database: MongoDB Atlas (free 512MB)

### Q: Timeline hoàn thành?
**A:**
- Phase 1 (✅ Done): Frontend UI/UX
- Phase 2 (2-3 ngày): Backend API
- Phase 3 (1-2 ngày): Integration
- Phase 4 (1 ngày): Deploy

---

## 4. Troubleshooting

| Vấn đề | Giải pháp |
|--------|----------|
| App không load | Refresh page (Ctrl+R) |
| API fail | Giải thích fallback to mock data |
| Responsive lỗi | Resize lại window |
| Build fail | Dùng dev server (npm run dev) |
| Port 3000 bị dùng | Thay port: `npm run dev -- --port 3001` |

---

## 5. Cheat Sheet

### URLs
- Home: http://localhost:3000/
- Products: http://localhost:3000/products
- Product Detail: http://localhost:3000/products/1
- Cart: http://localhost:3000/cart
- Checkout: http://localhost:3000/checkout
- Login: http://localhost:3000/login
- Register: http://localhost:3000/register
- Admin: http://localhost:3000/admin

### Keyboard Shortcuts
- F12: Open DevTools
- Ctrl+Shift+M: Toggle device toolbar
- Ctrl+R: Refresh page
- Ctrl+Shift+Delete: Clear cache
- Ctrl/Cmd + +: Zoom in
- Ctrl/Cmd + -: Zoom out

### Demo Tips
- Nói chậm, rõ ràng
- Highlight cursor khi click
- Pause để audience absorb
- Zoom in khi cần
- Backup slides/script

---

## 6. Post-Demo

### Feedback Collection
- Hỏi audience về UI/UX
- Hỏi về tính năng nào cần thêm
- Hỏi về performance
- Hỏi về timeline

### Next Steps
- Ghi lại feedback
- Báo cáo cho PM
- Schedule backend development
- Plan testing & QA

---

**Chúc demo thành công! 🎉**

Nếu có vấn đề, liên hệ Lệ 💧
