title = "Daily NAV Calculation Process"

content = """
- Gather closing prices from Bloomberg (equities) and IDC (fixed income) by 4:30 PM EST. For illiquid securities, use fair value models approved by the valuation committee.
- Accrue management fees (1.5% annual, daily accrual = AUM * 1.5% / 365), performance fees (20% above high-water mark, accrued monthly), and fund expenses (audit, legal, admin, custody).
- Apply corporate actions: dividends (record date, ex-date), stock splits, and mergers. Adjust share count and cost basis.
- Calculate total fund NAV = (market value of assets + cash + receivables) – (liabilities + accruals). Divide by outstanding shares to get NAV per share.
- Compare to prior day NAV per share. Tolerance: ±0.1%. If variance >0.5%, stop and escalate. If between 0.1% and 0.5%, investigate and document.
- Finalize NAV by 6:00 PM EST. Distribute to fund accounting, investor relations, and the transfer agent.
"""  # noqa: E501

version = "0.0.1"
