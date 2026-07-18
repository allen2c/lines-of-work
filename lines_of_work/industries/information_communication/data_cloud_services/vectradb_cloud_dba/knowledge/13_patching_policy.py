title = "Patching and Upgrade Cadence"

content = """
- Minor version upgrades (for example PostgreSQL 16.2 to 16.3): applied within 14 days of upstream release to the staging fleet, 7-day tenant notice, then rolling upgrade to prod cluster by cluster.
- Major version upgrades (for example 15 to 16): quarterly wave, tenant opt-in, with pg_upgrade --link for PostgreSQL to minimize downtime, target below 60 s.
- Security patches: CVSS 9.0 or higher patched within 72 h, 7.0 to 8.9 within 7 days, below 7.0 in the next monthly window.
- OS-level patches (Ubuntu 22.04) are covered by the host unattended-upgrades; reboot required monthly, blue-green at the cluster level.
- Pre-patch: snapshot via wal-g backup-push and verify checksum; post-patch: smoke test verify_db.sh and pg_stat_database.xact_rollback for unexpected spikes.
"""  # noqa: E501

version = "0.0.1"
