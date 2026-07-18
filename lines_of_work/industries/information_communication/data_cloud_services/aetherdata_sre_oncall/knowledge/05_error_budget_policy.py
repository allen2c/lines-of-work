title = "Error Budget Policy"

content = """
- Each service has an error budget equal to 100% minus the SLO target (e.g., 99.99% availability = 0.01% error budget per month).
- Error budget is consumed by any downtime or degraded performance that violates the SLO.
- If error budget remaining < 20%, all non-emergency deployments are frozen. Only security patches and data loss fixes allowed.
- If error budget is exhausted (0%), the service enters "burnout" mode: all changes require senior SRE approval and a full risk assessment.
- Error budget burn rate is monitored in real-time. If burn rate exceeds 2x monthly budget in 1 hour, escalate to team lead.
- At the end of each month, unused error budget is reset.
"""  # noqa: E501

version = "0.0.1"
