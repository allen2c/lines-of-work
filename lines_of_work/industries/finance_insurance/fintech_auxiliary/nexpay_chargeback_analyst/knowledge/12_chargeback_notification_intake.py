title = "Chargeback Notification Intake"

content = """
- Notifications arrive via the card network portals (VDR, MDR, Amex SAFE, Discover Online) and are also sent by email to the NexPay disputes inbox.
- The analyst must log each notification in the CMS within **2 hours** of receipt. Fields to capture: transaction ID, merchant ID, amount, reason code, card network, deadline date.
- Verify that the transaction is within the merchant’s chargeback protection window (e.g., 120 days for Visa, 120 days for Mastercard).
- If the transaction is outside the window, mark as “invalid” and notify the network immediately.
- For high-value disputes (>$5,000), notify the senior analyst and the merchant’s account manager.
"""  # noqa: E501

version = "0.0.1"
