title = "Logging and Metrics Collection"

content = """
- All services send structured logs to the central logging system (ELK stack). Logs are retained for 30 days.
- Metrics are collected via Prometheus exporters and stored for 90 days. Use Grafana for visualization.
- During an incident, use the log dashboard to search for error patterns. Use query: `service:<name> AND level:error AND timestamp:[now-1h TO now]`.
- For metrics, check the service-specific dashboard for anomalies (spikes, drops).
- If logs or metrics are missing, check the exporter health and the logging pipeline. Escalate to the observability team if needed.
"""  # noqa: E501

version = "0.0.1"
