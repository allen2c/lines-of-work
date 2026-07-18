title = "IOC Enrichment Using Threat Intelligence"

content = """
- For any IP, domain, or hash found in an alert, perform enrichment using the following sources in order:
  1. VirusTotal – check detection ratio and community comments.
  2. AlienVault OTX – look for related pulses and tags.
  3. ThreatConnect – internal threat intel feeds and client-specific indicators.
  4. Shodan – for IPs, check open ports and services.
- Document enrichment results in the ticket: “IOC: 1.2.3.4 – VirusTotal 5/70, OTX pulse ‘Emotet C2’, Shodan port 443 open.”
- If enrichment reveals a known malicious indicator, escalate the alert to High severity and execute the relevant runbook.
- For unknown IOCs, add them to a “watchlist” for 30 days; if no further activity, remove.
"""

version = "0.0.1"
