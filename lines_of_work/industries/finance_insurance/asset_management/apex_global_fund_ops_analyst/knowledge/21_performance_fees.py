title = "Performance Fee Calculation"

content = """
- Performance fee is 20% of the fund's net appreciation above the high-water mark (HWM). HWM is the highest NAV per share at which a performance fee was previously paid.
- Calculate at each crystallization date (typically December 31). If current NAV per share > HWM, fee = (current NAV – HWM) * number of shares outstanding * 20%.
- For funds with equalization, use the equalization method to ensure each investor pays a fair share. Maintain equalization credits/debits per investor.
- Accrue performance fee monthly based on the year-to-date appreciation. Reverse if NAV falls below HWM.
- Reconcile performance fee accruals against actual crystallization. Escalate if HWM is incorrectly set or if fee calculation results in a negative amount.
- Ensure performance fee is paid to the management company within 30 days of crystallization.
"""  # noqa: E501

version = "0.0.1"
