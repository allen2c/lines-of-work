title = "CI Integration for Test Automation"

content = """
Automated tests run as part of our CI pipeline. Every commit triggers
a subset of tests; full regression runs on merge to main. CI integration
ensures fast feedback and prevents regressions from reaching production.

**Pipeline Stages:** Unit tests run first and fastest. Integration tests
follow. API and UI tests may run in parallel or on a separate stage.
Deployment to staging triggers end-to-end smoke tests.

**Failure Handling:** A failed test blocks the pipeline. Developers
receive notifications with failure details and logs. Flaky tests are
quarantined and fixed; we do not allow known flaky tests to block
merges repeatedly.

**Reporting:** CI produces test reports (JUnit, Allure, or similar)
that are archived and linked to builds. We track trends: pass rates,
execution time, and failure categories over time.
"""  # noqa: E501

version = "0.0.1"
