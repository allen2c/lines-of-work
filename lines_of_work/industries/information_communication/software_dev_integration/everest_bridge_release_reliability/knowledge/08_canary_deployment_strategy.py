"""Canary deployment strategy knowledge item."""

title = "Canary Deployment Strategy"

content = """
Canary deployments route a small percentage of traffic to a new version before full
rollout. This limits blast radius if the new version has issues and allows real-world
validation.

**Traffic Split:** Start with a low percentage (e.g. 1–5%) and increase gradually based
on success criteria. Use load balancer or service mesh configuration to control the split.

**Success Criteria:** Define metrics that must hold for the canary to proceed: error rate,
latency, throughput. Automated checks can promote the canary or trigger rollback. Human
review may be required for the final step to full traffic.

**Observability:** Canary and baseline must be distinguishable in metrics and logs. Use
labels, tags, or headers to segment traffic. Compare canary vs. baseline in dashboards.
"""

version = "0.0.1"
