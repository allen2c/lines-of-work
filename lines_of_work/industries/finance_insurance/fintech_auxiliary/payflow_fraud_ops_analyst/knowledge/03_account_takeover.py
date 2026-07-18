title = "Account Takeover Detection and Response"

content = """
- ATO indicators: login from new device or IP, multiple failed password attempts, sudden change in personal info (email, phone).
- When ATO suspected: immediately place account on temporary hold, send automated email to customer, and initiate verification call.
- Verification steps: ask for last 3 transactions, confirm registered phone via OTP, check device history.
- If confirmed ATO: reset password, revoke all sessions, reverse unauthorized transactions, and file SAR if loss >$5k.
"""  # noqa: E501

version = "0.0.1"
