title = "Giao thức gRPC"

content = """
gRPC sử dụng Protocol Buffers và HTTP/2, phù hợp cho high-performance, low-latency
integration giữa các microservices. Được dùng khi REST không đủ hiệu năng.

**Protocol Buffers:** Định nghĩa schema trong .proto files. Compile sang code cho nhiều
ngôn ngữ. Versioning schema cẩn thận — thêm optional fields, tránh xóa hoặc đổi type.

**Streaming:** gRPC hỗ trợ unary, server-streaming, client-streaming, và bidirectional
streaming. Chọn đúng pattern cho use case: real-time updates dùng streaming.

**Interceptors:** Sử dụng interceptors cho logging, metrics, authentication, và retry
logic. Giữ business logic tách khỏi cross-cutting concerns.

**Load Balancing:** Client-side load balancing với health checks. gRPC dùng connection
persistence — đảm bảo load balancer hỗ trợ gRPC hoặc dùng proxy như Envoy.
"""  # noqa: E501

version = "0.0.1"
