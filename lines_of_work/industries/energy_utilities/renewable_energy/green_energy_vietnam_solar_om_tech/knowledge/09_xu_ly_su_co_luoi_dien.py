title = "Xử lý sự cố kết nối lưới điện"

content = """
- Mất lưới (Grid Loss): inverter tự ngắt, kiểm tra điện áp lưới tại tủ trung thế. Nếu mất lưới toàn bộ, báo EVN ngay, ghi nhận thời gian mất. Khi lưới có lại, inverter tự động kết nối sau 5 phút (theo quy định EVN).
- Sụt áp lưới (Under Voltage): inverter giảm công suất hoặc ngắt. Kiểm tra tải lưới, báo EVN nếu kéo dài > 10 phút.
- Yêu cầu cắt giảm công suất từ EVN: nhận lệnh qua điện thoại hoặc email, thực hiện giảm công suất bằng cách tắt dần các inverter (ưu tiên tắt inverter có hiệu suất thấp). Ghi nhận thời gian và mức giảm.
- Sự cố trạm biến áp: kiểm tra dầu biến áp, rơ le Buchholz, nhiệt độ. Nếu có dấu hiệu quá nhiệt hoặc rò rỉ dầu, dừng máy và báo trưởng ca.
"""

version = "0.0.1"
