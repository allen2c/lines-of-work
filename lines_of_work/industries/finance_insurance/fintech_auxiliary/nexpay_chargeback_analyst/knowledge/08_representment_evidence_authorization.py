title = "Representment Evidence for Authorization Disputes"

content = """
- Authorization disputes occur when the merchant did not obtain proper authorization (e.g., Visa 12.1 – Late Presentment, Mastercard 4840 – Duplicate).
- **For late presentment**: Provide proof that the transaction was submitted within the allowed window (e.g., timestamp of authorization request and settlement).
- **For duplicate processing**: Show that only one transaction was captured, or that the second transaction was a refund.
- **For expired card**: Provide evidence that the card was re-authorized after expiration (e.g., account updater service).
- **General rule**: Always include the original authorization code and the settlement batch report.
"""  # noqa: E501

version = "0.0.1"
