title = "Credit Decision Rules"

content = """
- For loans ≤ $10,000: auto-approve if credit score ≥ 680, DTI ≤ 43%, and no AML hits. Otherwise, route to underwriting.
- For loans > $10,000: always route to underwriting. Prepare a credit package with verified income, credit report, and collateral valuation (if secured).
- Ensure credit report is pulled only after obtaining written consent (e-signature accepted). The report must be no older than 30 days.
- If the applicant has a prior loan with NexaFin, check the repayment history. Any 60+ day delinquency in the last 12 months triggers a manual review.
- Document the decision rationale in LoanOS. For auto-approved loans, set status to "Approved – Pending Conditions".
"""

version = "0.0.1"
