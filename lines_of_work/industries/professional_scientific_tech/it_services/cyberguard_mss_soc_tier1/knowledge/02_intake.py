title = "Alert Intake Process"

content = """
- Alerts arrive from three primary sources: SIEM correlation rules, EDR detections, and user-reported phishing emails.
- SIEM alerts are ingested in real-time; each alert has a unique ID and severity (Low, Medium, High, Critical).
- EDR alerts from CrowdStrike appear in the Falcon console and are mirrored into the SIEM via API.
- Phishing emails are reported by users via a dedicated Outlook add-in that creates a ticket in ServiceNow with the original email attached.
- All alerts must be acknowledged in the SIEM within 2 minutes of generation; unacknowledged alerts trigger an escalation to the shift lead.
- During high-volume periods (e.g., DDoS), use the “batch triage” runbook to group similar alerts.
"""

version = "0.0.1"
