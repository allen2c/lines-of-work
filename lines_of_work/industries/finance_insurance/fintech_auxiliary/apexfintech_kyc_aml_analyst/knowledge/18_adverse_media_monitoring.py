title = "Adverse Media Monitoring Process"

content = """
- Sources: 12,000+ global news outlets, regulator enforcement actions, court filings – aggregated via ComplyAdvantage.
- Frequency: Real‑time push for onboarding; daily batch for existing customers.
- Scoring: Relevance (entity match ≥ 0.9), severity (criminal conviction = 100, civil penalty = 60, negative press = 30), recency (≤ 30 days = +20).
- Threshold: Score ≥ 70 → adverse‑media flag added to customer profile; triggers EDD if not already high risk.
- Analyst review: Validate true relevance, document false positives with source excerpt.
- Refresh: Full re‑screen annually; incremental updates daily.
"""  # noqa: E501

version = "0.0.1"
