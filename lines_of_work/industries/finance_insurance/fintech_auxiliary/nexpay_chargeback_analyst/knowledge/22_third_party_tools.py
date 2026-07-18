title = "Third-Party Tools (Verifi, Ethoca)"

content = """
- NexPay uses Verifi (Visa) and Ethoca (Mastercard) for chargeback alerts and prevention.
- **Verifi**: Provides real-time alerts when a cardholder initiates a dispute. The merchant can issue a refund before the chargeback is filed, avoiding the fee.
- **Ethoca**: Similar alerts for Mastercard. Also offers a “Collaboration” feature where the merchant can share evidence directly with the issuer.
- The analyst must monitor the Verifi and Ethoca dashboards daily. If an alert appears, notify the merchant immediately.
- For alerts, the merchant has 24 hours to respond. If they issue a refund, the chargeback is cancelled.
- These tools also provide data on friendly fraud patterns.
"""  # noqa: E501

version = "0.0.1"
