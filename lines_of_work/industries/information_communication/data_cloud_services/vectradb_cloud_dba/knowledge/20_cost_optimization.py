title = "Cost Optimization Levers"

content = """
- Reserved instance coverage target: 70 percent of steady-state prod compute, renewed annually.
- Storage tiering: WAL and archive logs older than 30 days moved to S3 Glacier IR; backups older than 90 days to S3 Glacier Deep Archive.
- Right-sizing: clusters with p95 CPU below 20 percent for 30 consecutive days are candidates for downsizing; flagged in the weekly capacity review.
- ClickHouse: enable enable_mixed_granularity_parts 1, set min_bytes_for_wide_part 0 for small tables.
- PostgreSQL: enable pg_prewarm on the top 10 tables per cluster after restart; configure idle_in_transaction_session_timeout 60 s to release locks from stuck apps.
- Monthly FinOps report: per-tenant cost breakdown, YoY change, top 5 cost drivers, savings recommendations.
"""  # noqa: E501

version = "0.0.1"
