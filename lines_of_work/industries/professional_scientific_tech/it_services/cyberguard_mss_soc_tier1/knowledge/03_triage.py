title = "Alert Triage Steps & Severity Levels"

content = """
- Triage steps: (1) Acknowledge alert, (2) Review alert details (source IP, destination, user, process, timestamp), (3) Check related logs (firewall, proxy, AD), (4) Cross-reference with threat intel, (5) Determine classification.
- Severity definitions:
  - **Low**: Single endpoint, no sensitive data, known benign pattern (e.g., failed login from internal IP).
  - **Medium**: Multiple endpoints or users, potential malware, but no evidence of data loss.
  - **High**: Confirmed malware execution, lateral movement, or credential theft.
  - **Critical**: Ransomware, data exfiltration, or compromise of privileged accounts.
- For Medium and above, always check the asset’s criticality (client-defined asset tags) and prioritize accordingly.
- Document triage findings in the ticket using the standard template: “Alert ID, Source, Action Taken, Verdict, IOCs, Next Steps.”
"""

version = "0.0.1"
