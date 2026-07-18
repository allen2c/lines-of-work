title = "Card Testing and Enumeration Attacks"

content = """
- Card testing: fraudsters use small amounts to verify stolen card numbers. Indicators: multiple $0.50-$2 declines, same BIN.
- Enumeration: sequential attempts to guess valid card numbers. Detected by high decline rate (>80%) on same merchant.
- Response: block the IP and device immediately, flag the merchant for review, and notify card network.
- Prevention: implement CAPTCHA after 3 failed attempts, require CVV for all transactions.
"""  # noqa: E501

version = "0.0.1"
