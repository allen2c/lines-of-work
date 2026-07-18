title = "Technology Stack & Tooling"

content = """
- Core CMS: proprietary “ComplianceHub” (React front‑end, PostgreSQL, Kubernetes). Version 3.4.1.
- Screening APIs: World‑Check (PEP/Sanctions), ComplyAdvantage (Adverse Media), Dow Jones (Watchlist). Rate limits: 5,000 req/min.
- Transaction Monitoring: “SentinelML” (Python/Scikit‑learn models, retrained monthly). Model versioning in MLflow.
- SAR Generation: “SARBuilder” micro‑service (FinCEN XML schema v1.2). Auto‑populates from case data.
- Document Vault: AWS S3 with Object Lock (WORM) for 10‑year retention.
- Identity Verification: “IDCheck” (biometric liveness, OCR, NFC chip read). SLA 99.9 % uptime.
- Monitoring & Alerting: Datadog dashboards for alert volume, SLA breach, API latency.
"""  # noqa: E501

version = "0.0.1"
