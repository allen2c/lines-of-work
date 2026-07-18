title = "Cloud Provider Outage Response"

content = """
- If a cloud provider (AWS, GCP, Azure) has a regional outage, check their status page and note the incident ID.
- For multi-region services, failover to another region using the disaster recovery runbook.
- For single-region services, declare SEV1 and follow the incident response process. Notify customers via status page.
- Do not attempt to fix provider-side issues. Focus on mitigating impact (e.g., redirect traffic, use cached data).
- After provider recovery, verify all services are healthy and re-enable any disabled features.
"""  # noqa: E501

version = "0.0.1"
