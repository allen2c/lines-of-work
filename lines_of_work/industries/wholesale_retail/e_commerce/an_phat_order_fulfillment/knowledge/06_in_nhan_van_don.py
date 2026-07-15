title = "In nhãn vận đơn và dán lên kiện hàng"

content = """
- Nhãn vận đơn được tạo từ hệ thống của đối tác vận chuyển (GHN, Viettel Post, GHTK, J&T) thông qua API tích hợp.
- Nhãn bao gồm: mã vận đơn (tracking number), tên người nhận, địa chỉ, số điện thoại, mã đơn hàng nội bộ, mã vạch, trọng lượng, loại dịch vụ.
- In nhãn trên giấy decal nhiệt (kích thước 10x15cm). Dán nhãn ở mặt trên của kiện hàng, không che khuất các nhãn cảnh báo.
- Đối với đơn COD, in thêm nhãn "COD – Thu hộ: [số tiền]" và dán cạnh nhãn vận đơn.
- Kiểm tra kỹ thông tin trên nhãn trước khi dán: địa chỉ, số điện thoại, mã vận đơn phải khớp với đơn hàng. Nếu sai, hủy nhãn và tạo lại.
"""

version = "0.0.1"
