title = "Point-in-Time Recovery"

content = """
- PostgreSQL PITR: stop the database, restore the last base backup to a fresh data directory, then run wal-g backup-fetch, configure recovery_target_time, start in recovery mode, and call pg_wal_replay_resume() to apply WAL.
- For P1 clusters the RPO target is 5 minutes. Verify recovery by running the tenant verify_db.sh checksum script and comparing row counts for the 50 largest tables.
- Document time-to-restore in the incident ticket; median should be under 18 min for a 200 GB cluster, under 45 min for a 1 TB cluster.
- Never overwrite a prod cluster in place; always restore to a new instance with a -restore-<timestamp> suffix, then cut over via CNAME or application-level switch.
"""  # noqa: E501

version = "0.0.1"
