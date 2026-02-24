title = "REST API best practices"

content = """
REST là giao thức phổ biến nhất cho tích hợp hệ thống. Các best practices sau đảm bảo API
của chúng ta tương thích và dễ tích hợp với đối tác trong khu vực.

**Stateless Design:** Mỗi request chứa đủ thông tin để xử lý. Không lưu session state trên
server giữa các request. JWT hoặc API key trong header cho authentication.

**HATEOAS (Optional):** Khi cần, response chứa links đến các resource liên quan. Giúp client
khám phá API mà không cần tài liệu cứng.

**Filtering and Pagination:** Endpoint list phải hỗ trợ filter (query params) và pagination
(cursor hoặc offset/limit). Mặc định giới hạn page size để tránh overload.

**Rate Limiting:** Triển khai rate limit và trả về header Retry-After khi vượt ngưỡng.
Thông tin rate limit trong response headers (X-RateLimit-*).
"""  # noqa: E501

version = "0.0.1"
