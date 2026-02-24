title = "Message Ordering"

content = """
Ordering: FIFO, partition order, causal. Trade-off với parallelism. Mekong
Delta Tech design partition key cho order need. Same key = same partition =
order. Different partition = no order. Document guarantee. Test. Consumer
handle out-of-order khi cần. Idempotent. Sequence number. Timestamp.
"""  # noqa: E501

version = "0.0.1"
