"""Deployment validation gates before production promotion."""

title = "Deployment Validation Gates"

content = """
Validation gates are automated checks that must pass before a deployment proceeds to the
next stage or production. They reduce the risk of deploying broken or misconfigured builds.

**Gate Types:** Unit tests, integration tests, security scans, dependency checks, and
build reproducibility. For production, add smoke tests, contract tests, and environment
consistency checks.

**Configuration:** Define gates per stage. Critical gates block progression; advisory
gates may warn but allow override with approval. Document override process and who can
authorize it.

**Feedback:** Surface gate results in the pipeline UI and notifications. Failed gates
should link to logs and remediation guidance. Track gate pass rates over time for
continuous improvement.
"""

version = "0.0.1"
