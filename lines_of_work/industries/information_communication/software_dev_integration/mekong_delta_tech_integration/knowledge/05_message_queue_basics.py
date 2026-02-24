title = "Cơ bản Message Queue"

content = """
Message queue cho phép decoupling giữa producer và consumer, đảm bảo reliability và
khả năng mở rộng. Là công cụ quan trọng trong kiến trúc event-driven.

**Asynchronous Communication:** Producer gửi message không cần chờ consumer xử lý ngay.
Hệ thống có thể xử lý spike và cho phép consumer scale độc lập.

**Delivery Guarantees:** Hiểu rõ at-most-once, at-least-once, exactly-once. Mỗi broker
có trade-off khác nhau. Chọn model phù hợp với business requirement.

**Idempotent Consumers:** Khi dùng at-least-once, consumer phải idempotent. Xử lý message
trùng không được gây side effect (như double charge). Dùng idempotency key.

**Dead Letter Queue (DLQ):** Message failed sau nhiều retry chuyển vào DLQ để audit và
xử lý thủ công. Monitor DLQ size và alert khi tăng đột biến.
"""  # noqa: E501

version = "0.0.1"
