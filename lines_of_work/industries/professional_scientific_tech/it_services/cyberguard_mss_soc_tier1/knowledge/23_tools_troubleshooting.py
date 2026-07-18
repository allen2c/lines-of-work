title = "Common Tool Issues & Troubleshooting"

content = """
- **Splunk slow**: Check “Monitoring Console” for CPU/memory; if >80%, restart search head via admin. If not resolved, escalate to SIEM admin.
- **CrowdStrike agent offline**: Verify endpoint is powered on; check Falcon console for last seen timestamp. If offline >30 min, notify client IT via SOC manager.
- **Proofpoint not blocking**: Check policy rules; ensure blocklist entry is active. If still not blocking, escalate to email security team.
- **ServiceNow ticket not updating**: Refresh page; if persists, clear cache or use incognito mode. Report to IT if issue continues.
- **Slack outage**: Use phone or email for critical communications; refer to the “Outage Runbook”.
"""

version = "0.0.1"
