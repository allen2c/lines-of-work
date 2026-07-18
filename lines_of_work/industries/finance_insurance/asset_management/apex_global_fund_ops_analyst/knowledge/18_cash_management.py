title = "Cash Management"

content = """
- Monitor daily cash balances across all fund accounts. Ensure sufficient cash for redemptions, expenses, and margin calls.
- Initiate wire transfers for redemptions, expenses, and income distributions. Use the firm's treasury system (ApexTreasury) with dual approval for amounts >$1M.
- Manage overdrafts: if a fund account goes negative, immediately transfer cash from the firm's liquidity facility. Interest charged at SOFR + 2%.
- For FX cash, convert excess foreign currency to base currency weekly to minimize FX risk.
- Reconcile cash movements against bank statements daily. For missing wires, contact the bank and escalate if not resolved within 2 hours.
- Report daily cash position to the treasury team by 10:00 AM EST.
"""  # noqa: E501

version = "0.0.1"
