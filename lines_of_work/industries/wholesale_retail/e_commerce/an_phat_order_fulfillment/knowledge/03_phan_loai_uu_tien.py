title = "Phân loại và ưu tiên đơn hàng"

content = """
- Đơn hàng được phân loại theo 3 mức ưu tiên: Cao (đã thanh toán trước, khách VIP, đơn hỏa tốc), Trung bình (COD thông thường, đơn tiêu chuẩn), Thấp (đơn đặt trước, đơn chờ).
- Khách VIP được xác định dựa trên tổng giá trị đơn hàng trong 6 tháng qua trên 20 triệu VNĐ hoặc số lượng đơn trên 10 đơn. Danh sách VIP được cập nhật hàng tháng.
- Đơn hỏa tốc (giao trong 2-4 giờ) chỉ áp dụng cho nội thành Hà Nội và TP.HCM, giá trị đơn tối thiểu 200.000 VNĐ, phí vận chuyển cố định 50.000 VNĐ.
- Trong cùng mức ưu tiên, đơn có thời gian đặt sớm hơn được xử lý trước (FIFO).
- Đơn hàng từ các sàn TMĐT (Shopee, Lazada, Tiki) có thời gian xử lý tối đa 24 giờ theo SLA của sàn, nếu không sẽ bị phạt. Do đó, ưu tiên xử lý đơn sàn trước đơn website riêng.
"""

version = "0.0.1"
