title = "Tích hợp Apache Kafka"

content = """
Kafka là distributed event streaming platform, phù hợp cho high-throughput, durable
event log. Được dùng rộng rãi tại Mekong Delta Tech cho event-driven integration.

**Topics and Partitions:** Mỗi topic chia thành partitions. Message với cùng partition
key đi vào cùng partition — đảm bảo ordering trong partition. Scale consumer bằng consumer
group.

**Producer Configuration:** acks=all cho durability. retries và idempotence=true để tránh
duplicate. Batching và compression (snappy, lz4) để tăng throughput.

**Consumer Offset:** Kafka lưu offset per partition. Commit offset sau khi xử lý xong.
Chọn enable.auto.commit cẩn thận — manual commit khi cần exactly-once processing.

**Schema Registry:** Dùng Avro hoặc Protobuf với Schema Registry để quản lý schema
evolution. Đảm bảo backward/forward compatibility khi thay đổi schema.
"""  # noqa: E501

version = "0.0.1"
