title = "Tích hợp GraphQL"

content = """
GraphQL cho phép client yêu cầu chính xác dữ liệu cần thiết, giảm over-fetching và
under-fetching. Phù hợp cho các hệ thống cần linh hoạt và performance cao.

**Schema Design:** Định nghĩa schema rõ ràng với types, queries, và mutations. Sử dụng
description cho mọi field. Tránh nested sâu quá 3-4 levels.

**N+1 Problem:** Sử dụng DataLoader hoặc batching để tránh N+1 query. GraphQL có thể gây
nhiều round-trip nếu không tối ưu.

**Error Handling:** GraphQL trả về 200 OK ngay cả khi có partial error. Errors nằm trong
response body. Chuẩn hóa error format với extensions cho mã lỗi nghiệp vụ.

**Security:** Vô hiệu hóa introspection trong production nếu cần. Giới hạn query depth
và complexity để chống DoS. Validate input cho mọi argument.
"""  # noqa: E501

version = "0.0.1"
