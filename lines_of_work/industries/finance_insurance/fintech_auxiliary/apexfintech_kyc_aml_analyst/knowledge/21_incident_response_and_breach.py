title = "Incident Response & Data Breach Procedure"

content = """
- Detection: SIEM alerts, vendor breach notification, internal whistleblower.
- Classification: Level 1 (low – no PII), Level 2 (medium – KYC data exposed), Level 3 (high – SAR/BO data exposed).
- Response team: Analyst (first responder), Senior Analyst (coordinator), MLRO (decision), DPO (privacy), IT Security (containment).
- SLA: Containment ≤ 4 h (Level 2/3); forensic imaging ≤ 24 h; regulator notification ≤ 72 h (GDPR) or 24 h (FinCEN) as applicable.
- Communication: Template breach notice to affected customers within 5 business days post‑containment.
- Post‑incident: Root‑cause analysis within 10 business days; remediation plan tracked in JIRA; lessons learned fed into training.
"""  # noqa: E501

version = "0.0.1"
