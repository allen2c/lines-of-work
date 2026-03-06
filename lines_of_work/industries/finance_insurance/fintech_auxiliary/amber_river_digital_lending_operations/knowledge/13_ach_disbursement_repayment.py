title = "ACH Disbursement and Repayment Processing"

content = """
Amber River uses the Automated Clearing House (ACH) network for loan
disbursements and recurring repayment collection. ACH is the standard
electronic fund transfer method for US-based lending.

**Disbursement:** Upon approval and signed agreement, funds are sent via
ACH credit to the borrower's designated bank account. Standard ACH
disbursement typically completes in 1–3 business days. Same-day ACH may
be available for a fee. The borrower must provide a valid routing number
and account number; we verify account ownership before disbursement.

**Repayment Collection:** We initiate ACH debits on the scheduled due
date. Borrowers authorize recurring debits at origination. Failed
payments may be retried per our retry policy; we notify borrowers of
failures and request updated payment information.

**Return Codes:** ACH returns (e.g., insufficient funds, invalid account,
unauthorized) are handled per NACHA rules. We track return rates and
may restrict or suspend future ACH privileges for accounts with
excessive returns.

**Authorization and Revocation:** Borrowers may revoke ACH authorization
at any time by contacting us. Revocation does not cancel the underlying
debt; alternative payment methods must be arranged.

**Timing:** ACH transactions are batch-processed. Cutoff times and
holiday schedules affect availability. We communicate expected
disbursement and debit dates clearly to borrowers.
"""  # noqa: E501

version = "0.0.1"
