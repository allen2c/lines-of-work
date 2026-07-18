title = "Replication Configuration"

content = """
- Standard topology for P1 PostgreSQL: 1 primary, 2 synchronous replicas in-region (RPO 0 within region), 1 async replica in a second region for DR (RPO 30 s typical, 5 min SLA).
- MySQL: 1 primary, 2 semisync replicas (after_ack_wait 1), 1 Group Replication channel for read scaling.
- MongoDB: replica set with 5 voting members, writeConcernMajority default, readConcern majority for tenant-facing reads.
- ClickHouse: 2 replicas per shard via ReplicatedMergeTree, plus Distributed tables over 3 shards; ZooKeeper ensemble 1+2 across 3 AZs.
- Replication lag SLO: P1 2 s p99, P2 10 s p99, P3 60 s p99.
"""  # noqa: E501

version = "0.0.1"
