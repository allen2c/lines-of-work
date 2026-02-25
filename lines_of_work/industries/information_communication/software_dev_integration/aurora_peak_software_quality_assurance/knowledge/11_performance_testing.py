title = "Performance Testing for Financial Applications"

content = """
Financial applications must handle peak loads without degradation. Performance
testing validates response times, throughput, and resource utilization under
realistic and stress conditions.

**Load Testing:** We simulate expected user concurrency and transaction
volumes. Targets are set from business projections (e.g., 1000 concurrent
users, 500 TPS). We measure latency percentiles (p50, p95, p99) and
throughput.

**Stress and Soak Testing:** Stress tests push the system beyond normal
capacity to find breaking points. Soak tests run at sustained load for
extended periods to detect memory leaks, connection exhaustion, or
gradual degradation.

**Financial-Specific Concerns:** Transaction processing must complete within
SLA windows. Batch jobs (end-of-day, reconciliation) must finish before
deadlines. We test these explicitly and track trends over releases.
"""  # noqa: E501

version = "0.0.1"
