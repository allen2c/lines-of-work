title = "Compliance and Audit Posture"

content = """
- Certifications maintained: SOC 2 Type II annual, ISO 27001 3-year cycle with yearly surveillance, GDPR for EU regions, HIPAA BAA on Enterprise plan in US regions.
- Evidence collection: quarterly access review exported from the IAM portal, monthly vulnerability scan with Tenable, annual penetration test by an external firm.
- Data residency: EU tenant data stays in eu-west-1 and eu-north-1; cross-region replication is opt-in and contractually scoped.
- Right to erasure: PII columns identified via the pii_tags table; erasure script reviewed by Legal, executed by DBA in a legal-hold ticket, with SHA-256 confirmation of removed rows.
- Audit log retention: 7 years for SOX-scoped clusters, 3 years for GDPR-scoped, 1 year for standard.
"""  # noqa: E501

version = "0.0.1"
