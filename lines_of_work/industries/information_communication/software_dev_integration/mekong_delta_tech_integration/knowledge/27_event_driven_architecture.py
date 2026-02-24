title = "Kiến trúc Event-Driven"

content = """
Event-driven architecture dùng events để communicate giữa services. Producer publish
event, consumer subscribe. Loose coupling, scalability, audit trail tự nhiên.

**Event vs Command:** Event = đã xảy ra (OrderPlaced). Command = yêu cầu hành động
(PlaceOrder). Event thường broadcast. Command point-to-point. Design event schema
cẩn thận — include aggregate id, timestamp, payload, metadata.

**Event Sourcing (Optional):** Store events thay vì state. Rebuild state bằng replay.
Audit trail built-in. Complex — cần snapshot, compaction. Không phải mọi use case.

**Outbox Pattern:** Tránh dual-write (DB + queue). Write event vào outbox table
trong transaction. Separate process poll và publish. Guarantee exactly-once publish
với transactional outbox.

**Event Schema Evolution:** Version events. Backward compatible changes. Consumer
handle unknown fields. Deprecation process. Schema registry cho Kafka.
"""  # noqa: E501

version = "0.0.1"
