title = "Mastercard Reason Codes – Key Codes"

content = """
- Mastercard uses numeric codes like 4837, 4853, 4849. They are grouped by chargeback reason.
- **4837 – No Cardholder Authorization**: Fraud claim. Merchant must provide proof of cardholder authentication (e.g., 3DS, tokenization).
- **4853 – Not as Described or Defective**: Similar to Visa 11.3. Evidence includes product description, photos, and customer complaint history.
- **4849 – Merchandise Not Received**: Requires proof of delivery with signature or tracking showing “delivered”.
- **4840 – Duplicate Processing**: Merchant must show that only one transaction was submitted.
- **4863 – Cardholder Does Not Recognize**: Often friendly fraud. Merchant can provide transaction details (IP, device, account history).
"""  # noqa: E501

version = "0.0.1"
