title = "Repayment Schedule Setup"

content = """
- After funding, generate the amortization schedule in LoanOS. Ensure the first payment date is at least 30 days after funding.
- Set up recurring ACH payments if the borrower opted for auto-pay. Confirm the bank account is the same as the funding account.
- For manual payment methods (check, debit card), configure the payment portal with the correct due date and late fee structure.
- Late fee: 5% of the missed payment amount, capped at $25 per occurrence. Apply after a 10-day grace period.
- Notify the borrower via email and secure message of the payment schedule, due dates, and how to make payments.
"""

version = "0.0.1"
