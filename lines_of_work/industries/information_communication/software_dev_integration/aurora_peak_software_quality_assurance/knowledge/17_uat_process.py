title = "User Acceptance Testing (UAT) Process"

content = """
UAT validates that the system meets business requirements from the
user's perspective. Business stakeholders execute scenarios in a
staging environment before production release.

**UAT Planning:** UAT scenarios are derived from acceptance criteria
and user stories. Scenarios represent real-world workflows: happy
paths and key exception flows. We schedule UAT with sufficient
time for execution and defect resolution.

**Environment and Data:** UAT runs in a staging environment that
mirrors production as closely as possible. Test data is prepared
to support the scenarios. Access and credentials are provided
to UAT participants.

**Sign-Off:** UAT completion requires all scenarios passed or
waived. Business sign-off is recorded. Defects found in UAT
are triaged; critical issues block release until fixed.
"""  # noqa: E501

version = "0.0.1"
