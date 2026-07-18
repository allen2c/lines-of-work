title = "Slow Query Triage Workflow"

content = """
- Step 1: pull top 50 by total_exec_time from pg_stat_statements over the last 24 h.
- Step 2: filter out queries with calls below 10 (likely ad-hoc) and mean_exec_time below 100 ms (acceptable).
- Step 3: for each remaining query, capture EXPLAIN (ANALYZE, BUFFERS, VERBOSE) and the actual bind parameters.
- Step 4: classify the root cause: missing index, stale stats, schema mismatch, application N+1, or genuine data growth.
- Step 5: open a ticket to the tenant with the diagnosis and a recommended DDL or config change; track resolution in slow-query-tracker.
"""  # noqa: E501

version = "0.0.1"
