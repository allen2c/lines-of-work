title = "Idempotency Keys"

content = """
Idempotency key cho phép client retry safe. Server trả cached response khi nhận
duplicate key. Bắt buộc cho payment, order placement, và critical operations.

**Client Usage:** Client generate unique key (UUID) per logical operation. Gửi
trong header Idempotency-Key. Same key cho retry. Different key cho new operation.

**Server Handling:** Store (key, response) với TTL (24h). First request với key:
process, cache response, return. Subsequent same key: return cached, không process.
Key scope: per user/account. Cleanup expired.

**Key Requirements:** Uniqueness. Client responsibility. Server reject empty/invalid.
Limit key length. Consider storage — Redis, DB. High QPS = careful design.

**Edge Cases:** Request timeout — client retry same key. Server có thể đã process.
Cached response correct. In-flight: debounce, wait for first complete.
"""  # noqa: E501

version = "0.0.1"
