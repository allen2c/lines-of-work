title = "Security Pricing and Valuation"

content = """
- Obtain daily closing prices from Bloomberg (equities, ETFs) and IDC (fixed income) by 4:30 PM EST. For mutual funds, use NAV from the fund's administrator.
- For illiquid securities (e.g., private equity, distressed debt), use fair value estimates from the valuation committee. Update monthly or upon material events.
- For derivatives, use mark-to-market from counterparty statements or Bloomberg. For OTC derivatives, obtain valuation from the firm's risk system.
- Validate prices: compare to prior day, check for stale prices (>15 days), and flag outliers (>5% change). If price is missing, use last available and escalate.
- For securities with multiple pricing sources, use the primary source; if unavailable, use secondary and document.
- Reconcile pricing against custodian valuations weekly. For discrepancies >0.5%, investigate and adjust.
"""  # noqa: E501

version = "0.0.1"
