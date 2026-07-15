title = "Tạo lệnh lấy hàng (Pick List)"

content = """
- Sau khi phân loại, hệ thống OMS tự động sinh pick list cho nhân viên kho. Pick list bao gồm: mã đơn hàng, danh sách SKU, số lượng, vị trí kệ (theo zone A/B/C – hàng điện tử nhỏ zone A, gia dụng lớn zone B, phụ kiện zone C).
- In pick list ra giấy hoặc gửi qua thiết bị di động (sử dụng ứng dụng kho). Mỗi pick list tối đa 10 đơn để tối ưu thời gian di chuyển.
- Nhân viên kho quét mã vạch từng SKU để xác nhận lấy đúng hàng. Nếu quét sai, hệ thống báo lỗi và yêu cầu kiểm tra lại.
- Sau khi lấy đủ hàng, nhân viên kho đánh dấu hoàn thành pick list, đơn chuyển sang trạng thái "Đã lấy hàng – chờ đóng gói".
"""

version = "0.0.1"
