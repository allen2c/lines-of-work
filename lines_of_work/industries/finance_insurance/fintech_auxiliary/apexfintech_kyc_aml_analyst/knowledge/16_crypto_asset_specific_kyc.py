title = "Crypto‑Asset Specific KYC Requirements"

content = """
- Onchain analytics integration: Chainalysis Reactor for address clustering, risk scoring (0‑100).
- Wallet verification: Proof‑of‑control via signed message (nonce) for non‑custodial wallets.
- Travel Rule compliance: For TX ≥ $1,000 (or €1,000) collect originator/beneficiary VASP data (name, account, jurisdiction).
- Source‑of‑funds: Require exchange deposit receipts or mining revenue proof for deposits > $10,000.
- Stablecoin monitoring: Track issuer redemption patterns; flag > 5 % daily volume from single user.
- Record retention: Onchain transaction hashes stored alongside off‑chain KYC for 7 years.
"""  # noqa: E501

version = "0.0.1"
