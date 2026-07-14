title = "Quy trình khởi động/dừng hệ thống"

content = """
- Khởi động: kiểm tra trạng thái lưới (tần số, điện áp ổn định), đóng máy cắt trung thế, bật inverter theo thứ tự từng string, theo dõi công suất tăng dần.
- Dừng thường: giảm công suất từ từ, tắt inverter, mở máy cắt, cô lập nguồn DC.
- Dừng khẩn cấp: nhấn nút E-stop, cắt toàn bộ nguồn, báo động.
- Ghi nhật ký thời gian khởi động/dừng, lý do.
- Đối với tuabin gió: khởi động khi gió ổn định >3 m/s, dừng khi gió >25 m/s hoặc có cảnh báo.
"""

version = "0.0.1"
