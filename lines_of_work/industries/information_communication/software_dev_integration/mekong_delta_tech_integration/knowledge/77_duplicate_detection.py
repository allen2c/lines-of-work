title = "Phát hiện trùng lặp"

content = """
Duplicate detection trong integration — message, record, request. At-least-once
delivery có thể duplicate. Idempotent processing cần detect. Mekong Delta Tech
có strategy cho duplicate.

**Detection:** Unique key (business ID, idempotency key). Hash của content.
Store seen keys. TTL. Bloom filter cho large set. Dedupe window. Scope:
per partition, per consumer.

**Processing:** First occurrence: process. Duplicate: skip, return cached,
ack. Don't reprocess. Side effect must be idempotent. Log duplicate for
monitoring.

**Storage:** Redis, DB. Key = dedup key. Value = result or flag. TTL = retention
window. Cleanup. Consider storage cost. High throughput = careful.

**Testing:** Test duplicate scenario. Verify no double process. Load test.
Chaos: duplicate delivery. Verify idempotency. Document behavior.
"""  # noqa: E501

version = "0.0.1"
