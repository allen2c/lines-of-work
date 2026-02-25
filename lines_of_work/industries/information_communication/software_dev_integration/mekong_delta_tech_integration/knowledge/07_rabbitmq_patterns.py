title = "Patterns RabbitMQ"

content = """
RabbitMQ cung cấp flexible routing với exchanges và queues. Phù hợp cho complex routing
và workloads không cần retention lâu như Kafka.

**Exchange Types:** Direct (routing key exact match), Topic (pattern match), Fanout
(broadcast), Headers. Chọn type phù hợp với routing requirement.

**Durable and Persistence:** Khai báo queue và message persistent để survive broker restart.
Trade-off: persistence giảm throughput. Cân nhắc cho từng use case.

**Acknowledgments:** Manual ack khi consumer xử lý xong. Reject với requeue=false gửi
message vào DLQ. Prefetch limit để tránh một consumer nhận quá nhiều message chưa xử lý.

**Connection and Channel:** Một connection cho process, nhiều channel cho concurrent
operations. Reuse connection, tạo channel mới cho thread. Implement connection recovery.
"""  # noqa: E501

version = "0.0.1"
