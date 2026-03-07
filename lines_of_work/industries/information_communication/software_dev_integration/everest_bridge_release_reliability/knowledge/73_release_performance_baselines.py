"""Release performance baselines for regression detection."""

title = "Release Performance Baselines"

content = """
Performance baselines establish expected metrics for a release. Comparing post-deploy
metrics against baselines helps detect regressions early.

**Baseline Definition:** Capture latency percentiles (p50, p95, p99), throughput, error
rates, and resource utilization from a stable period before release. Store baselines in
a versioned format tied to the release.

**Comparison:** After deployment, compare metrics over a defined window (e.g. 15–30 min)
against baselines. Define thresholds for acceptable drift. Alert on significant degradation.

**Action:** If baselines are exceeded, investigate before expanding rollout. Correlate
with code changes, configuration, or external factors. Document baseline updates when
intentional performance changes occur.
"""

version = "0.0.1"
