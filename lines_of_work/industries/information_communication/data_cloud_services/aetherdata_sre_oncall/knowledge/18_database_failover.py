title = "Database Failover Procedures"

content = """
- For managed PostgreSQL clusters: if primary node is unhealthy, automatic failover occurs within 30 seconds. Verify new primary is accepting writes.
- For Redis: if master is down, sentinel promotes a replica. Check data consistency.
- For Cassandra: if a node is down, the cluster remains available. Repair the node using `nodetool repair`.
- Manual failover: use the runbook for the specific database type. Always test in staging first.
- After failover, monitor replication lag and ensure all replicas are in sync.
"""  # noqa: E501

version = "0.0.1"
