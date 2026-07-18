title = "Alert Triage Categories"

content = """
- **SEV1**: Complete service outage (e.g., all database clusters unreachable, data loss). Response time: immediate, resolution within 1 hour.
- **SEV2**: Significant degradation (e.g., p99 latency > 5 seconds for a major customer, 10%+ error rate). Response: within 5 minutes, resolution within 4 hours.
- **SEV3**: Minor degradation (e.g., single node down, non-critical feature broken). Response: within 30 minutes, resolution within 24 hours.
- **SEV4**: Informational (e.g., disk usage > 70%, certificate expiring in 30 days). Response: within 4 hours, resolution within 7 days.
- Use the alert severity matrix in the runbook repository (runbooks.aetherdata.io/severity) for edge cases.
- If unsure, classify as SEV2 and escalate if needed.
"""  # noqa: E501

version = "0.0.1"
