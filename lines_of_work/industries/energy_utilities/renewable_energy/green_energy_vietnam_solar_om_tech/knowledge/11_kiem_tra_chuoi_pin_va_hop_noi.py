title = "Kiểm tra chuỗi pin và hộp nối (string & junction box)"

content = """
- Kiểm tra string: đo dòng điện mỗi string bằng ampe kìm DC (Fluke 393) tại combiner box. So sánh với dòng trung bình của các string cùng inverter. Nếu lệch > 20%, string đó có vấn đề (tấm pin hỏng, bóng che, kết nối lỏng).
- Kiểm tra hộp nối (junction box): mở nắp, kiểm tra diode bypass (dùng đồng hồ vạn năng đo thông mạch). Nếu diode bị chập hoặc đứt, thay thế. Kiểm tra kết nối MC4 có bị oxy hóa không, vệ sinh bằng cồn isopropyl nếu cần.
- Đo điện áp hở mạch (Voc) của string: dùng đồng hồ đo DC, so sánh với Voc danh định (tấm pin 450Wp có Voc ~49,5V, string 20 tấm => Voc ~990V). Sai lệch > 5% cần kiểm tra từng tấm.
- Ghi nhận kết quả vào bảng kiểm tra string, cập nhật CMMS.
"""

version = "0.0.1"
