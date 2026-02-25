title = "Webhook Signature Verification Support"

content = """
Webhooks use signatures to verify
authenticity. Failed verification
rejects deliveries. Support
helps users implement correct
verification.

**Documentation:** Provide
signature algorithm, header
name, and verification steps.
Link to developer docs.

**Common Errors:** Wrong secret,
incorrect encoding, or
timing issues. Verify
secret is correctly
configured and not expired.

**Security:** Never share
webhook secrets in ticket.
Use secure channel for
secret rotation guidance.
"""  # noqa: E501

version = "0.0.1"
