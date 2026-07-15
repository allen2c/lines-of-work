title = "Xử lý sự cố hệ thống SCADA"

content = """
- Mất kết nối SCADA: kiểm tra mạng LAN, router 4G dự phòng. Nếu mất internet, chuyển sang kết nối 4G tự động. Nếu vẫn mất, kiểm tra nguồn điện của thiết bị SCADA (UPS).
- Dữ liệu hiển thị sai: kiểm tra cảm biến (CT, PT) tại inverter, so sánh với đồng hồ đo độc lập. Hiệu chỉnh hệ số nhân trong SCADA nếu cần.
- Lỗi phần mềm: khởi động lại dịch vụ iSolarCloud trên server. Nếu không khắc phục, liên hệ hỗ trợ kỹ thuật Sungrow qua hotline 24/7.
- Backup dữ liệu: sao lưu cơ sở dữ liệu SCADA hàng tuần vào ổ cứng ngoài, lưu trữ ít nhất 1 năm.
"""

version = "0.0.1"
