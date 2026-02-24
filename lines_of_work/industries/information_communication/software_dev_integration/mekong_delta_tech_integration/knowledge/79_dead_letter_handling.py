title = "Xử lý Dead Letter"

content = """
Dead letter queue (DLQ) chứa message failed sau retry. Cần process để không
mất data. Mekong Delta Tech có DLQ process cho mọi consumer.

**Flow:** Message fail → retry → exhaust retry → move to DLQ. Original message
preserved. Metadata: error, attempt count, timestamp. Alert on DLQ.

**Inspection:** Dashboard. List DLQ messages. View content. Filter. Search.
Correlation to original. Context. Support investigation.

**Handling Options:** Replay (fix issue, retry). Discard (invalid, poison).
Modify and replay. Manual fix. Escalate. SLA cho DLQ process. Don't let
accumulate.

**Prevention:** Root cause fix. Reduce DLQ. Improve error handling. Better
validation. Circuit breaker. Monitor DLQ rate. Quality metric.
"""  # noqa: E501

version = "0.0.1"
