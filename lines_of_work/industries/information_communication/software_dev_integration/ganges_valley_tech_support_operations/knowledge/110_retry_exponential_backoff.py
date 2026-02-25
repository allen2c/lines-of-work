title = "Retry and Exponential Backoff Guidance"

content = """
Transient failures (network, rate
limits) often resolve with retry.
Support advises on retry strategy
and backoff for API clients.

**Transient Errors:** 5xx, timeouts,
429. Retry with backoff is
appropriate. Document product
retry recommendations.

**Exponential Backoff:** Double
delay between retries. Cap
max delay. Reduces thundering
herd during outages.

**Idempotency:** For mutations,
use idempotency keys when
supported. Prevents duplicate
operations on retry. Reference
API docs.
"""  # noqa: E501

version = "0.0.1"
