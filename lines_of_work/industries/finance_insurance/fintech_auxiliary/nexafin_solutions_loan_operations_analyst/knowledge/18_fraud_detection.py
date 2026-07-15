title = "Fraud Detection"

content = """
- Monitor for red flags: multiple applications with similar data, mismatched IP addresses, synthetic identity patterns (thin credit file + recent SSN issuance).
- Use the fraud scoring module in LoanOS. Scores above 75 (out of 100) require manual review. Scores above 90 must be escalated to the fraud team.
- For suspected identity theft, freeze the application and notify the borrower via secure message. Do not share details of the suspicion.
- If fraud is confirmed, file a Suspicious Activity Report (SAR) with FinCEN within 30 days. Coordinate with the compliance officer.
- Maintain a fraud watchlist of known fraudulent identities and check new applications against it.
"""

version = "0.0.1"
