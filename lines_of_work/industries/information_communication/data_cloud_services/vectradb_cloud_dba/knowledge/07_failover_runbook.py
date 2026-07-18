title = "Failover Procedures"

content = """
- Automatic failover is enabled for P1 and P2 clusters when both conditions are true for 5 consecutive minutes: primary unreachable via pg_is_in_recovery() and at least one replica shows streaming with lag below 10 s.
- PostgreSQL: use patroni with etcd consensus. Promote with patronictl failover --master <cluster> --candidate <replica>. Verify new primary with SELECT pg_is_in_recovery(); expecting false.
- MySQL: orchestrator detects and promotes; verify with SHOW SLAVE STATUS\\G and SELECT @@global.read_only.
- MongoDB: rs.stepDown(60) for graceful, otherwise automatic election per replica set protocol.
- After failover: re-attach the old primary as a replica, file a post-mortem, and notify the tenant within 30 minutes.
"""  # noqa: E501

version = "0.0.1"
