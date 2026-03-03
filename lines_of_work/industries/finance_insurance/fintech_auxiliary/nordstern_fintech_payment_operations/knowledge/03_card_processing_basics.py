title = "Card Processing Basics"

content = """
Nordstern provides card acquiring through partner schemes (Visa, Mastercard) for
merchants who accept card payments online, in-app, or at point of sale.

**Authorization Flow:** Card transactions require authorization before capture.
Authorization checks card validity and available funds. Captured amounts settle
in batches. Uncaptured authorizations expire after scheme-defined periods
(typically 7–30 days depending on channel).

**Settlement Cycles:** Card settlements typically run T+1 or T+2. Funds appear
in the merchant's bank account after scheme processing and nostro reconciliation.
Exact timing depends on merchant category and agreement terms.

**Interchange and Fees:** Card scheme interchange rates vary by card type,
merchant category (MCC), and transaction channel (e-commerce vs POS). Nordstern
pricing includes scheme costs plus a margin. High-risk or high-chargeback
merchants may face differentiated pricing.

**3D Secure (3DS):** Strong Customer Authentication (SCA) under PSD2 requires
3DS for most e-commerce card transactions. Merchants must implement 3DS to
reduce liability shift and chargeback risk. Exemptions exist for low-value,
recurring, and trusted beneficiary transactions.

**Tokenization:** For recurring or stored-card scenarios, merchants should use
tokenization rather than storing raw card numbers. Reduces PCI scope and
improves security.
"""  # noqa: E501

version = "0.0.1"
