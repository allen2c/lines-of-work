title = "Equalization Accounting"

content = """
- For funds with performance fees, use equalization to ensure investors who subscribe or redeem during the performance period pay/receive a fair share of the performance fee.
- When an investor subscribes, calculate an equalization credit: (subscription NAV – HWM) * shares * 20% (if NAV > HWM). Credit reduces future performance fee.
- When an investor redeems, calculate an equalization charge: (redemption NAV – HWM) * shares * 20% (if NAV > HWM). Charge is deducted from redemption proceeds.
- Maintain an equalization ledger per investor. Update after each subscription/redemption and at crystallization.
- At crystallization, the total equalization credits/debits should net to zero. Reconcile against the performance fee accrual.
- Escalate if equalization calculations produce a material imbalance (>$10,000) or if the ledger is not updated in real time.
"""  # noqa: E501

version = "0.0.1"
