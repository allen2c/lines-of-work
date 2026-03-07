"""Verification after rollback execution."""

title = "Release Rollback Verification"

content = """
After a rollback, verify that the system has returned to a known good state. Do not assume
rollback success; confirm through checks and monitoring.

**Immediate Checks:** Run smoke tests against the rolled-back version. Verify that the
previous release artifacts are active and serving traffic. Check that configuration and
feature flags match the pre-incident state.

**Stability Window:** Monitor for a defined period (e.g. 15–30 minutes) after rollback. Watch
error rates, latency, and user-reported issues. Escalate if anomalies persist.

**Documentation:** Record rollback time, reason, and outcome. Update incident ticket with
verification results. Schedule post-mortem to identify root cause and preventive measures.

**Data Consistency:** If the release included data migrations, assess whether rollback
requires data reversion. Document any manual steps and dependencies.
"""

version = "0.0.1"
