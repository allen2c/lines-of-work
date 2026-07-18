title = "Transaction Monitoring Alert Generation"

content = """
- Engine: Rule‑based + ML anomaly detection (scores 0‑100). Core rules: (a) Single TX ≥ $10,000; (b) Velocity > 5 TX/hr; (c) Structuring patterns (multiple < $3,000 within 24 h); (d) Geo‑risk (TX to/from FATF high‑risk); (e) Crypto‑fiat conversion > $25,000/day.
- Alert volume: ~1,200 alerts/day; 65 % auto‑closed as low risk (score < 30).
- Alert attributes: Customer ID, timestamp, amount, currency, channel, risk score, rule IDs triggered.
- Enrichment: Auto‑attach KYC profile, latest PEP/sanctions status, adverse‑media flag.
- Queue: High (score ≥ 70) → Senior Analyst within 1 h; Medium (30‑69) → Analyst within 4 h; Low (<30) → auto‑close with log.
"""  # noqa: E501

version = "0.0.1"
