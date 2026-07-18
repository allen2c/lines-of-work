title = "Derivative Operations"

content = """
- Process futures: receive trade confirmations, match, and settle via central counterparty. Monitor margin calls and variation margin.
- For options: exercise or assign at expiration. For OTC options, confirm with counterparty and record premium.
- For swaps (interest rate, credit default, total return): receive confirmations, set up in the risk system, and accrue periodic payments.
- Reconcile derivative positions against counterparty statements daily. For margin calls, ensure cash is transferred within 1 hour.
- For collateral management: post or receive collateral (cash or securities) based on CSA agreements. Revalue collateral daily.
- Escalate if a margin call is not met, if a derivative position is not confirmed, or if a swap payment is missed.
"""  # noqa: E501

version = "0.0.1"
