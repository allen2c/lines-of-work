"""Multi-region release strategy."""

title = "Multi-Region Releases"

content = """
Multi-region deployments require coordination across geographies. Decide order: primary first
or canary region first. Account for data replication lag and cross-region dependencies.
Use feature flags or traffic routing for gradual rollout. Monitor each region post-deploy.
Define region-specific rollback procedures. Document regional constraints (compliance,
latency) that affect release order.
"""

version = "0.0.1"
