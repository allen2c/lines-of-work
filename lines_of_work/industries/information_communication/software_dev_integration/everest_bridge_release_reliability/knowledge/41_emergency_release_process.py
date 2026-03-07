"""Emergency release process for critical production fixes."""

title = "Emergency Release Process"

content = """
Emergency releases address critical production issues that cannot wait for the next scheduled
release. Define clear triggers: data loss risk, security vulnerability, major outage, or
regulatory breach. The process must be faster than normal but still controlled.

**Expedited Path:** Use a dedicated emergency branch or hotfix path. Require minimal but
mandatory checks: unit tests, smoke tests, and sign-off from at least one senior engineer.
Document the emergency in the release ticket with root cause and business justification.

**Approval:** Emergency releases may bypass normal approval chains but require post-facto
review. Notify Release Manager and on-call before deployment. Log all steps for audit.

**Rollback:** Ensure rollback is tested or trivial (e.g. config revert). If the fix introduces
new risk, prepare monitoring and rollback plan. Conduct post-incident review within 48 hours.
"""

version = "0.0.1"
