"""Deployment automation tools knowledge item."""

title = "Deployment Automation Tools"

content = """
Deployment automation reduces human error, ensures consistency, and enables rapid rollback.
Tools should integrate with the pipeline, support rollback, and provide audit trails.

**Pipeline Integration:** Deployments run as pipeline stages, triggered by successful build
and test. Manual steps are minimized. Credentials and secrets are managed by the pipeline,
not by individuals.

**Idempotency:** Deployment actions should be idempotent. Running the same deployment
twice produces the same result. This supports retries and simplifies rollback.

**Rollback Support:** Tools must support one-command or one-click rollback to a previous
version. Rollback should not require manual artifact retrieval or complex procedures.

**Audit Trail:** Log every deployment: who triggered it, when, what version, from which
pipeline run. Retain logs for compliance and incident review.

**Environment Parity:** Use the same tooling and process across staging and production.
Differences in tooling introduce environment-specific failures. Parameterize environment
differences, not process differences.
"""

version = "0.0.1"
