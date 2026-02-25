title = "Chiến lược Retry"

content = """
Retry là cần thiết khi tích hợp với hệ thống có transient failure. Chiến lược retry
đúng tránh thất bại không cần thiết và không gây overload.

**Exponential Backoff:** Chờ tăng dần giữa các lỗi: 1s, 2s, 4s, 8s... Cap max delay.
Jitter (random) để tránh thundering herd khi nhiều client retry cùng lúc.

**Retriable vs Non-Retriable:** Chỉ retry transient error (503, timeout, connection
reset). Không retry 4xx (trừ 429 rate limit) hoặc validation error. Idempotent
operations mới retry safe.

**Max Attempts:** Giới hạn số lần retry. Sau đó fail hoặc chuyển DLQ. Circuit breaker
khi failure rate cao — stop retry tạm thời, cho hệ thống recovery.

**Idempotency:** Với non-idempotent operation, dùng idempotency key. Server detect
duplicate và return cached response thay vì execute lại.
"""  # noqa: E501

version = "0.0.1"
