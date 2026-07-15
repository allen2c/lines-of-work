title = "Quy trình ứng phó sự cố"

content = """
- Phân loại sự cố: Cấp 1 (cảnh báo SCADA, tự xử lý trong 30 phút), Cấp 2 (hỏng inverter, mất string, xử lý trong 2 giờ), Cấp 3 (cháy nổ, mất lưới, tai nạn – xử lý khẩn cấp).
- Quy trình Cấp 1: xác nhận cảnh báo, thực hiện reset hoặc kiểm tra nhanh, ghi nhật ký. Nếu không hết, nâng lên Cấp 2.
- Quy trình Cấp 2: thông báo trưởng ca, lập nhóm xử lý, cách ly thiết bị, sửa chữa hoặc thay thế. Cập nhật tiến độ mỗi 30 phút.
- Quy trình Cấp 3: dừng toàn bộ nhà máy (nếu cần), gọi cấp cứu, báo EVN, báo giám đốc. Sau sự cố, lập biên bản điều tra nguyên nhân và đề xuất phòng ngừa.
"""

version = "0.0.1"
