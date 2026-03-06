title = "Alerting Thresholds"

content = """
Alerts must be actionable and tuned to avoid fatigue. Define thresholds for:
pipeline failures, latency exceedances, data freshness, consumer lag, error
rates. Use severity levels (critical, warning, info). Critical alerts page
on-call; warnings go to Slack. Avoid alerting on transient issues; use
cooldowns and aggregation. Document expected response times per alert type.
Review and adjust thresholds quarterly based on false positive rates. Rhein
Cloud uses PagerDuty for critical alerts; Slack for warnings. Every alert
must have a runbook link.
"""

version = "0.0.1"
