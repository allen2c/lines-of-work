"""Dependency management for releases knowledge item."""

title = "Dependency Management for Releases"

content = """
Dependencies (libraries, frameworks, base images) affect release stability. Managing them
systematically reduces surprise failures and security vulnerabilities.

**Version Pinning:** Pin all direct and transitive dependencies to exact versions in the
release artifact. Use lock files (e.g., package-lock, Pipfile.lock) and commit them. Never
deploy with floating versions in production.

**Dependency Updates:** Schedule regular dependency updates. Test updates in isolation before
rolling into a release. Track known vulnerabilities and prioritize patches.

**Compatibility Matrix:** Maintain a matrix of supported dependency versions. Document
incompatibilities and upgrade paths. When upgrading, run full regression and integration
tests.

**Transitive Risk:** Audit transitive dependencies for license and security issues. Use
tooling to detect known vulnerabilities. Escalate critical findings before release.

**Release Cutoff:** At release cutoff, freeze dependency versions. Any dependency change
after cutoff requires a new release or explicit exception with risk assessment.
"""

version = "0.0.1"
