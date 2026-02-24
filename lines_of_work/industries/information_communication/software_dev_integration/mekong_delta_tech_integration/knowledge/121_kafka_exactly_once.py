title = "Kafka Exactly-Once Semantics"

content = """
Exactly-once: process mỗi message đúng một lần. Khó với distributed system.
Kafka transactional producer + consumer. Mekong Delta Tech dùng khi cần.

**Transactional Producer:** Enable idempotence. Transaction. Send trong
transaction. Commit. Abort. Consumer read only committed. Exactly-once
produce. Config.

**Transactional Consumer:** Read-process-write in transaction. Commit offset
với output. Atomic. Single transaction. Or two-phase. Complex. Worth khi
critical. Document. Test.

**Limitation:** Performance. Complexity. Not all use case. At-least-once
+ idempotent consumer often enough. Choose. Document guarantee. Consumer
responsibility. Exactly-once khi business requirement. Otherwise simpler.
"""  # noqa: E501

version = "0.0.1"
