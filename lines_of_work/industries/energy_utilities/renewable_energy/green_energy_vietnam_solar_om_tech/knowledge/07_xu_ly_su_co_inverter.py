title = "Xử lý sự cố inverter"

content = """
- Lỗi thường gặp: "Grid Over Voltage" (do lưới tăng áp đột ngột) – inverter tự ngắt, chờ 5 phút rồi khởi động lại. Nếu lặp lại nhiều lần, báo EVN.
- "DC Bus Over Voltage" – kiểm tra điện áp string, có thể do bóng che hoặc tấm pin hỏng gây mất cân bằng. Dùng SCADA xem string nào có điện áp cao bất thường, kiểm tra thực địa.
- "IGBT Fault" – thường do quá nhiệt hoặc lỗi driver. Reset inverter, nếu vẫn lỗi thì thay module IGBT (cần kỹ thuật viên có chứng chỉ). Ghi log lỗi và báo nhà cung cấp.
- "Communication Error" – kiểm tra cáp Ethernet, switch, IP của inverter. Ping từ SCADA, nếu không được thì reset bộ truyền thông (COM board) hoặc thay thế.
"""

version = "0.0.1"
