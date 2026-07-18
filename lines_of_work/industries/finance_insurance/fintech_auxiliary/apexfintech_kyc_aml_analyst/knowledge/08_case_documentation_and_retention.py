title = "Case Documentation & Retention Standards"

content = """
- CMS structure: Case header (ID, customer, risk rating, status), Timeline (auto‑logged actions), Evidence vault (documents, screenshots, API logs), Decision log (analyst, reviewer, approver).
- Mandatory artifacts per case: CDD/EDD checklist, screening results, alert enrichment, triage notes, SAR draft (if any), closure memo.
- Retention: Minimum 7 years after relationship end; for SAR‑related cases, 10 years per FinCEN guidance.
- Access control: Role‑based (Analyst RW, Senior Analyst RW, MLRO RWA, Audit RO). Encryption at rest (AES‑256) and in transit (TLS 1.3).
- Audit trail: Immutable log (append‑only) with SHA‑256 hash chaining.
"""  # noqa: E501

version = "0.0.1"
