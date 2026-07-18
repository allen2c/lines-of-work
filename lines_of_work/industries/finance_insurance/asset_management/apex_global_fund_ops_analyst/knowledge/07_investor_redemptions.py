title = "Investor Redemption Processing"

content = """
- Receive redemption requests (form, signature, and wire instructions) by 12:00 PM EST for same-day NAV. Verify investor signature and account details.
- Check for any redemption gates: if total redemptions in a month exceed 10% of fund NAV, apply pro-rata gate. Notify investors within 1 business day.
- Calculate redemption proceeds = shares redeemed * NAV per share (as of trade date). For funds with equalization, deduct equalization charge.
- Process settlement: wire proceeds to investor's bank account within T+3 (equity funds) or T+5 (illiquid funds). For in-kind redemptions, coordinate with portfolio management.
- Update investor register and send confirmation. For redemptions >$5M, notify senior operations and treasury for cash planning.
- If redemption request is incomplete, return to investor relations for correction. Escalate if not processed by cutoff.
"""  # noqa: E501

version = "0.0.1"
