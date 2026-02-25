title = "Requirements Traceability for Audits"

content = """
Regulatory and internal audits require evidence that requirements are
tested and results recorded. Traceability links requirements to test
cases and test results, forming a complete chain.

**Traceability Matrix:** We maintain a matrix mapping requirement IDs
to test case IDs. Each requirement has at least one test; each test
covers at least one requirement. Gaps or orphan tests are reviewed
and resolved.

**Test Case Identification:** Test cases have unique IDs and are stored
in our test management system. Execution results (pass/fail, date,
tester) are recorded and retained for audit periods.

**Coverage Reporting:** We report coverage as the percentage of
requirements with at least one passed test. Coverage targets are
set per release; 100% coverage of regulatory requirements is
mandatory before sign-off.
"""  # noqa: E501

version = "0.0.1"
