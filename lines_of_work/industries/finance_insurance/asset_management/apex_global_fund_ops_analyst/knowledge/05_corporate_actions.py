title = "Corporate Actions Processing"

content = """
- Monitor corporate actions via Bloomberg, DTCC, and custodian alerts. Categories: mandatory (dividends, splits) and voluntary (tender offers, rights).
- For dividends: record ex-date, record date, pay date. Input dividend amount and currency. Accrue on ex-date, receive on pay date.
- For stock splits: adjust share count and cost basis. For reverse splits, ensure fractional shares are handled per fund policy (cash in lieu).
- For mergers: process exchange of shares, update security master, and record any cash consideration.
- For voluntary actions: obtain portfolio manager's election by 12:00 PM on election date. Submit to custodian by 2:00 PM. If no election, default to no action.
- Escalate if election deadline is missed. Document all corporate actions in the corporate actions log with supporting evidence.
"""  # noqa: E501

version = "0.0.1"
