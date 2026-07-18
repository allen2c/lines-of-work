title = "Position Reconciliation"

content = """
- Compare fund positions (by security, quantity, and market value) against custodian and prime broker records daily.
- Use the firm's position reconciliation system (ApexPos). Import custodian positions, match against internal portfolio accounting system (Advent APX).
- Tolerance: 0 shares for equities, 0.01% for bonds. For derivatives, match notional and margin.
- Common breaks: corporate actions not reflected, trade settlement timing, stock lending recall. Investigate and adjust within 24 hours.
- For breaks >$10,000 market value, escalate to senior operations. For persistent breaks, request a full audit from custodian.
- At month-end, perform a full position reconciliation and sign off by the 3rd business day.
"""  # noqa: E501

version = "0.0.1"
