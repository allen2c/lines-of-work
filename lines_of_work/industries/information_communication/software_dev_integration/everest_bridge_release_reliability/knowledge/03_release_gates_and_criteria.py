"""Release gates and criteria knowledge item."""

title = "Release Gates and Criteria"

content = """
Release gates are checkpoints that must pass before a release proceeds. They enforce
quality and readiness standards and prevent unsuitable changes from reaching production.

**Pre-merge Gates:** Code review approval, CI passing (build, tests, lint), and branch
protection rules. These gates apply at the pull-request level and prevent broken code
from entering the main branch.

**Pre-deploy Gates:** All automated tests green, security scans passed, performance
regressions within tolerance, and required approvals obtained. Staging must reflect the
exact artifact and configuration intended for production.

**Go/No-Go Criteria:** A final human checkpoint before production deploy. Criteria may
include: no critical open defects, rollback plan confirmed, stakeholders notified,
deployment window approved. Document and enforce these consistently.
"""

version = "0.0.1"
