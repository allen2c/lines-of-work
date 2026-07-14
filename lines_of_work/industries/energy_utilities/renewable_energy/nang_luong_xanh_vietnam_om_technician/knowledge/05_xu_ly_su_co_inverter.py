title = "Xử lý sự cố inverter"

content = """
- Lỗi thường gặp: quá nhiệt, quá áp DC, mất kết nối lưới, lỗi IGBT, lỗi cảm biến.
- Bước 1: kiểm tra log lỗi trên SCADA, ghi mã lỗi.
- Bước 2: kiểm tra nguồn DC đầu vào (điện áp, dòng), nếu quá áp > 110% Voc max thì kiểm tra string.
- Bước 3: kiểm tra nhiệt độ heatsink, quạt làm mát. Nếu quạt hỏng, thay ngay.
- Bước 4: reset inverter (power cycle). Nếu lỗi tái diễn, thay card điều khiển hoặc IGBT.
- Thời gian xử lý mục tiêu: < 2 giờ đối với inverter ảnh hưởng > 10% công suất.
"""

version = "0.0.1"
