title = "Monitoring and Alerting"

content = """
- Deploy NexusCloud Monitoring Agent on all VMs (Linux/Windows). Agent collects CPU, memory, disk, network metrics every 60 seconds.
- Create default dashboards: Overview (resource health), Performance (top 5 metrics), Security (failed logins, open ports). Use Grafana or CloudWatch.
- Alert rules: CPU >80% for 5 minutes, disk >90% for 10 minutes, memory >90% for 5 minutes. Action: send email to ops team, create ticket.
- For Premium/Enterprise: add custom metrics (application-level), integrate with PagerDuty, and set up synthetic monitoring (uptime checks every 5 minutes).
- Alert fatigue reduction: suppress alerts during maintenance windows (defined in runbook). Use deduplication (same alert within 1 hour grouped).
"""

version = "0.0.1"
