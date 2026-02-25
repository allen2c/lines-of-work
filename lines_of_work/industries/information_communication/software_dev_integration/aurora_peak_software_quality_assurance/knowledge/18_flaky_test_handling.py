title = "Flaky Test Identification and Resolution"

content = """
Flaky tests pass or fail intermittently without code changes. They
undermine confidence in automation and waste engineering time.
We treat flakiness as a high-priority defect.

**Identification:** CI systems that run tests multiple times can
detect flakiness. We also monitor historical pass rates; a test
that fails occasionally warrants investigation. Developers report
flaky tests when they observe inconsistent behavior.

**Common Causes:** Timing dependencies, shared mutable state,
environment variability, and external service unreliability.
Tests that depend on random data or system time are common
culprits. Fixing often involves making tests deterministic.

**Resolution:** Flaky tests are quarantined (skipped or moved to
a separate suite) until fixed. We do not allow quarantined tests
to remain indefinitely. Root cause analysis guides the fix.
"""  # noqa: E501

version = "0.0.1"
