title = "Ticket Escalation to Tier-2"

content = """
- Escalate when: (a) alert severity is High or Critical, (b) multiple hosts affected (≥3), (c) data exfiltration suspected, (d) runbook step fails, (e) client requests escalation, (f) alert involves a privileged account (admin, service account).
- Escalation process: (1) Add a note in ServiceNow with “Escalated to Tier-2” and reason, (2) Tag @tier2-lead in Slack with ticket number and summary, (3) Provide full context: timeline, IOCs, actions taken, runbook output.
- Do not close the ticket; leave it open for Tier-2 to take ownership.
- If Tier-2 does not respond within 15 minutes, escalate to SOC manager via phone.
"""

version = "0.0.1"
