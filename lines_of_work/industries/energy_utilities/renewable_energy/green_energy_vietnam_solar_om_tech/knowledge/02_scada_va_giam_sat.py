title = "Hệ thống SCADA và giám sát từ xa"

content = """
- Hệ thống SCADA sử dụng phần mềm Sungrow iSolarCloud, hiển thị real-time: công suất tức thời (MW), điện áp DC/AC, dòng điện, nhiệt độ inverter, sản lượng ngày/tháng/năm.
- Các cảnh báo chính: "Inverter Fault", "Grid Loss", "Over Temperature", "String Current Mismatch", "Communication Error". Mỗi cảnh báo có mức độ ưu tiên (cao, trung bình, thấp).
- Quy trình giám sát: kiểm tra màn hình SCADA mỗi 30 phút trong ca, ghi nhận bất thường vào nhật ký. Nếu có cảnh báo mức cao, phải xác nhận và xử lý trong vòng 5 phút.
- Hệ thống lưu trữ dữ liệu 5 năm, cho phép xuất báo cáo xu hướng. Sử dụng kết nối 4G dự phòng nếu mạng LAN bị gián đoạn.
- Cài đặt ngưỡng cảnh báo: nhiệt độ inverter > 60°C, dòng string chênh lệch > 20% so với trung bình, công suất giảm đột ngột > 10% trong 1 phút.
"""

version = "0.0.1"
