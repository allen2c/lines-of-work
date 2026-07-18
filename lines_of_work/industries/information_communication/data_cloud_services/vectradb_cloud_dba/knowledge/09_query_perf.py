title = "Query Performance Tuning"

content = """
- Slow query thresholds: above 500 ms p95 over 1 h window triggers a ticket; above 2 s p95 escalates to the tenant within 24 h.
- PostgreSQL: use pg_stat_statements (top 20 by total_exec_time), join with pg_stat_user_tables to find the underlying tables, then EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON).
- Common fixes: missing index (add), statistics stale (ANALYZE), wrong join order (hint via planner GUC for tenant opt-in), parameter sniffing (re-test with plan_cache_mode = force_custom_plan).
- MySQL: optimizer trace, EXPLAIN FORMAT=TREE, sys.schema_index_statistics for unused index detection.
- MongoDB: aggregation pipelines rewritten to put $match before $lookup, indexed explain('executionStats'); ClickHouse: system.query_log filtered by type >= 'QueryFinish'.
"""  # noqa: E501

version = "0.0.1"
