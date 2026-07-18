title = "Incident Classification Categories"

content = """
- Use the following categories when classifying alerts:
  - **Malware**: Any malicious software (trojan, ransomware, worm).
  - **Phishing**: Social engineering via email, SMS, or voice.
  - **Brute Force**: Repeated failed login attempts.
  - **Lateral Movement**: Unusual network connections between internal hosts.
  - **Data Exfiltration**: Large outbound data transfers to external IPs.
  - **Denial of Service**: DDoS or application-layer attacks.
  - **Policy Violation**: Unauthorized software, access, or data handling.
  - **Unknown**: Insufficient information; escalate to Tier-2.
- Each classification has a corresponding runbook; if none exists, escalate.
"""

version = "0.0.1"
