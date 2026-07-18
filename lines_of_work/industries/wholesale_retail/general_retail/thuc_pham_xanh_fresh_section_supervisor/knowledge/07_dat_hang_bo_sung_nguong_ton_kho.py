title = "Đặt hàng bổ sung và ngưỡng tồn kho"

content = """
- Xác định ngưỡng tồn kho tối thiểu: hàng tươi sống (thịt, cá, rau) = 3 ngày bán, hàng đông lạnh = 7 ngày bán. Dựa trên doanh số trung bình 7 ngày gần nhất.
- Đặt hàng hàng ngày vào lúc 9h sáng cho giao hàng ngày hôm sau. Sử dụng phần mềm đặt hàng nội bộ hoặc gọi điện cho nhà cung cấp chính.
- Công thức đặt hàng: Số lượng đặt = (Dự báo bán 2 ngày tới) - (Tồn kho hiện tại) + (Tồn kho an toàn 1 ngày). Ví dụ: dự báo bán thịt 50kg/ngày, tồn 30kg, an toàn 20kg → đặt 50*2 - 30 + 20 = 90kg.
- Điều chỉnh theo mùa: dịp lễ Tết tăng 30-50% lượng đặt, mùa mưa giảm 20% cho rau lá.
- Xác nhận đơn hàng với nhà cung cấp trước 11h. Nếu không nhận được xác nhận, gọi lại hoặc tìm nguồn thay thế.
- Theo dõi tỷ lệ giao đúng hạn: nếu nhà cung cấp giao thiếu >2 lần trong tháng, báo cáo quản lý để xem xét thay đổi.
"""

version = "0.0.1"
