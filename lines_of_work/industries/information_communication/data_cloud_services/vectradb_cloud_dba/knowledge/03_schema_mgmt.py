title = "Schema Change Management"

content = """
- All DDL on prod clusters goes through the Schema Review pipeline: PR opened against acme/dba-changes repo, CI runs sqitch verify, pg_regress for PostgreSQL, and a liquibase --contexts=prod dry-run.
- Forward and reverse migrations are mandatory. Forward must be online-safe: no ACCESS EXCLUSIVE lock longer than 2 s on tables above 10 GB; use CREATE INDEX CONCURRENTLY, gh-ost for MySQL, or the engine online DDL.
- Rolling deploy is enforced: schema change first applied to the read replica, then promoted, then applied to the old primary after re-attachment.
- Long-running migrations (above 5 min wall clock or on tables above 100 GB) require a written runbook and a standby engineer to babysit the rollout.
"""  # noqa: E501

version = "0.0.1"
