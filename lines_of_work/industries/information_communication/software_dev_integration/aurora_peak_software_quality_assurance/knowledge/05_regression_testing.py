title = "Regression Testing and Release Confidence"

content = """
Regression testing verifies that changes do not break existing functionality.
In a fintech context, a single unnoticed regression can cause incorrect
transactions or regulatory violations. We treat regression as a core
quality gate.

**Regression Suite Composition:** The regression suite covers critical
paths: authentication, core transactions, reporting, and integrations.
It grows over time but is regularly pruned to remove obsolete tests.
We aim for high automation of regression to enable fast feedback.

**Execution Timing:** Regression runs on every merge to main and before
each release. Critical paths run first; full suite runs overnight or
in parallel. Flaky tests are fixed or removed — they undermine
confidence in results.

**Baseline and Drift:** We maintain a known-good baseline for performance
and behavior. Significant drift triggers investigation before release.
"""  # noqa: E501

version = "0.0.1"
