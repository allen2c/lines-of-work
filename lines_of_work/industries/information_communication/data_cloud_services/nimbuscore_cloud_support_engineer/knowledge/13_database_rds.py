title = "Managed PostgreSQL and MySQL (NimbusDB) Issues"

content = """
- Connection storm symptoms: `too many connections` errors combined with a CPU plateau. The default `max_connections` is `DBInstanceClassMemory / 9531392`, capped at 5000.
- Recommend connection pooling via `pgbouncer` or `RDS Proxy` for any workload with more than 200 concurrent connections.
- Read replica lag above 30 seconds under steady load usually points to long-running writes on the primary; ask for `pg_stat_activity` and `pg_locks` output.
- Failover from primary to standby typically completes in 60-120 seconds; during failover, the writer endpoint briefly rejects new connections.
- Storage autoscaling can only expand, never shrink. If a customer provisioned 1 TB but only uses 100 GB, the cost cannot be reduced by shrinking the volume.
"""  # noqa: E501

version = "0.0.1"
