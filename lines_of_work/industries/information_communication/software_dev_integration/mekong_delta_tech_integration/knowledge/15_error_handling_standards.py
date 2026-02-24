title = "Chuẩn xử lý lỗi"

content = """
Xử lý lỗi nhất quán giúp client integrate dễ dàng và debug nhanh. Mekong Delta Tech
theo chuẩn RFC 7807 Problem Details cho API response.

**Error Response Structure:** type (URI), title (human), status (HTTP code), detail
(cụ thể), instance (request URI), extension fields cho context nghiệp vụ. Luôn
trả về JSON cho API.

**HTTP Status Codes:** 400 validation, 401 unauthorized, 403 forbidden, 404 not found,
409 conflict, 429 rate limit, 500 server error. Dùng đúng code. Tránh 200 với error
trong body (trừ GraphQL).

**Error Codes:** Mã lỗi nghiệp vụ (INVALID_ORDER_ID, DUPLICATE_ENTRY) để client handle
programmatically. Kèm message cho human. Document tất cả error codes.

**Logging:** Log error với correlation ID. Không log sensitive data. Stack trace
chỉ trong non-prod hoặc qua support channel. Client nhận correlation ID để support.
"""  # noqa: E501

version = "0.0.1"
