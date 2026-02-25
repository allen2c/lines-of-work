title = "Tiêu chuẩn AQL trong kiểm tra chất lượng"

content = """
AQL (Acceptable Quality Level) là chuẩn quốc tế dùng để quyết định chấp nhận hay
từ chối lô sản phẩm dựa trên kích thước mẫu và số lỗi cho phép.

**Mức AQL thông dụng:** General inspection: AQL 2.5 cho lỗi major, AQL 4.0 cho
lỗi minor. Final inspection: AQL 1.5 major, AQL 2.5 minor. Khách hàng có thể
yêu cầu AQL chặt hơn (1.0, 0.65) cho hàng cao cấp.

**Lấy mẫu:** Theo bảng AQL (ISO 2859 hoặc tương đương). Kích thước lô quyết định
số mẫu cần kiểm. Random sampling từ toàn bộ lô. Không chọn mẫu theo chủ quan.

**Quyết định:** Nếu số lỗi trong mẫu ≤ Ac (Accept), lô đạt. Nếu ≥ Re (Reject),
lô không đạt. Lô không đạt: sorting 100%, sửa chữa, hoặc từ chối giao hàng.
"""  # noqa: E501

version = "0.0.1"
