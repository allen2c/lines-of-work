title = "Kiểm tra tồn kho thực tế"

content = """
- Sau khi tiếp nhận, truy vấn tồn kho trong hệ thống WMS (Warehouse Management System) cho từng SKU.
- Nếu tồn kho khả dụng (available stock) đủ cho toàn bộ đơn, đơn chuyển sang trạng thái "Sẵn sàng lấy hàng".
- Nếu thiếu một hoặc nhiều SKU, hệ thống tự động tạo đơn chờ (backorder) cho phần thiếu, phần có sẵn vẫn xử lý bình thường. Gửi email/Zalo thông báo cho khách hàng về thời gian dự kiến nhập hàng (thường 3-7 ngày).
- Đối với hàng tồn kho dự trữ (safety stock) – mỗi SKU có ngưỡng tối thiểu (ví dụ: điện thoại iPhone 15: 10 cái, tủ lạnh Samsung: 5 cái). Khi tồn kho dưới ngưỡng, tự động gửi cảnh báo cho bộ phận thu mua.
- Trường hợp hàng tồn kho thực tế lệch với hệ thống (kiểm kê định kỳ), ưu tiên điều chỉnh theo số thực tế và báo cáo lên quản lý kho.
"""

version = "0.0.1"
