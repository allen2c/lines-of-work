title = "Delinquency Monitoring"

content = """
- Run a daily report of all loans with a past due balance. Categorize by days past due (DPD): 1-10, 11-30, 31-60, 61-90, 90+.
- For loans 1-10 DPD: send an automated reminder via secure message and email. No manual action required.
- For 11-30 DPD: review the borrower's payment history and contact information. If no payment after 15 days, escalate to collections.
- For 31-60 DPD: prepare a detailed delinquency note including reason for non-payment (if known), updated income/employment status, and any hardship communication.
- For 61+ DPD: flag for potential charge-off. Notify the credit bureau (if applicable) and prepare loss mitigation options.
"""

version = "0.0.1"
