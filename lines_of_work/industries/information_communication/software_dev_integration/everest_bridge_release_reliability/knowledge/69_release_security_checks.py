"""Release security checks to reduce vulnerability risk."""

title = "Release Security Checks"

content = """
Security checks in the release pipeline catch vulnerabilities before they reach production.
Integrate automated scans and manual review where appropriate.

**Automated Scans:** Dependency scanning (e.g. for known CVEs), container image scanning,
static application security testing (SAST), and dynamic scanning in staging. Fail the
pipeline on critical findings or require explicit override with documented justification.

**Secrets:** Scan for accidentally committed secrets. Use pre-commit hooks and CI checks.
Ensure production secrets are never in code or config repos.

**Manual Review:** For high-risk changes (auth, permissions, data handling), require
security team review. Define criteria for when review is needed. Document review
checklist and sign-off process.
"""

version = "0.0.1"
