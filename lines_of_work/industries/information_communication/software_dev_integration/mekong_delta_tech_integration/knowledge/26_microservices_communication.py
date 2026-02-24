title = "Giao tiếp Microservices"

content = """
Microservices communicate qua network. Chọn pattern phù hợp ảnh hưởng consistency,
latency, coupling. Sync vs async là quyết định kiến trúc quan trọng.

**Synchronous:** REST, gRPC. Request-response. Đơn giản. Nhưng coupling — client
chờ. Cascade failure risk. Dùng cho read-heavy, cần immediate response. Timeout
và circuit breaker bắt buộc.

**Asynchronous:** Message queue, event bus. Fire and forget. Decoupling. Eventual
consistency. Dùng cho write, notification, batch. Handle duplicate, ordering.

**Hybrid:** Thường kết hợp. Sync cho critical path. Async cho side effect. Saga
pattern cho distributed transaction. Chọn per use case.

**Service Mesh:** Istio, Linkerd handle cross-cutting: retry, timeout, encryption,
observability. Giảm logic trong từng service. Overhead và complexity trade-off.
"""  # noqa: E501

version = "0.0.1"
