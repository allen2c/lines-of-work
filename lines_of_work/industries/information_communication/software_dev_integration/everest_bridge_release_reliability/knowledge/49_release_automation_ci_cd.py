"""Release automation and CI/CD integration."""

title = "Release Automation CI/CD"

content = """
CI/CD pipelines automate build, test, and deployment stages. Release automation ensures
consistency, reduces human error, and provides auditability. Integrate release gates
into the pipeline.

**Pipeline Stages:** Build, unit test, integration test, artifact creation, staging
deploy, staging validation, production deploy (manual or automated), post-deploy
verification. Each stage can be a gate.

**Gates:** Fail the pipeline on test failure, security scan issues, or approval rejection.
Do not allow manual overrides without documented exception and audit.

**Visibility:** Expose pipeline status to stakeholders. Use dashboards for release
progress. Notify on failure and on successful production deployment.
"""

version = "0.0.1"
