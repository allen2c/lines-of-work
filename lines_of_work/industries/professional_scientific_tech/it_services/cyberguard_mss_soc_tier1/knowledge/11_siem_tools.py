title = "SIEM Platform: Splunk Enterprise Security"

content = """
- Splunk ES is the primary SIEM; it ingests logs from firewalls, proxies, AD, endpoints, and cloud services.
- Key dashboards: “Security Overview”, “Notable Events”, “Risk Analysis”, “Threat Intelligence”.
- Use the “Notable Events” dashboard to view all alerts; filter by status (New, Acknowledged, In Progress, Resolved).
- Common SPL queries: `index=* sourcetype=WinEventLog:Security EventCode=4625` for failed logins; `index=* sourcetype=firewall action=blocked` for blocked traffic.
- To add an IOC to a watchlist: use the “Threat Intelligence” menu, select “Add Indicator”, enter the IOC and expiration (default 30 days).
- If Splunk is slow or unresponsive, check the “Monitoring Console” for resource usage; escalate to SIEM admin if needed.
"""

version = "0.0.1"
