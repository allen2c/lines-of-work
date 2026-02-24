title = "Correlation ID"

content = """
Correlation ID (trace ID) liên kết các log và request qua nhiều service. Essential
cho distributed tracing và debug. Mekong Delta Tech enforce correlation ID cho mọi
integration.

**Propagation:** Client gửi X-Correlation-ID hoặc tạo nếu không có. Mỗi service
propagate header qua downstream call. Pass qua message trong async flow. Same ID
cho toàn bộ request chain.

**Logging:** Mọi log entry include correlation ID. Structured logging (JSON).
Search log bằng correlation ID để see full flow. Link logs từ nhiều service.

**Standards:** W3C Trace Context (traceparent, tracestate). B3 (X-B3-TraceId).
OpenTelemetry. Chọn standard và stick with it. Tương thích với tracing system.

**Debugging:** User report issue → get correlation ID từ response → search logs.
See full request path, latency per service, error location. Reduce MTTR significantly.
"""  # noqa: E501

version = "0.0.1"
