title = "Chargeback Linkage and Dispute Process"

content = """
- Chargebacks are linked to fraud patterns using shared attributes: merchant ID, device fingerprint, IP address, card BIN.
- Analysts use a linkage tool (LinkFraud) that scores probability of common origin (0-100%). Threshold for investigation: >60%.
- For linked chargebacks, create a consolidated case and recommend blocking the merchant or user account.
- Dispute responses: gather evidence (transaction logs, IP, device) and submit to card network within 10 business days.
"""  # noqa: E501

version = "0.0.1"
