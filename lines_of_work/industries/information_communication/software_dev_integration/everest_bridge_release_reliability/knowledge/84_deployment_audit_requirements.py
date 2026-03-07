"""Deployment audit requirements for compliance and traceability."""

title = "Deployment Audit Requirements"

content = """
Audit requirements ensure that every deployment is traceable for compliance, security, and
incident investigation. Capture who, what, when, and why for each production change.

**Required Fields:** Deployment ID, timestamp, artifact version, deployer identity, approval
chain, and change description. Link to ticket or release document. Store in immutable log.

**Retention:** Retain audit records per organizational and regulatory policy (e.g. 1–7 years).
Ensure records are tamper-evident and accessible for audits.

**Access Control:** Restrict audit log modification. Grant read access to compliance, security,
and release teams. Use separate storage or append-only systems where possible.

**Integration:** Emit audit events from the deployment pipeline. Include pre-deploy and
post-deploy state. Support querying by date, service, or release for incident analysis.
"""

version = "0.0.1"
