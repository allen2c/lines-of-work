title = "Multi-Currency Accounts"

content = """
Nordstern settlement occurs in EUR. Merchants receiving payments in multiple
currencies receive EUR equivalent based on conversion at settlement.

**Settlement Currency:** All payouts are in EUR. Card transactions in GBP,
CHF, USD, or other currencies are converted using the applicable scheme
or acquirer rate at the time of batch settlement.

**Holding Balances:** Some merchants may have multi-currency ledger
balances within the Nordstern system for internal allocation. Payout
to external bank accounts remains EUR unless a specific multi-currency
product is contracted.

**FX Risk:** Merchants bear foreign exchange risk when accepting
non-EUR payments. Rate applied is the rate at settlement, not at
transaction time. For predictable cash flow, consider dynamic
pricing or hedging strategies.

**Reporting:** Multi-currency transaction reports show both original
currency and EUR equivalent. Reconciliation should use the currency
and rate applicable to the merchant's accounting treatment.
"""  # noqa: E501

version = "0.0.1"
