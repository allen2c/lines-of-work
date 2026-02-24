title = "Adapter SOAP sang REST"

content = """
Nhiều hệ thống enterprise cũ dùng SOAP/XML. Adapter chuyển REST/JSON request sang
SOAP call và ngược lại. Cho phép modern client integrate với legacy backend.

**Protocol Translation:** REST request → build SOAP envelope. Map REST params
vào SOAP body. Call SOAP endpoint. Parse SOAP response → REST JSON. Handle
SOAP faults → HTTP error.

**Schema Mapping:** XML schema phức tạp. JSON simpler. Cần mapping rõ ràng.
Nested elements, namespaces, attributes. Use XSLT hoặc code. Round-trip
preserve data. Handle optional elements.

**WS-Security:** SOAP thường có WS-Security (signature, encryption, tokens).
Adapter handle authentication. Extract credentials từ REST request. Propagate
to SOAP. Có thể cần certificate management.

**Performance:** SOAP overhead lớn. Connection pooling. Consider caching
response khi appropriate. Batch SOAP call nếu có. Monitor latency.
"""  # noqa: E501

version = "0.0.1"
