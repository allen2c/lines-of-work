title = "Endpoint Detection & Response: CrowdStrike Falcon"

content = """
- CrowdStrike Falcon is deployed on all client endpoints; it provides real-time detection and prevention.
- Alerts appear in the Falcon console under “Detections”; each detection has a severity (Low, Medium, High, Critical) and a MITRE ATT&CK technique.
- Common actions: “Contain” (isolate host from network), “Kill Process”, “Quarantine File”, “Add to Blocklist”.
- For Tier-1, you are authorized to contain a host only if the runbook explicitly allows it (e.g., ransomware runbook). Otherwise, escalate.
- To view process tree: click on detection, then “Process Explorer” to see parent-child relationships.
- Always check the “Prevention” tab to see if the endpoint blocked the threat automatically.
"""

version = "0.0.1"
