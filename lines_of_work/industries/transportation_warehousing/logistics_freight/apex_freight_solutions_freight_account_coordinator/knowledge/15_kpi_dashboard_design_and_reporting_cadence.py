title = "KPI Dashboard Design and Reporting Cadence"

content = """
- Dashboard built in Power BI, refreshed nightly from TMS data warehouse.  
- Core widgets: OTP/OTD trends (weekly), Cost‑per‑Mile vs. Budget (monthly), Carrier Utilization % (weekly), Spot vs. Contract Mix (monthly), Invoice Accuracy (weekly), Claims Cost (monthly).  
- Distribution: automated email to Account Team (Mon 8 am), Senior Management (Mon 10 am), VP Ops (first business day of month).  
- Drill‑through: click carrier name → detailed scorecard; click lane → rate variance waterfall.  
- Data quality rules: missing GPS > 5 % of loads flags “Data Gap” widget.
"""  # noqa: E501

version = "0.0.1"
