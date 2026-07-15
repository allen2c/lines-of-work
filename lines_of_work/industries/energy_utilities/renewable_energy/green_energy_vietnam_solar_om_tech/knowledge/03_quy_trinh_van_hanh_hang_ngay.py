title = "Quy trình vận hành hàng ngày"

content = """
- Đầu ca: đăng nhập SCADA, kiểm tra trạng thái toàn bộ inverter (online/offline/error), ghi nhận sản lượng đêm trước. Kiểm tra nhật ký ca trước và các công việc đang dang dở.
- Trong ca: giám sát SCADA định kỳ, thực hiện kiểm tra thực địa 2 lần/ca (sáng 8h, chiều 14h) gồm: kiểm tra inverter, combiner box, tủ điện, không có dấu hiệu bất thường (rò rỉ, tiếng ồn, mùi khét).
- Cuối ca: tổng hợp sản lượng ngày, ghi chép sự cố đã xử lý, cập nhật tình trạng thiết bị vào CMMS, bàn giao cho ca sau bằng văn bản và trao đổi trực tiếp.
- Báo cáo hàng ngày gửi trưởng ca và giám đốc nhà máy trước 17h, bao gồm: sản lượng, số inverter lỗi, thời gian dừng, công việc bảo trì đã thực hiện.
"""

version = "0.0.1"
