title = "Request Deduplication"

content = """
Client có thể gửi duplicate request (retry, bug). Server dedupe bằng idempotency
key. Mekong Delta Tech implement deduplication cho mutable operations.

**Key Source:** Client provide Idempotency-Key header. UUID. Required cho POST,
PUT, PATCH, DELETE. Optional cho GET (no need). Document. Reject missing khi
required. Validate format.

**Storage:** Store (key, response, status) với TTL. Redis, DB. Per user/tenant
scope. Key collision = same operation. Different client? Scope. Cleanup expired.
Memory/Storage. Configurable TTL.

**Response:** First request: process, store, return. Duplicate: return stored.
Same status, body. Don't process again. 409 Conflict? No, return original.
Idempotent. Client retry get same result.

**Edge Case:** In-flight duplicate. Debounce. Wait first complete. Or reject
concurrent same key. Document. Clear. Test.
"""  # noqa: E501

version = "0.0.1"
