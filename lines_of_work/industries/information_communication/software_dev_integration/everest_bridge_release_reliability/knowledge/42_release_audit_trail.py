"""Release audit trail and traceability requirements."""

title = "Release Audit Trail"

content = """
Every change deployed to production must be traceable. The audit trail links artifacts,
commits, tickets, approvals, and deployment events. This supports compliance, incident
investigation, and rollback decisions.

**Required Data:** For each release: artifact ID, source commit hashes, ticket references,
approver identities, deployment timestamp, target environment, and outcome (success/failure).
Store in a central system (CI/CD, ticketing, or dedicated release tool).

**Retention:** Retain audit records per organizational policy (often 1–2 years). Ensure
immutability: append-only logs, no deletion of deployment history.

**Usage:** Use the audit trail to answer: what changed, when, who approved, and what was
the state before/after. In incident response, correlate deployments with symptom onset.
"""

version = "0.0.1"
