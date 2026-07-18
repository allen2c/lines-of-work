title = "Backup Policy and Retention"

content = """
- PostgreSQL: nightly logical dump via pg_dump -Fc plus continuous WAL archiving to S3 with wal-g. WAL segments kept 7 days; full base backups weekly.
- MySQL: nightly mysqldump --single-transaction --routines --triggers plus xtrabackup full every 6 hours for P1 clusters.
- MongoDB: mongodump nightly plus continuous oplog tail with 24 h window.
- ClickHouse: BACKUP ... TO S3(...) nightly plus replicated storage on each shard.
- Retention: P1 30 days, P2 14 days, P3 7 days. Quarterly DR drill restores a random P1 cluster to dr-restore-use1 and validates row counts against pg_stat_user_tables.n_live_tup or the engine equivalent.
"""  # noqa: E501

version = "0.0.1"
