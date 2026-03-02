title = "Payment Types Overview"

content = """
Nordstern supports multiple payment methods to serve diverse merchant needs across
the SEPA zone. Each payment type has distinct settlement timing, fees, and use cases.

**SEPA Credit Transfer (SCT):** Standard bank-to-bank transfers within the euro zone.
Typically settles in one business day (T+1). Used for recurring payments, B2B
invoicing, and larger transactions. Lower fees than card schemes. Requires
IBAN and beneficiary details.

**SEPA Instant Credit Transfer (SCT Inst):** Real-time euro transfers, completing
within seconds. Maximum single transaction €100,000. Higher per-transaction fee
than SCT. Ideal for time-sensitive payouts, urgent refunds, and instant wallet
top-ups. Availability depends on beneficiary bank support.

**Card Payments (Visa, Mastercard):** Acquired via partner schemes. Settlement
typically T+1 or T+2 depending on scheme and merchant category. Subject to
interchange and scheme fees. Supports e-commerce, POS, and mobile payments.
Chargeback rights apply; merchants must retain evidence for disputed transactions.

**Digital Wallets:** Integration with Apple Pay, Google Pay, and regional wallets.
Transactions route through underlying card or SEPA rails. Settlement follows the
underlying scheme. Provides streamlined checkout for consumers.

**Direct Debit (SDD):** Pull-based collections from payer accounts. Used for
subscriptions and recurring billing. Requires mandate setup. Longer settlement
and higher return risk than credit transfers.
"""  # noqa: E501

version = "0.0.1"
