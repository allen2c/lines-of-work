title = "Representment Evidence for Fraud Disputes"

content = """
- For fraud reason codes (Visa 10.4, Mastercard 4837, Discover UA01), the key is proving the cardholder authorized the transaction.
- **Required evidence**: (a) 3DS authentication response (CAVV, ECI, or PARes), (b) AVS match (street and ZIP), (c) CVV match, (d) IP address and device fingerprint matching the cardholder’s known behavior.
- **Best practice**: Include a screenshot of the checkout page showing the cardholder entered CVV and billing address. Also include a transaction receipt with timestamp.
- **If 3DS was not used**: Provide evidence of previous successful transactions from the same cardholder, or a signed contract/agreement.
- **Do not submit**: Only the merchant’s internal notes or generic “customer said it was them” statements.
"""  # noqa: E501

version = "0.0.1"
