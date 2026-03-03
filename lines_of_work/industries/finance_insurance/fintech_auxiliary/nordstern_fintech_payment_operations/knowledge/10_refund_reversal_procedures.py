title = "Refund and Reversal Procedures"

content = """
Refunds return funds to the customer. Reversals undo an authorization or
capture. Correct handling avoids duplicate refunds and chargebacks.

**Card Refunds:** Process refunds via the same channel used for the original
transaction (API, dashboard, or batch file). Refunds post to the same card
within scheme-defined timeframes. Refunds cannot exceed the original
transaction amount. Partial refunds are supported for some use cases.

**Refund Timing:** Process refunds promptly. Delayed refunds are a common
cause of chargebacks — customers dispute when they do not see expected
refunds. Typical processing: 5–10 business days to card, depending on
issuer. Inform customers of expected timing.

**SEPA Reversals:** SCT and SCT Inst support reversal (recall) mechanisms
within defined windows. Outcomes depend on beneficiary bank. For payouts
sent in error, initiate recall immediately and notify the beneficiary
to avoid duplicate payouts.

**Void vs Refund:** Void cancels an uncaptured authorization. Refund returns
funds after capture. Use void when the merchant cancels before shipping
or before capture; use refund after the transaction has settled.

**Documentation:** Retain records of all refunds. Required for chargeback
representment if the cardholder later disputes the original transaction.
"""  # noqa: E501

version = "0.0.1"
