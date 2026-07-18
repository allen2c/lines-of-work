title = "Routine Maintenance"

content = """
- Autovacuum tuning: autovacuum_vacuum_scale_factor 0.05, autovacuum_analyze_scale_factor 0.02, autovacuum_max_workers 4, autovacuum_naptime 15 s for high-churn tables.
- Manual VACUUM FREEZE on tables above 100 GB quarterly, scheduled in the tenant maintenance window.
- ANALYZE after any bulk load above 10 percent of table rows; do not rely on autovacuum for fresh statistics.
- pg_repack for tables with bloat above 40 percent where REINDEX CONCURRENTLY is insufficient.
- Statistics refresh for information_schema and the tenant reporting views: weekly, Sunday 03:00 UTC.
"""  # noqa: E501

version = "0.0.1"
