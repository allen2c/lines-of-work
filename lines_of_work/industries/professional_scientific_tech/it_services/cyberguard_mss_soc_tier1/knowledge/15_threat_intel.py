title = "Threat Intelligence Feeds & Integration"

content = """
- CyberGuard MSS subscribes to multiple threat intel feeds: VirusTotal Premium, AlienVault OTX, Recorded Future, and internal feeds from client-specific threat hunts.
- Feeds are integrated into Splunk ES via the Threat Intelligence framework; indicators are automatically matched against incoming logs.
- When enriching an IOC, always check the “Threat Intel” dashboard in Splunk to see if the indicator has been seen before.
- For new IOCs, add them to the “CyberGuard Global Blocklist” after Tier-2 approval.
- Daily threat intel briefings are posted in #threat-intel Slack channel at 08:00 and 20:00; review them for emerging threats.
"""

version = "0.0.1"
