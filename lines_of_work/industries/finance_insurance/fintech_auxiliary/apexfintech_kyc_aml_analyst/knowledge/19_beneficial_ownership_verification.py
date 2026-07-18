title = "Beneficial Ownership Verification"

content = """
- Definition: Natural person(s) ultimately owning/controlling ≥ 25 % of voting rights or capital, or exercising control via other means.
- Collection: Corporate onboarding requires BO register extract (or self‑declaration with supporting docs: shareholder register, trust deed).
- Verification: Cross‑check with public registries (UK Companies House, US FinCEN BO registry, EU central registers) – API latency < 2 s.
- Discrepancy handling: If declared BO differs from registry → request notarized resolution; escalate to Senior Analyst if unresolved in 5 business days.
- Ongoing: Re‑verify BO annually or on material change (e.g., share transfer > 10 %).
- Record: BO data stored in encrypted BO module, linked to customer case.
"""  # noqa: E501

version = "0.0.1"
