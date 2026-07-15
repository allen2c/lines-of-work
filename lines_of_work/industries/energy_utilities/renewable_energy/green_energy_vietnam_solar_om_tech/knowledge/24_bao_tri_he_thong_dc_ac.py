title = "Bảo trì hệ thống điện một chiều (DC) và xoay chiều (AC)"

content = """
- Hệ thống DC: từ tấm pin đến inverter. Kiểm tra cầu chì DC, đầu nối MC4, cáp DC. Đo điện trở cách điện DC so với đất (megger 1000V) mỗi tháng, yêu cầu > 1 MΩ. Nếu < 0,5 MΩ, tìm điểm rò và cách ly.
- Hệ thống AC: từ inverter đến máy biến áp. Kiểm tra MCCB, contactor, cáp AC. Đo điện trở cách điện AC (megger 500V) mỗi quý, yêu cầu > 5 MΩ. Kiểm tra bảo vệ quá dòng và chạm đất.
- Kiểm tra sóng hài (THD) trên lưới AC bằng máy phân tích chất lượng điện (Fluke 435). THD < 5% theo tiêu chuẩn EVN. Nếu > 5%, cần kiểm tra inverter và bộ lọc.
- Ghi chép kết quả vào sổ bảo trì, cập nhật CMMS. Nếu phát hiện hư hỏng, lập kế hoạch sửa chữa ưu tiên.
"""

version = "0.0.1"
