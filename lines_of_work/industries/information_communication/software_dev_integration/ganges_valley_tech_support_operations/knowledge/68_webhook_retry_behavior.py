title = "Webhook Retry and Delivery Guarantees"

content = """
Webhooks may fail due to timeouts,
errors, or recipient unavailability.
Products typically retry with
exponential backoff. Support explains
this behavior to users.

**Retry Policy:** Document retry
intervals, max attempts, and
dead-letter handling. Different
products have different policies.

**Troubleshooting:** Check delivery
logs for status codes and response.
4xx indicates recipient configuration;
5xx may trigger retries. Advise on
idempotency and acknowledgment.

**Manual Retry:** Some products allow
manual webhook resend. Guide users
when appropriate.
"""  # noqa: E501

version = "0.0.1"
