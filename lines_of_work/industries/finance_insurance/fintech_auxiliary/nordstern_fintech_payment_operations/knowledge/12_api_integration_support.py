title = "API Integration Support"

content = """
Nordstern offers REST APIs for payment initiation, refunds, and retrieval.
Merchants integrate to accept payments programmatically.

**Authentication:** API requests use API keys or OAuth 2.0. Keys are
issued in the partner portal. Never expose keys in client-side code or
public repositories. Rotate keys periodically and on suspected compromise.

**Endpoints:** Base URL and endpoint documentation are in the developer
portal. Sandbox and production environments use different URLs and keys.

**Idempotency:** Payment and refund requests should include idempotency
keys to prevent duplicate processing when retries occur due to timeouts
or network issues.

**Webhooks:** Configure webhooks to receive asynchronous notifications
for payment status changes, refunds, and chargebacks. Verify webhook
signatures to ensure authenticity. Implement idempotent handlers —
the same event may be delivered more than once.

**Rate Limits:** APIs are subject to rate limits. High-volume merchants
should implement backoff and respect retry-after headers. Contact
Technical Integration for limit increases.
"""  # noqa: E501

version = "0.0.1"
