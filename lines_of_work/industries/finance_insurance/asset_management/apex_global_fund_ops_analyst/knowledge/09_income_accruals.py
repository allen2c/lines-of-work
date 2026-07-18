title = "Income Accruals"

content = """
- Accrue interest income on fixed income securities daily using the effective interest method. For bonds, accrue coupon interest from last coupon date to valuation date.
- Accrue dividend income on equities on ex-date. For dividends declared but not yet paid, record a receivable.
- For amortization/accretion: for bonds purchased at a premium or discount, amortize/accrete the difference over the remaining life using the constant yield method.
- For income from securities lending, accrue based on daily lending revenue reports from the lending agent.
- Reconcile accrued income against actual receipts monthly. Investigate any variance >$1,000.
- At month-end, reverse and re-accrue all income accruals to ensure proper period cut-off.
"""  # noqa: E501

version = "0.0.1"
