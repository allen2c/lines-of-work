title = "Quản lý cảnh báo (Alarm management)"

content = """
- Phân loại: Critical (mất lưới, cháy), Major (giảm công suất >30%), Minor (cảnh báo nhiệt độ, lỗi cảm biến).
- Critical: xử lý ngay, báo động toàn nhà máy, ghi nhận thời gian phản hồi.
- Major: xử lý trong 2 giờ, nếu không khắc phục được thì báo kỹ sư trưởng.
- Minor: xử lý trong ca, ghi vào nhật ký.
- Mỗi cảnh báo có ID, thời gian, mô tả, hành động, kết quả. Lưu trong CMMS.
- Định kỳ rà soát danh sách cảnh báo, tắt những cảnh báo giả (spurious) sau khi xác nhận.
"""

version = "0.0.1"
