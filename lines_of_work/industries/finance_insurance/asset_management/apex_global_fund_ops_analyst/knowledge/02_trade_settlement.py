title = "Trade Settlement and Matching"

content = """
- Receive trade confirmations from brokers (via Bloomberg or email) by 6:00 PM trade date. Match against internal trade blotter from portfolio management.
- Key fields: security identifier (CUSIP/ISIN), trade date, settlement date, quantity, price, commission, net amount.
- For equity trades, settlement is T+2; for fixed income, T+1 or T+2 per market convention. For FX forwards, settlement on value date.
- If trade does not match, contact broker within 1 hour of market close. Common mismatches: price, quantity, commission. Resolve by T+1 morning.
- Monitor DVP settlement via custodian reports. If fail occurs, log in ApexOps, request penalty interest (if counterparty fails) per ISDA master agreement.
- Escalate to senior operations if fail persists beyond T+3. For fails due to internal error, correct and implement preventive controls.
"""  # noqa: E501

version = "0.0.1"
