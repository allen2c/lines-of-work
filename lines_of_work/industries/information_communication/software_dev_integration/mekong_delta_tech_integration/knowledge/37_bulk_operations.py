title = "Bulk Operations"

content = """
Bulk API cho phép client gửi nhiều items trong một request. Hiệu quả hơn nhiều
request riêng. Mekong Delta Tech cung cấp bulk endpoint cho high-volume integration.

**Batch Endpoint:** POST /v1/orders/batch. Body chứa array of items. Process
từng item. Response chứa result per item. Partial success — một số succeed,
một số fail. Client handle mixed response.

**Size Limits:** Giới hạn batch size (100-1000 items). Reject khi vượt. Document
limit. Client chunk khi cần. Consider request size limit (payload MB).

**Idempotency:** Bulk với idempotency key. Same key = same result. Retry safe.
Server dedupe. Store result keyed by idempotency key. TTL cho cleanup.

**Error Handling:** Per-item error trong response. Error code và message. Client
retry failed items. Don't fail entire batch cho một item — unless atomic required.
Atomic bulk = transactional, complex, slower.
"""  # noqa: E501

version = "0.0.1"
