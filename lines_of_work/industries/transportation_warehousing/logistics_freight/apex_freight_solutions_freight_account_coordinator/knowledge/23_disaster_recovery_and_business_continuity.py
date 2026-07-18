title = "Disaster Recovery and Business Continuity"

content = """
- RPO: 15 minutes (continuous replication to secondary AWS region).  
- RTO: 4 hours for TMS, 2 hours for GPS/visibility feeds.  
- Failover drill: quarterly tabletop, annual full failover test (last test 2024‑11‑15, passed).  
- Critical personnel: Coordinator, Senior Account Manager, IT Ops Lead – all have VPN and laptop pre‑configured.  
- Communication plan: status page (status.apexfreight.com), Slack #bc‑alerts, customer email blast within 30 min of outage.  
- Data backup: daily snapshots retained 30 days, monthly retained 12 months, yearly retained 7 years.  
- Vendor SLAs: MacroPoint 99.9 % uptime, FourKites 99.5 %; penalties enforced per contract.
"""  # noqa: E501

version = "0.0.1"
