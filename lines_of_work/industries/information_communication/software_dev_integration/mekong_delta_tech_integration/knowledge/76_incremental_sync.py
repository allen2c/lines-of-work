title = "Incremental Sync"

content = """
Incremental sync chỉ sync thay đổi, không full reload. Hiệu quả cho large
dataset. Mekong Delta Tech dùng incremental cho nhiều integration.

**Mechanism:** Watermark (max updated_at). Change data capture (CDC). Event
log. Cursor. Sync since last success. Idempotent. Resume from checkpoint.

**Challenges:** Deleted records (soft delete, tombstone). Out-of-order updates.
Initial load vs incremental. Schema change. Clock skew. Handle edge case.

**Implementation:** Query WHERE updated_at > last_sync. Paginate. Commit
checkpoint after batch. Fail = retry from last checkpoint. Don't skip. Verify
count. Reconciliation với full occasionally.

**Partner API:** Polling with since param. Webhook for change. Both. Document
incremental support. Rate limit consideration. Backfill capability.
"""  # noqa: E501

version = "0.0.1"
