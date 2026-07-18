title = "Basic Incident Response Steps"

content = """
- For confirmed incidents, follow the NIST-based IR process: Preparation, Detection & Analysis, Containment, Eradication, Recovery, Post-Incident.
- As Tier-1, you are responsible for Detection & Analysis and initial Containment (if runbook allows).
- Containment actions: isolate host via CrowdStrike, block IP on firewall, disable user account in AD.
- After containment, document all actions in the ticket and hand over to Tier-2 for Eradication and Recovery.
- Do not attempt to remove malware or restore systems; that is Tier-2/3 responsibility.
"""

version = "0.0.1"
