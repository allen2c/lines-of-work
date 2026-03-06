title = "Real-Time Dashboard Data Feeds"

content = """
Real-time dashboards consume streaming or high-frequency batch data. Latency
requirements are typically under one minute. Operations monitor feed health,
lag, and freshness. Backpressure from slow consumers can affect upstream
systems. Use separate topics or partitions for real-time vs batch consumers
to isolate impact.
"""

version = "0.0.1"
