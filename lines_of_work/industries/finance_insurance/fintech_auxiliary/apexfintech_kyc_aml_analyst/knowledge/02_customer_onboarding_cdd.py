title = "Customer Onboarding & CDD Process"

content = """
- Trigger: New retail or corporate account creation via API or portal.
- Steps: 1) Collect identity data (full name, DOB, nationality, address, government ID). 2) Verify ID via biometric liveness + OCR (success rate ≥ 98 %). 3) Run sanctions/PEP/adverse‑media screening (real‑time API, timeout 3 s). 4) Assign risk score using weighted model (ID verification 30 %, geography 25 %, product 20 %, transaction volume 15 %, adverse media 10 %). 5) If score ≤ 30 → auto‑approve; 31‑70 → manual CDD review; >70 → EDD queue.
- Documentation: Store verified documents in encrypted blob storage, link to case ID AML‑YYYYMMDD‑XXXX.
- SLA: Complete CDD within 24 h for retail, 48 h for corporate.
"""  # noqa: E501

version = "0.0.1"
