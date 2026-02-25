title = "Kafka Consumer Group"

content = """
Consumer group partition work giữa consumers. Scale horizontally. Mekong
Delta Tech design consumer group cho integration processing.

**Partition Assignment:** Each partition assign to one consumer in group.
Rebalance khi consumer join/leave. Cooperative rebalancing. Minimize
disruption. Sticky assignment.

**Processing:** Consumer process message từ assigned partitions. Order within
partition. Parallel across partitions. Offset commit. Manual vs auto. Commit
after process. Exactly-once với transactional consumer.

**Scaling:** Add consumer đến max partitions. More consumer = idle. Partition
count = max parallelism. Plan partition count. Rebalance cost. Monitor lag.

**Failure:** Consumer crash = rebalance. Uncommitted message reprocessed.
Idempotent. Handle duplicate. Long process = increase session timeout. Don't
block rebalance.
"""  # noqa: E501

version = "0.0.1"
