title = "Post-Investigation Actions"

content = """
- After investigation, update case status: "Confirmed Fraud", "False Positive", "Suspicious - No Action".
- For confirmed fraud: block account, reverse transactions (if within 60 days), file SAR if applicable.
- For false positive: release hold, notify customer, and add to model training data to reduce future false positives.
- For suspicious but inconclusive: place account under monitoring for 30 days, escalate if new activity.
- All actions are recorded in CaseFlow with reason and timestamp.
"""  # noqa: E501

version = "0.0.1"
