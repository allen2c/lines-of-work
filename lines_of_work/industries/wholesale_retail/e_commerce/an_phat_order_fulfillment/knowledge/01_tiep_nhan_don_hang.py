title = "Tiếp nhận đơn hàng từ các kênh"

content = """
- Đơn hàng được đồng bộ tự động từ Shopee, Lazada, Tiki và website An Phát vào hệ thống OMS (Order Management System) mỗi 5 phút.
- Kiểm tra các trường bắt buộc: họ tên, số điện thoại (10-11 số, đầu 03/05/07/08/09), địa chỉ chi tiết (số nhà, đường, phường/xã, quận/huyện, tỉnh/thành phố), danh sách sản phẩm (SKU, số lượng, đơn giá), phương thức thanh toán (COD, chuyển khoản ngân hàng, thẻ tín dụng/ghi nợ, ví điện tử).
- Nếu thiếu thông tin hoặc sai định dạng, đơn tự động chuyển sang trạng thái "Chờ xác nhận" và gửi thông báo cho CSKH để liên hệ khách hàng bổ sung.
- Đối với đơn COD, kiểm tra hạn mức tối đa 15.000.000 VNĐ (theo chính sách công ty). Đơn trên 15 triệu phải được phê duyệt bởi trưởng nhóm.
- Ghi nhận thời gian đặt hàng để tính ưu tiên: đơn đặt trước 12h trưa được xử lý trong ngày, sau 12h chuyển sang ngày làm việc tiếp theo.
"""

version = "0.0.1"
