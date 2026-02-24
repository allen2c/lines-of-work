title = "Tích hợp WebSocket"

content = """
WebSocket cung cấp full-duplex communication qua một connection. Phù hợp cho real-time
updates, chat, live data. Khác với HTTP request-response.

**Connection Lifecycle:** Handshake HTTP upgrade. Maintain connection. Ping/pong để
keepalive. Graceful close với close frame. Handle reconnection phía client.

**Message Format:** Text hoặc binary. Chuẩn hóa format (JSON). Có message type để
routing. Sequence number cho ordering nếu cần. Idempotency cho critical message.

**Scaling:** WebSocket stateful — sticky session hoặc shared state (Redis) khi có
multiple server. Load balancer cần hỗ trợ WebSocket (connection upgrade).

**Error Handling:** Connection có thể drop. Client implement reconnect với backoff.
Server có thể reject với close code. Handle partial message, frame fragmentation.
"""  # noqa: E501

version = "0.0.1"
