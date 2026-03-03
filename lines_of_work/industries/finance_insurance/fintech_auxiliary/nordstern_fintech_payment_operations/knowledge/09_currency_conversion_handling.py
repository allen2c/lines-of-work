title = "Currency Conversion Handling"

content = """
Nordstern primarily processes EUR-denominated payments within SEPA. Multi-currency
scenarios require clarity on who converts and when.

**Card Multicurrency:** When a customer pays in a currency different from the
merchant's settlement currency, conversion can occur at the issuer (cardholder's
bank) or the acquirer. Merchants can choose Dynamic Currency Conversion (DCC)
to present prices in the cardholder's currency — the merchant or a DCC provider
sets the rate; cardholder sees local currency at checkout.

**Settlement Currency:** Nordstern settles in EUR. Non-EUR card transactions
are converted at the scheme rate (or acquirer rate) at settlement. Merchants
selling in GBP, CHF, or other currencies receive EUR equivalent in their
settlement account.

**SEPA Scope:** SEPA schemes are EUR-only. Payments to or from non-EUR
accounts use correspondent banking or alternative rails, not SEPA.

**Transparency:** Merchants must disclose currency conversion and applicable
margins to customers per PSD2 and consumer protection rules. Hidden fees
or misleading exchange rate presentation can trigger complaints and
regulatory scrutiny.
"""  # noqa: E501

version = "0.0.1"
