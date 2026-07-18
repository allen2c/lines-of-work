title = "Monitoring Dashboards (Grafana)"

content = """
- **Main Dashboard**: Shows overall service health, SLO compliance, and error budget for all services.
- **Service-Specific Dashboards**: For each service (e.g., PostgreSQL, Redis, Object Store) – latency, throughput, error rates, resource utilization.
- **Alert Dashboard**: Lists all active alerts with severity, duration, and assigned responder.
- **Capacity Dashboard**: CPU, memory, disk, network per node, with trend lines and 80% threshold markers.
- **Dependency Dashboard**: Health of external dependencies (cloud provider APIs, DNS, CDN).
- All dashboards are refreshed every 30 seconds. Use the `?refresh=30s` parameter.
"""  # noqa: E501

version = "0.0.1"
