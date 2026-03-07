"""Deployment rollback automation for fast recovery."""

title = "Deployment Rollback Automation"

content = """
Automated rollback reduces mean time to recovery when a deployment causes issues. Design
rollback to be as simple and fast as deployment where possible.

**Mechanisms:** Blue-green and canary deployments allow instant traffic shift back. For
rolling deployments, automate revert to previous artifact version. Use infrastructure
as code to redeploy previous known-good state.

**Triggers:** Automated rollback can trigger on health check failure, error rate spike, or
latency degradation. Define thresholds per service. Ensure alerts are tuned to avoid
false positives that cause unnecessary rollbacks.

**Manual Override:** Engineers must be able to trigger rollback manually. Document the
command or button. Log all rollbacks for post-incident analysis.
"""

version = "0.0.1"
