title = "gRPC Interceptor"

content = """
Interceptor: middleware cho gRPC. Logging, auth, metrics, retry. Mekong Delta
Tech dùng interceptor cho cross-cutting. Centralize logic.

**Types:** Unary, streaming. Client, server. Both. Chain. Order matter. First
in = outer. Auth before logging. Error handling. Panic recover. Don't block.

**Implementation:** Implement interceptor interface. Call next. Wrap. Add
metadata. Modify context. Return error. Chain builder. Register. Per call,
per RPC. Flexibility.

**Use Cases:** Logging (request, response, duration). Auth (validate, inject).
Metrics (count, histogram). Tracing (span). Retry. Timeout. Rate limit.
Standard. Reuse. Test. Document.
"""  # noqa: E501

version = "0.0.1"
