title = "Funding Disbursement"

content = """
- Before funding, confirm all conditions are met: signed promissory note, verified collateral (if secured), insurance proof (if required), and any other stipulations.
- Initiate ACH transfer for amounts ≤ $50,000; wire transfer for larger amounts. Use the bank account verified during KYC (must match the borrower's name).
- For ACH, set the effective date to the next business day. For wire, process within 2 hours of receiving the funding request.
- Record the transaction ID, amount, and date in LoanOS. Update loan status to "Funded – Active".
- If funding fails (e.g., invalid account number), notify the borrower and request corrected bank details. Place a 48-hour hold.
"""

version = "0.0.1"
