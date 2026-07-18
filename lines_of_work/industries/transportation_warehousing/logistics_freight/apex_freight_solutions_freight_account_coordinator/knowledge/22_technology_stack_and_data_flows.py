title = "Technology Stack and Data Flows"

content = """
- Core TMS: FreightOps v3.2 (cloud, multi‑tenant).  
- Integrations: MacroPoint (GPS), FourKites (visibility), DAT RateView (market rates), Project44 (appointment), EDI 204/214/210 (customer/carrier), QuickBooks Enterprise (AP/AR).  
- Data warehouse: Snowflake; nightly ETL via Fivetran.  
- BI: Power BI embedded in TMS dashboards.  
- Automation: RPA bots for invoice three‑way match (UiPath), tender broadcast (Power Automate).  
- Security: SSO via Okta, role‑based access, data encrypted at rest (AES‑256) and in transit (TLS 1.2).  
- Change management: bi‑weekly release cycle; regression test suite > 90 % coverage.
"""  # noqa: E501

version = "0.0.1"
