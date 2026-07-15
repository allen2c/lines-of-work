title = "Theo dõi trạng thái đơn hàng"

content = """
- Sử dụng API tracking của từng đối tác vận chuyển để lấy trạng thái mới nhất mỗi 30 phút.
- Các trạng thái chính: Đã nhận hàng, Đang vận chuyển, Đến bưu cục trung chuyển, Đang giao, Giao thành công, Giao thất bại (không liên lạc được, từ chối nhận, sai địa chỉ).
- Cập nhật tự động vào OMS. Nếu trạng thái "Giao thất bại", hệ thống gửi cảnh báo cho nhân viên xử lý.
- Đối với đơn COD, khi trạng thái "Giao thành công", hệ thống tự động ghi nhận doanh thu và gửi thông báo cho kế toán.
- Nếu đơn không có cập nhật trạng thái trong 48 giờ (đối với nội thành) hoặc 72 giờ (liên tỉnh), coi là delay và tiến hành tra soát.
"""

version = "0.0.1"
