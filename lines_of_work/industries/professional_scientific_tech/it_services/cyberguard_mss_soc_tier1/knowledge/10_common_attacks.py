title = "Common Attack Types & Indicators"

content = """
- **Ransomware**: File encryption, ransom note, unusual file extensions (.encrypted, .lockbit), high CPU usage on endpoints.
- **Phishing**: Suspicious sender domains, urgent language, mismatched URLs, attachments with macros.
- **Brute Force**: Multiple failed logins from a single IP across multiple accounts, often followed by a successful login.
- **DDoS**: High volume of traffic from many IPs, targeting a single service, causing latency or outage.
- **Data Exfiltration**: Large outbound data transfers (e.g., >100 MB in 5 minutes), connections to known C2 IPs, use of uncommon protocols (e.g., DNS tunneling).
- **Insider Threat**: Unusual access times, downloading large amounts of data, accessing sensitive folders without business need.
"""

version = "0.0.1"
