title = "Identity Verification Flows"

content = """
Identity verification supports regulatory compliance and fraud prevention.
Different flows apply to merchants vs end customers.

**Merchant Onboarding:** KYC requires verified identity of business
representatives and beneficial owners. We accept government-issued ID
and proof of address. Video identification or qualified trust services
may be used for fully remote onboarding. Enhanced due diligence applies
to high-risk merchants.

**Payout Account Verification:** Before sending payouts to a new bank
account, we may require verification. Common methods: micro-deposit
verification (two small credits, merchant confirms amounts) or
document-based verification (bank statement, signed letter).

**Consumer Verification:** For certain use cases (e.g., high-value
transactions, regulatory requirements), end-customer identity checks
may be needed. Merchants are responsible for collecting and verifying
customer identity when required; Nordstern does not perform end-customer
KYC for most flows.

**Data Retention:** Verification documents and results are retained per
regulatory requirements. Merchants must not store sensitive verification
data longer than necessary.
"""  # noqa: E501

version = "0.0.1"
