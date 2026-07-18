title = "Disaster Recovery Strategy"

content = """
- Recovery tiers: Tier 1 (P1, cross-region async replica, RTO 1 h, RPO 5 min), Tier 2 (P2, in-region replicas only, RTO 4 h, RPO 1 h), Tier 3 (P3, in-region single replica, RTO 24 h, RPO 24 h).
- DR sites: us-west-2 for us-east-1, eu-west-1 for eu-north-1, ap-southeast-2 for ap-southeast-1. Cross-region links are private peering, encrypted with MACsec where supported.
- DR drill: quarterly, picks a random Tier 1 cluster, restores it to the DR site, runs the tenant smoke test, and times the result. Drill result and deviations documented in dr-drills repo.
- DNS failover: Route 53 and Cloud DNS health checks on the primary endpoint, 30 s interval, 3 failures trigger failover to the DR endpoint with a 60 s TTL.
- Runbook: dr-runbook.md in the dba-runbooks repo, reviewed annually.
"""  # noqa: E501

version = "0.0.1"
