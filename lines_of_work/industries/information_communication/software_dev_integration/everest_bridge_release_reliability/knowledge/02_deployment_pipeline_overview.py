"""Deployment pipeline overview knowledge item."""

title = "Deployment Pipeline Overview"

content = """
The deployment pipeline automates the path from source code to production. A reliable pipeline
reduces human error, enforces quality gates, and provides an audit trail for every change.

**Stages:** Typical stages include build, unit test, integration test, artifact creation,
staging deployment, acceptance test, and production deployment. Each stage should be
idempotent where possible and fail fast when quality criteria are not met.

**Artifact Flow:** Build once, deploy many. Produce immutable artifacts (e.g. container images,
packages) in early stages and promote the same artifact through environments. Never rebuild
for production from a different commit than what was tested in staging.

**Visibility:** The pipeline should expose status, logs, and duration for each run. Failed
stages must block progression and surface clear error information for remediation.
"""

version = "0.0.1"
