title = "American Express Chargeback Process"

content = """
- Amex operates differently: they act as both issuer and network. Chargebacks are called “disputes” and are handled via the Amex SAFE portal.
- Amex does not use standard reason codes; instead they provide a dispute reason (e.g., “Merchandise Not Received”, “Unauthorized Charge”).
- Representment must be submitted within 20 calendar days of the dispute notification. Amex does not offer pre-arbitration; the decision is final.
- Evidence requirements are strict: for unauthorized charges, provide proof of cardholder authentication (3DS) or AVS/CVV match. For service disputes, provide refund policy and communication logs.
- Amex has a “Chargeback Prevention Program” – merchants can enroll to receive alerts before a dispute is filed.
"""  # noqa: E501

version = "0.0.1"
