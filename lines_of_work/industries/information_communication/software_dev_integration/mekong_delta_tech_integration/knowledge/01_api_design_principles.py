title = "Nguyên tắc thiết kế API"

content = """
Thiết kế API là nền tảng của mọi tích hợp hệ thống. Tại Mekong Delta Tech, chúng ta tuân
thủ các nguyên tắc nhất quán để đảm bảo API dễ sử dụng, mở rộng được, và bảo trì lâu dài.

**RESTful Semantics:** Sử dụng đúng động từ HTTP: GET để đọc, POST để tạo, PUT/PATCH để cập
nhật, DELETE để xóa. Tên tài nguyên dùng danh từ số nhiều (ví dụ: /users, /orders).

**Versioning:** Mọi API phải có phiên bản rõ ràng. Ưu tiên URL versioning (/v1/users) hoặc
Accept header. Không breaking change trong cùng major version.

**Idempotency:** Các thao tác thay đổi dữ liệu quan trọng phải idempotent khi có thể. Client
gửi idempotency key để tránh xử lý trùng khi retry.

**Response Consistency:** Trả về cấu trúc nhất quán: data, pagination meta, và error format
theo chuẩn RFC 7807 khi có lỗi.
"""  # noqa: E501

version = "0.0.1"
