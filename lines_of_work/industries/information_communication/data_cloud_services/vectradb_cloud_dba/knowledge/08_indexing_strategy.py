title = "Index Management and Bloat Control"

content = """
- PostgreSQL: identify bloat with pgstattuple; rebuild if dead-tuple ratio above 20 percent or index bloat above 50 percent. Use REINDEX CONCURRENTLY to avoid exclusive locks.
- Schedule VACUUM (ANALYZE, VERBOSE) daily on tables above 1 GB; autovacuum scale factor 0.05, cost limit 2000, cost delay 20 ms, workers 4, max_workers tuned to vCPU count.
- MySQL: OPTIMIZE TABLE monthly for InnoDB tables above 5 GB; monitor INFORMATION_SCHEMA.INNODB_SYS_TABLES.
- Index candidates: columns with high idx_scan/seq_scan ratio in pg_stat_user_tables; confirm with EXPLAIN (ANALYZE, BUFFERS) before creation.
- Composite indexes follow equality-then-range rule; partial indexes for WHERE deleted_at IS NULL style predicates.
"""  # noqa: E501

version = "0.0.1"
