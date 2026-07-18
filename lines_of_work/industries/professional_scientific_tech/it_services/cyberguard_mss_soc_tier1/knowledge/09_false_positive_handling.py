title = "False Positive Handling & Documentation"

content = """
- A false positive (FP) is an alert that triggers on legitimate activity (e.g., internal vulnerability scan, scheduled backup, admin remote access).
- Steps to confirm FP: (1) Verify the source IP belongs to an internal asset or known vendor, (2) Check the activity against change management records, (3) Confirm with the asset owner if needed.
- Once confirmed, close the ticket with reason “False Positive – [specific reason]” and add the alert signature to the FP list in the SIEM.
- The FP list is maintained in a shared spreadsheet; each entry includes: alert name, trigger condition, reason, date added, and analyst name.
- If the same FP pattern appears frequently, submit a request to the SIEM team to tune the rule.
"""

version = "0.0.1"
