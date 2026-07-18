title = "Sanctions Screening Process"

content = """
- Lists: OFAC SDN, EU Consolidated List, UK HM Treasury, UN Security Council, Canada, Australia; updated every 15 min via API.
- Screening points: Onboarding, each transaction ≥ $1,000, periodic batch (nightly) for all active customers.
- Matching logic: Exact name + fuzzy (Jaro‑Winkler ≥ 0.85) + alias/former name; address/ID cross‑check.
- Disposition: True hit → immediate block, generate case AML‑YYYYMMDD‑XXXX, notify MLRO within 30 min. Potential hit → queue for analyst review (max 4 h). False positive → documented with justification, supervisor sign‑off.
- Reporting: OFAC “blocked property” report filed within 10 business days; EU/UK reporting per local timelines.
"""  # noqa: E501

version = "0.0.1"
