title = "Loan Agreement Generation"

content = """
- After approval, generate the promissory note and disclosure documents using the template engine in LoanOS. Include all required state-specific disclosures (e.g., right of rescission for home equity loans).
- Verify that the loan amount, interest rate, APR, term, payment schedule, and fees match the approved terms. Any discrepancy must be corrected before sending.
- Send the agreement to the borrower via secure e-signature platform (DocuSign). Set a 7-day expiry for signature.
- If the borrower requests changes (e.g., different payment date), route to underwriting for re-approval. Do not modify the agreement without authorization.
- Once signed, store the executed copy in the loan file and update status to "Conditions – Pending Funding".
"""

version = "0.0.1"
