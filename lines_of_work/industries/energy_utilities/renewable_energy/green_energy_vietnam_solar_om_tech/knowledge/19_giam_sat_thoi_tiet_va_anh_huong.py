title = "Giám sát thời tiết và ảnh hưởng đến vận hành"

content = """
- Trạm thời tiết tại nhà máy đo: bức xạ mặt trời (W/m²), nhiệt độ môi trường, tốc độ gió, độ ẩm, lượng mưa. Dữ liệu được tích hợp vào SCADA.
- Khi có cảnh báo bão (gió > 60 km/h): chuyển inverter sang chế độ "Storm Mode" (giảm công suất hoặc ngắt), kiểm tra chằng buộc tấm pin, di dời vật dụng dễ bay.
- Khi có sét: ngắt toàn bộ inverter và tủ điện, không làm việc ngoài trời. Sau sét, kiểm tra thiết bị chống sét (SPD) tại combiner box và tủ AC, thay nếu đèn báo hỏng.
- Mùa mưa: tăng tần suất kiểm tra rò rỉ nước vào inverter, vệ sinh máng xối trên mái pin. Độ ẩm cao có thể gây ngưng tụ trong tủ điện, cần bật đèn sấy hoặc quạt thông gió.
"""

version = "0.0.1"
