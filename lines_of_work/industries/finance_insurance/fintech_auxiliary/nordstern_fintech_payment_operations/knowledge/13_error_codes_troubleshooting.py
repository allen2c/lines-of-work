title = "Error Codes and Troubleshooting"

content = """
API and dashboard operations return error codes to indicate failure reason.
Common codes and resolution steps:

**Authentication Errors (401, 403):** Invalid or expired API key, insufficient
permissions. Verify key validity in the partner portal. Check that the correct
environment (sandbox vs production) is used.

**Validation Errors (400):** Invalid request payload — missing required fields,
incorrect format (e.g., IBAN, amount), or business rule violation. Review the
API reference and error message details. Common issues: decimal precision
exceeding scheme limits, invalid currency codes.

**Rate Limit (429):** Too many requests. Implement exponential backoff. For
sustained high volume, request rate limit increase from Technical Integration.

**Server Errors (5xx):** Nordstern or upstream system issues. Retry with
idempotency key. If persistent, check status page and escalate to Technical
Integration.

**Declined Transactions:** Card declined by issuer — insufficient funds,
blocked card, or issuer fraud rules. Customer must contact their bank.
Do not retry the same card repeatedly; this can trigger further blocks.

**SEPA Rejections:** Invalid IBAN, closed account, or beneficiary bank
rejection. Verify account details with the beneficiary.
"""  # noqa: E501

version = "0.0.1"
