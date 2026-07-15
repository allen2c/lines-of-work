title = "Payment Processing"

content = """
- Monitor daily incoming payments via ACH, wire, debit card, and check. Match each payment to the correct loan using the loan ID or reference number.
- Apply payments in the order: fees, interest, principal. For partial payments, allocate proportionally across all outstanding amounts.
- If a payment is received after the due date but within the grace period (10 days), do not assess a late fee. If after grace, apply the late fee automatically.
- For returned ACH (NSF), reverse the payment, assess a $35 NSF fee, and notify the borrower. Update the loan status to "Past Due – NSF".
- Reconcile the daily payment batch with the bank statement. Report any discrepancies > $100 to the finance team.
"""

version = "0.0.1"
