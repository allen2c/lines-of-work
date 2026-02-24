title = "HTTP Client Best Practices"

content = """
HTTP client configuration ảnh hưởng integration reliability. Mekong Delta Tech
config client đúng cách. Retry, timeout, connection pool.

**Timeout:** Connect timeout, read timeout. Set both. Avoid infinite wait.
Conservative default. Override per request khi cần. Propagate. Document.

**Retry:** Retry transient error. Exponential backoff. Max attempts. Idempotent
only. Don't retry 4xx (except 429). Configurable. Log retry. Metric.

**Connection:** Connection pooling. Keep-alive. Max per host. Connection timeout.
Reuse. Don't create per request. Connection manager. Clean shutdown.

**Security:** TLS verification. Certificate pinning (when appropriate). No
plain HTTP. Validate redirect. Follow redirect limit. Headers. User-Agent.
"""  # noqa: E501

version = "0.0.1"
