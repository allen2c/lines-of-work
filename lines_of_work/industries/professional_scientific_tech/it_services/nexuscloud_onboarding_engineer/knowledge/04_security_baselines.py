title = "Security Baselines"

content = """
- Default baseline includes: CIS benchmark Level 1 for cloud provider, enforced password policies, MFA for all admin users, encryption at rest (AES-256), TLS 1.2+ for all endpoints.
- Additional controls for Premium/Enterprise: CIS Level 2, GuardDuty/Security Center, vulnerability scanning (weekly), SIEM integration (Splunk/QRadar), and DDoS protection.
- All baselines must be applied before any workload deployment. Exceptions require CISO approval.
- Quarterly review: engineer must verify baseline compliance using NexusCloud Compliance Scanner (tool). Non-compliant resources flagged within 24 hours.
- Customer can request custom baselines (e.g., HIPAA, FedRAMP) - handled by security team, not onboarding engineer.
"""

version = "0.0.1"
