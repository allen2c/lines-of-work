title = "Escalation Paths"

content = """
- **First Level**: On-call SRE (you). If you do not acknowledge within 2 minutes, PagerDuty escalates to secondary.
- **Second Level**: Senior SRE on-call (backup). If secondary does not acknowledge within 5 minutes, escalate to SRE manager.
- **Third Level**: SRE Manager (business hours) or Engineering Director (after hours). Contact via phone (listed in PagerDuty).
- **External**: For cloud provider issues, open a support ticket with AWS/GCP/Azure and post the ticket ID in #incidents.
- **Vendor**: For third-party tools (Datadog, PagerDuty, Slack), use their status page and support channels. If critical, escalate to the vendor’s emergency line.
"""  # noqa: E501

version = "0.0.1"
