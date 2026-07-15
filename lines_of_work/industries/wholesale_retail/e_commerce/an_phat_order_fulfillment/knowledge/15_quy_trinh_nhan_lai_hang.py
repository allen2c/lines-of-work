title = "Quy trình nhận lại hàng hoàn trả"

content = """
- Kho nhận hàng hoàn trả từ khách (qua bưu điện hoặc khách mang trực tiếp). Kiểm tra mã RMA trên kiện hàng.
- Mở kiện, đối chiếu sản phẩm với phiếu hoàn trả. Kiểm tra tình trạng: nguyên vẹn, đầy đủ phụ kiện, không trầy xước.
- Nếu hàng đạt tiêu chuẩn (còn mới 100%), nhập kho trở lại với trạng thái "Hàng hoàn – Sẵn sàng bán lại". Nếu hàng lỗi nhẹ (trầy xước, mất phụ kiện), chuyển sang khu vực "Hàng lỗi – Thanh lý" hoặc "Hàng chờ sửa chữa".
- Cập nhật OMS: đơn hoàn trả chuyển trạng thái "Đã nhận hàng – Chờ hoàn tiền".
- Nếu hàng không đúng với mô tả hoặc thiếu, lập biên bản, chụp ảnh, báo cáo trưởng nhóm để quyết định hoàn tiền một phần hoặc từ chối.
"""

version = "0.0.1"
