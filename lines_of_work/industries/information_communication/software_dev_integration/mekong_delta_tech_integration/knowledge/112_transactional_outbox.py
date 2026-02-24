title = "Transactional Outbox Pattern"

content = """
Outbox pattern đảm bảo exactly-once publish khi có DB write. Write to outbox
trong transaction. Separate process publish. Mekong Delta Tech dùng cho
event publishing.

**Flow:** Business logic + insert outbox trong same transaction. Commit. Async
process poll outbox. Publish to Kafka. Mark published. Delete hoặc mark. Exactly-once
vì transactional. Order? Process in order. Partition by aggregate.

**Implementation:** Outbox table. Columns: id, aggregate_id, event_type, payload,
created_at, published_at. Index for poll. Batch publish. Idempotent publish
(keyed by id). Cleanup old. Monitor lag.

**Failure:** Publish fail. Retry. DLQ khi exhaust. Don't lose. Process order.
Duplicate? Consumer idempotent. Kafka transactional id. Document. Test.
"""  # noqa: E501

version = "0.0.1"
