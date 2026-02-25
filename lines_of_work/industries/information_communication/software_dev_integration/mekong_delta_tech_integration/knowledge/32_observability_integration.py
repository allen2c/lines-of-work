title = "Observability cho Integration"

content = """
Observability (metrics, logs, traces) là must-have cho integration. Không thể
debug production issue mà không có visibility. Mekong Delta Tech standardize
observability cho mọi integration.

**Metrics:** Request count, latency (p50, p95, p99), error rate per endpoint,
downstream dependency latency. RED (Rate, Errors, Duration) cho request. USE
(Utilization, Saturation, Errors) cho resources. Export Prometheus format.

**Distributed Tracing:** Trace request qua services. Span per operation. See
critical path, bottleneck. Jaeger, Zipkin, Tempo. Sample rate cho high traffic.

**Logging:** Structured JSON. Correlation ID. Log level (debug, info, warn, error).
No sensitive data. Centralized (ELK, Loki). Retention policy. Log aggregation
cho search.

**Alerting:** Alert on error rate, latency SLO breach, dependency down. Runbook
cho mỗi alert. Avoid alert fatigue. Escalation path. Test alert regularly.
"""  # noqa: E501

version = "0.0.1"
