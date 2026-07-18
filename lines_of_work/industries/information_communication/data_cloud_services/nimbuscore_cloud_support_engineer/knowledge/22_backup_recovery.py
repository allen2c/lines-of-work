title = "Backup, Snapshots, and Disaster Recovery Drills"

content = """
- EBS snapshots are incremental forever, but the first snapshot of a volume is always a full copy.
- Cross-region snapshot copy is a two-step operation: snapshot, then copy. The copy step's progress is visible in the Console at 5-minute granularity.
- Database automated backups have a default retention of 7 days; max is 35 days. Long-term retention beyond 35 days requires manual snapshots.
- A disaster recovery drill is a customer-initiated simulated failover; the engineer role provides runbook support but does not execute the failover.
- RPO/RTO targets: managed databases can achieve RPO < 5 seconds with cross-region replicas; self-managed EC2-equivalent workloads depend on the customer's snapshot cadence.
"""  # noqa: E501

version = "0.0.1"
