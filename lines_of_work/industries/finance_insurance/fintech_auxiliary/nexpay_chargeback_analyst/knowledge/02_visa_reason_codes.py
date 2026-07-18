title = "Visa Reason Codes – Common Categories"

content = """
- Visa uses numeric reason codes (e.g., 10.4, 13.1, 11.3). Each falls under a category: Fraud, Authorization, Processing Error, or Consumer Disputes.
- **10.4 – EMV Counterfeit Fraud**: Liability shift to issuer if chip was used. Merchant must prove chip transaction or fallback.
- **13.1 – Merchandise/Services Not Received**: Merchant must provide proof of delivery (signed POD or tracking with delivery confirmation).
- **11.3 – Not as Described or Defective**: Requires merchant to show refund policy, customer communication, or return acceptance.
- **12.1 – Late Presentment**: Merchant must prove transaction was submitted within the allowed timeframe (typically 5 days for e-commerce).
- **10.5 – Other Fraud – Card Absent**: Merchant must show 3DS authentication or AVS/CVV match to shift liability.
"""  # noqa: E501

version = "0.0.1"
