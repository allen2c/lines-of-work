title = "Giám sát SCADA – các thông số chính"

content = """
- Màn hình chính hiển thị tổng công suất (MW), sản lượng ngày (MWh), hiệu suất hệ thống (PR – Performance Ratio).
- Theo dõi từng inverter: công suất đầu ra, điện áp DC, dòng DC, nhiệt độ heatsink. Ngưỡng cảnh báo: nhiệt độ >60°C, dòng DC > 110% định mức.
- Tuabin gió: tốc độ gió (m/s), tốc độ rotor (RPM), công suất, góc pitch, nhiệt độ hộp số. Cảnh báo khi rung động > 5 mm/s.
- Trạm biến áp: điện áp phía trung thế (22kV), dòng, tần số, nhiệt độ dầu. Ngưỡng tần số: 49.5-50.5 Hz.
- Cảnh báo thời tiết: bức xạ mặt trời (W/m²), nhiệt độ môi trường, độ ẩm, hướng gió.
- Lưu log SCADA ít nhất 30 ngày, sao lưu hàng tuần.
"""

version = "0.0.1"
