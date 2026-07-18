title = "Investor Subscription Processing"

content = """
- Receive subscription documents (subscription agreement, AML/KYC forms, wire confirmation) from investor relations by 12:00 PM EST for same-day NAV.
- Verify investor identity and AML/KYC status against the firm's compliance database. If incomplete, reject and notify investor relations.
- Calculate number of shares = subscription amount / NAV per share (as of trade date). For funds with equalization, apply equalization credit.
- Update the investor register in the transfer agent system (TA2000). Send confirmation to investor and investor relations.
- For subscriptions after cutoff, apply next business day NAV. For large subscriptions (>$10M), notify portfolio management for liquidity planning.
- Ensure subscription proceeds are received in the fund's bank account before issuing shares. If wire is missing, hold shares until funds clear.
"""  # noqa: E501

version = "0.0.1"
