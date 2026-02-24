title = "Quản lý API Key"

content = """
API key là hình thức đơn giản cho machine-to-machine authentication. Phù hợp khi
OAuth2 quá phức tạp cho use case.

**Generation and Storage:** Generate cryptographically random key. Hash trước khi lưu
(giống password). Chỉ show plain key một lần khi tạo. User copy và lưu an toàn.

**Transmission:** Đưa key trong header (X-API-Key, Authorization: Bearer) hoặc query
param. Ưu tiên header — query param có thể lọt vào logs. Luôn dùng HTTPS.

**Rotation:** Cho phép nhiều key active. Rotate định kỳ. Revoke key cũ khi đã migrate.
Grace period để client update. Alert khi key sắp expire.

**Scoping:** Key có thể gắn permission hoặc scope. Rate limit per key. Audit log mọi
request với key identifier. Detect và block abuse pattern.
"""  # noqa: E501

version = "0.0.1"
