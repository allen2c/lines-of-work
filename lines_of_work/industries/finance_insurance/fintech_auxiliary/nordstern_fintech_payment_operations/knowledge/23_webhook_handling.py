title = "Webhook Handling"

content = """
Webhooks deliver asynchronous notifications for payment events. Proper
handling ensures reliable integration and prevents duplicate processing.

**Event Types:** Common events include: payment.authorized, payment.captured,
payment.failed, refund.completed, chargeback.created. Full list is in the
developer documentation.

**Endpoint Requirements:** Webhook endpoints must be publicly accessible
HTTPS URLs. Respond with 2xx within a short timeout (typically 15–30
seconds). Slow processing should be done asynchronously after acknowledging.

**Signature Verification:** Each webhook includes a signature header. Verify
the signature using your webhook secret before processing. Reject unsigned
or invalid signatures to prevent spoofing.

**Idempotency:** The same event may be delivered multiple times due to
retries. Use the event ID to deduplicate. Process each event ID only once.

**Retry Behavior:** Failed deliveries (non-2xx or timeout) are retried with
exponential backoff. After exhausting retries, events may be available via
a recovery API. Ensure your endpoint is stable to avoid repeated failures.
"""  # noqa: E501

version = "0.0.1"
