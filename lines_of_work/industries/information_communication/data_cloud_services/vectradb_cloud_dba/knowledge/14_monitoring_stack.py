title = "Observability Stack"

content = """
- Metrics: Prometheus plus VictoriaMetrics long-term storage, 13-month retention.
- Logs: Loki for application and DB logs, retained 30 days hot and 1 year cold in S3.
- Traces: OpenTelemetry instrumentation for slow queries above 1 s, sampled at 10 percent, exported to Tempo.
- Dashboards: per-cluster Grafana with panels for connections, locks, replication lag, cache hit ratio, autovacuum queue, top queries, and checkpoint write time.
- Alert routing: Alertmanager to PagerDuty for SEV1 and SEV2, Slack #dba-alerts for SEV3, email digest for SEV4.
"""  # noqa: E501

version = "0.0.1"
