title = "Tích hợp OAuth2"

content = """
OAuth2 là chuẩn ủy quyền cho API. Mekong Delta Tech dùng OAuth2 khi tích hợp với
các hệ thống bên thứ ba và cung cấp API cho đối tác.

**Grant Types:** Authorization Code cho web app (có redirect). Client Credentials cho
machine-to-machine. Refresh token để lấy access token mới khi hết hạn.

**Token Storage:** Lưu access token và refresh token an toàn. Encrypt at rest. Không
expose trong logs hoặc client-side. Rotate refresh token khi dùng.

**Scope and Permissions:** Định nghĩa scope granular. Client request scope tối thiểu
cần thiết. Server validate scope cho mỗi request. Principle of least privilege.

**Token Validation:** Validate signature (JWT) hoặc introspect với authorization server.
Check expiration, audience, issuer. Cache validation result trong thời gian ngắn.
"""  # noqa: E501

version = "0.0.1"
