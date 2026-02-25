title = "Giao hàng Webhook"

content = """
Webhook cho phép server push event đến client thay vì client poll. Phổ biến cho
notification và real-time sync. Mekong Delta Tech dùng webhook cho đối tác integration.

**Payload and Signing:** Gửi event payload (JSON). Sign với HMAC hoặc shared secret
để client verify authenticity. Header X-Webhook-Signature. Client must verify.

**Retry Logic:** Retry với exponential backoff khi delivery fail (non-2xx). Giới hạn
số lần. Log failure. Có dashboard để xem delivery status và manually retry.

**Idempotency:** Client nhận duplicate có thể. Dùng idempotency key (event_id) để
dedupe. Client respond 200 sớm, process async. Acknowledge trước khi timeout.

**Security:** HTTPS only. Optional authentication (API key, OAuth). Validate client
endpoint trước khi production (verification challenge). Rate limit per client.
"""  # noqa: E501

version = "0.0.1"
