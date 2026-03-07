"""Automated deployment verification."""

title = "Deployment Verification Automation"

content = """
Automated verification confirms that a deployment succeeded and the system is healthy. Run
checks immediately after deployment and before marking the release complete.

**Smoke Tests:** Execute critical path tests against the new deployment. Verify core endpoints,
authentication, and database connectivity. Fail fast if any check fails.

**Health Probes:** Use liveness and readiness probes. Ensure new instances are receiving
traffic and responding correctly. Check dependency connectivity (databases, caches, queues).

**Metrics Baseline:** Compare post-deploy metrics to pre-deploy baseline. Alert on significant
drift in error rates, latency, or throughput. Allow configurable thresholds per service.

**Integration:** Wire verification into the deployment pipeline. Block release completion until
all checks pass. Support manual override with documented justification for exceptional cases.
"""

version = "0.0.1"
