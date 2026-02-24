title = "Đặt tên Metric"

content = """
Metric naming convention. Consistent. Queryable. Mekong Delta Tech follow
Prometheus naming. Integration metrics discoverable.

**Format:** snake_case. Prefix (service_). Name. Unit suffix (_seconds, _bytes).
Descriptive. Don't aggregate in name. Labels cho dimensions. Example:
http_requests_total, http_request_duration_seconds.

**Labels:** Partition dimensions. Don't high cardinality (user_id). Use for
filter, group by. endpoint, method, status. Consistent across services.
Document labels.

**Types:** Counter (monotonic). Gauge (current value). Histogram (distribution).
Summary. Choose correct. Don't misuse. Prometheus best practice.

**Integration:** Downstream call duration. Per dependency. Success/fail. Rate.
Alert from. Dashboard. Standard names. Onboard new metric. Review.
"""  # noqa: E501

version = "0.0.1"
