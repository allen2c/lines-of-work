title = "Protocol Buffers"

content = """
Protocol Buffers (protobuf) là binary serialization format. Compact, fast, có
schema. Dùng cho gRPC, Kafka, internal service communication. Mekong Delta Tech
dùng protobuf cho high-performance integration.

**Schema Definition:** .proto files. Message với fields có number. Number không
đổi khi schema evolve. Compile sang code (protoc). Multiple language support.

**Backward Compatibility:** Thêm optional field: safe. Không dùng số cũ cho field
mới. Không xóa field — deprecate. Không đổi type. reserved keyword cho số đã dùng.

**Encoding:** Binary, compact. Faster và smaller hơn JSON. Nhưng không human-readable.
Debug cần tool. Schema required để decode. Good cho internal, consider JSON cho
public API.

**Versioning:** Field number là identity. Old client ignore unknown field. New
client có default cho missing field. Careful với required — avoid adding.
"""  # noqa: E501

version = "0.0.1"
