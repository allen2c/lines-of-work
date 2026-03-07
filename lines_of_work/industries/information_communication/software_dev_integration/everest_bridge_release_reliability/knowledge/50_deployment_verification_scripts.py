"""Deployment verification scripts and automation."""

title = "Deployment Verification Scripts"

content = """
Automated verification scripts confirm that a deployment succeeded. Run after each
deploy to validate critical paths, configuration, and dependencies.

**Scope:** Health checks, smoke tests, API availability, database connectivity, external
service integration. Focus on high-impact, fast-executing checks. Full regression runs
separately.

**Failure Handling:** If verification fails, treat as deployment failure. Trigger
rollback or alert for manual intervention. Do not mark deployment as successful until
verification passes.

**Maintenance:** Keep scripts in version control. Update when application behavior
changes. Run in CI and in production post-deploy. Document what each check validates.
"""

version = "0.0.1"
