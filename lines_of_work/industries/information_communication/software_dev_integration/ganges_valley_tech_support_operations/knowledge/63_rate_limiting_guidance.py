title = "Rate Limiting and Throttling Guidance"

content = """
APIs and services enforce rate limits to
ensure fair usage. Exceeded limits cause
429 errors or throttling. Support helps
users understand and work within limits.

**Limit Types:** Per-user, per-IP, or
per-account. Limits may vary by plan.
Document and communicate limits clearly.

**Recovery:** 429 responses often include
Retry-After. Advise users to back off
and retry. For sustained needs, recommend
plan upgrade or contact sales.

**Best Practices:** Batching, caching,
and exponential backoff reduce limit
hits. Link to API best-practice docs.
"""  # noqa: E501

version = "0.0.1"
