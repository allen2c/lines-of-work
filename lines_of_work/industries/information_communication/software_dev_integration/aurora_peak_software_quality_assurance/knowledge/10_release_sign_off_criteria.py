title = "Release Sign-Off Criteria and Quality Gates"

content = """
A release is approved for production only when all quality gates are met.
Sign-off is the responsibility of the QA lead, with input from developers
and product owners. We never ship known critical or high defects.

**Mandatory Gates:** All planned test cases executed and passed (or
waived with documented justification). No open critical or high defects.
Regression suite green. Performance and security checks completed.
Deployment runbook reviewed and rehearsed.

**Waiver Process:** In rare circumstances, a defect may be waived for
a release. Waivers require documented risk assessment, mitigation plan,
and approval from engineering and product leadership. Waivers are
never granted for data integrity or security issues.

**Post-Release Verification:** After deployment, we run smoke tests
in production to confirm the release is functioning. Any failure
triggers rollback per our incident process.
"""  # noqa: E501

version = "0.0.1"
