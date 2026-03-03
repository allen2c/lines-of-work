title = "Digital Wallet Operations"

content = """
Nordstern supports digital wallet integrations (Apple Pay, Google Pay, and
regional options) for card-based checkout. Wallets provide a streamlined
experience and can improve conversion.

**How It Works:** Wallet transactions use tokenized card credentials stored
on the device. The underlying payment is a card transaction; settlement
follows card scheme rules. Nordstern receives standard card authorization
and capture flows.

**Merchant Setup:** Merchants must register domain and app identifiers with
Nordstern and configure wallet-enabled payment methods in their integration.
Apple Pay requires a valid Apple Developer account and certificate.

**SCA and Wallets:** Wallet transactions typically satisfy SCA through
device biometrics or device passcode. Merchants benefit from higher
approval rates and liability shift for fraud.

**Refunds:** Refunds for wallet-originated transactions follow standard
card refund procedures. Funds return to the linked card; the customer
sees this in their card statement, not necessarily in the wallet app.

**Regional Availability:** Wallet support varies by country and scheme.
Merchants selling in multiple regions should verify wallet acceptance
for each market.
"""  # noqa: E501

version = "0.0.1"
