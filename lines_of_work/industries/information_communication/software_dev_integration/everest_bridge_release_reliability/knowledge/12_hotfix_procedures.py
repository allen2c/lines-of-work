"""Hotfix procedures knowledge item."""

title = "Hotfix Procedures"

content = """
Hotfixes address critical production issues that cannot wait for the next scheduled release.
They follow an accelerated but controlled process to minimize risk while restoring service.

**Triage:** Confirm the issue is production-critical: data loss, security breach, or major
service outage. Non-critical bugs follow the standard release cycle.

**Branch Strategy:** Create a hotfix branch from the production tag or release branch. Do not
branch from develop or feature branches. Ensure the fix is minimal and isolated.

**Expedited Review:** Hotfixes receive priority code review. Focus on correctness and absence
of regressions. Document the rationale for bypassing normal gates if any are skipped.

**Targeted Testing:** Run smoke tests and regression tests for the affected area. Full test
suites may be abbreviated with explicit sign-off. Document what was tested.

**Deployment:** Deploy during the next available window or, for severe incidents, during an
emergency window. Notify stakeholders. Use the same deployment pipeline as regular releases.

**Merge Back:** Merge the hotfix into the main development branch immediately after deployment
to prevent divergence. Update release notes and incident documentation.
"""

version = "0.0.1"
