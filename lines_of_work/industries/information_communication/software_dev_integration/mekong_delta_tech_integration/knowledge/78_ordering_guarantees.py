title = "Ordering Guarantees"

content = """
Ordering: FIFO, partition ordering, no ordering. Trade-off với throughput và
complexity. Mekong Delta Tech document ordering guarantee cho mỗi integration.

**Kafka:** Ordering per partition. Same key → same partition → order. Different
partition: no order. Design partition key for order need. Single partition =
strict order, bottleneck.

**Message Queue:** Per-queue FIFO ( RabbitMQ). Or no order (competing consumer).
Choose queue design. Priority queue? Multiple queue for priority?

**API:** Request order không guarantee response order. Async. Client handle.
Correlation. Don't assume. Document. State machine phía client khi cần order.

**Trade-off:** Strict order = lower throughput. Partition = parallelism vs order.
Choose per use case. Payment vs analytics. Document guarantee clearly.
"""  # noqa: E501

version = "0.0.1"
