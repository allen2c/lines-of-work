title = "Runbook Execution Guidelines"

content = """
- Runbooks are stored in the SOC knowledge base (Confluence) and organized by alert type (e.g., “Ransomware Detection”, “Brute Force Attack”, “Data Exfiltration”).
- Each runbook contains: objective, prerequisites, step-by-step actions, expected outcomes, and escalation criteria.
- Before executing, verify that the alert matches the runbook trigger conditions exactly. If not, do not proceed; escalate to Tier-2.
- Document each step taken in the ticket, including timestamps and any commands run.
- If a runbook step fails (e.g., unable to block an IP via firewall API), escalate to Tier-2 immediately with details of the failure.
- After execution, update the alert status to “Resolved” or “Escalated” and add a summary of actions.
"""

version = "0.0.1"
