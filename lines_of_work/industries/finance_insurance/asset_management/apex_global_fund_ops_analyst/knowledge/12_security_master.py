title = "Security Master Setup"

content = """
- When a new security is purchased, create a security master record in the portfolio accounting system (Advent APX).
- Required fields: security name, identifier (CUSIP, ISIN, SEDOL), security type (equity, bond, derivative), currency, country, industry, pricing source (Bloomberg, IDC), and corporate actions flag.
- For bonds, enter coupon rate, maturity date, issue date, and day count convention (30/360, actual/360).
- For derivatives, enter contract terms: expiration, strike, multiplier, underlying asset.
- Validate security master against Bloomberg or other reference data. If discrepancies, correct before trade settlement.
- For private placements or illiquid securities, obtain valuation committee approval and set fair value methodology.
- Maintain a log of all security master changes with date and reason.
"""  # noqa: E501

version = "0.0.1"
