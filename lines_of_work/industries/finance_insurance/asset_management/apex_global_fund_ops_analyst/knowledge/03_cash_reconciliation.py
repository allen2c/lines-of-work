title = "Cash Reconciliation"

content = """
- Daily: reconcile fund cash balances against custodian bank statements and prime broker cash accounts. Use the firm's reconciliation tool (ApexRecon).
- Steps: import custodian statement, match opening balance, list all cash movements (trades, dividends, fees, subscriptions/redemptions), compute closing balance.
- Tolerance: $100 per line item. For discrepancies >$1,000, investigate immediately. Common causes: timing differences, missing wires, incorrect fee deductions.
- For FX cash, convert to base currency using the daily spot rate from Bloomberg. Revalue all foreign cash positions at month-end.
- Resolve breaks within 24 hours. If break >$50,000, escalate to senior manager and treasury team. Document root cause in the break log.
"""  # noqa: E501

version = "0.0.1"
