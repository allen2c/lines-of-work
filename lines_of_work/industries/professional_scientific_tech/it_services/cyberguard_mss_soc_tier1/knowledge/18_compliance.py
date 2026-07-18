title = "Relevant Compliance Standards"

content = """
- Clients may be subject to: GDPR, PCI-DSS, HIPAA, SOC 2, ISO 27001.
- For GDPR: if an incident involves personal data of EU residents, notify the SOC manager immediately; do not document PII in tickets (use anonymized references).
- For PCI-DSS: any alert involving cardholder data (e.g., credit card numbers in logs) must be escalated to Tier-2 and the client’s compliance officer.
- For HIPAA: protected health information (PHI) incidents require special handling; follow the “HIPAA Incident Response” runbook.
- All analysts must complete annual compliance training; records are tracked in the LMS.
"""

version = "0.0.1"
