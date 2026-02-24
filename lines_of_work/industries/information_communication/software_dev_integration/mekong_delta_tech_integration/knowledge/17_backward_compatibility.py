title = "Tương thích ngược"

content = """
Backward compatibility đảm bảo client cũ vẫn hoạt động khi server update. Quan trọng
cho integration trong ecosystem nhiều bên.

**Schema Evolution:** Thêm optional field an toàn. Không xóa required field. Không đổi
type của existing field. Protocol Buffers và Avro có rules rõ ràng. JSON schema cần
careful.

**Default Values:** Field mới có default. Client cũ không gửi → server dùng default.
Client mới có thể gửi. Đảm bảo default hợp lý và documented.

**Behavioral Changes:** Đổi behavior có thể break client. Version API hoặc feature
flag. A/B test với subset client trước khi roll out. Document behavior change.

**Testing:** Contract testing (Pact, etc) để verify compatibility. Integration test
với client cũ. CI chạy compatibility suite trước release.
"""  # noqa: E501

version = "0.0.1"
