title = "Capacity Monitoring and Forecasting"

content = """
- Metrics scraped every 15 s via node_exporter and engine exporters, stored in Prometheus, alerted by Alertmanager, visualized in Grafana.
- Key SLOs: CPU p95 below 70 percent, connection pool utilization below 80 percent, disk usage below 75 percent (warn at 70, page at 85), IOPS below 70 percent of provisioned, WAL volume below 4 GB per hour for P1.
- Forecast model: linear regression on the last 14 days of disk growth, projection 14 / 30 / 90 days; flag if any projection exceeds 85 percent within 30 days.
- Quarterly review: present the top 10 over-provisioned clusters (CPU p95 below 20 percent for 30 days) for downsizing, and the top 10 under-provisioned (p95 above 80 percent for 7 days) for upgrade.
"""  # noqa: E501

version = "0.0.1"
