"""Post-release verification knowledge item."""

title = "Post-Release Verification"

content = """
Post-release verification confirms that a deployment has succeeded and the system behaves as
expected in production. It runs immediately after deployment and before the release is declared
complete.

**Smoke Tests:** Execute a minimal set of critical-path checks: core APIs respond, authentication
works, and primary user flows complete. These tests should run within minutes and surface obvious
failures.

**Health Checks:** Verify that all services report healthy status. Check load balancer targets,
container orchestration health, and dependency connectivity. Unhealthy targets must be investigated
before sign-off.

**Metrics Baseline:** Compare key metrics (latency, error rate, throughput) against pre-release
baselines. Significant drift warrants investigation. Document acceptable variance thresholds.

**Log and Trace Sampling:** Spot-check logs and traces for new errors or anomalies. Correlate with
deployment timestamps to distinguish pre-existing issues from release-induced problems.

**Sign-Off Criteria:** The release is verified when smoke tests pass, health checks are green,
metrics remain within threshold, and no critical errors appear in sampled logs. Document the
verification outcome and timestamp for audit.
"""

version = "0.0.1"
