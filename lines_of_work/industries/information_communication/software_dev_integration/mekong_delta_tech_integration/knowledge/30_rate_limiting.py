title = "Rate Limiting"

content = """
Rate limiting bảo vệ API khỏi abuse và đảm bảo fair usage. Client cần handle rate
limit response và backoff. Integration design phải consider rate limit.

**Strategies:** Fixed window, sliding window, token bucket. Mỗi có trade-off.
Per-IP, per-user, per-API-key. Different limit cho endpoint (read vs write).

**Response:** 429 Too Many Requests. Retry-After header. X-RateLimit-* headers
(limit, remaining, reset). Allow client plan request. Document limit trong API doc.

**Client Handling:** Respect Retry-After. Exponential backoff khi 429. Queue
request khi cần. Batch khi API cho phép. Cache để giảm call. Monitor usage.

**Distributed Rate Limit:** Redis hoặc similar cho shared state. Token bucket
trong Redis. Consistent hashing. Consider rate limit khi design high-throughput
integration.
"""  # noqa: E501

version = "0.0.1"
