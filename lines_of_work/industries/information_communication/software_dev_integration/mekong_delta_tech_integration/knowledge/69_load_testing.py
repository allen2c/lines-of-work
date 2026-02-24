title = "Load Testing"

content = """
Load test verify system under load. Find bottleneck. Validate capacity.
Integration cần load test trước production. Mekong Delta Tech load test
mọi API.

**Metrics:** Throughput (RPS). Latency (p50, p95, p99). Error rate. Resource
usage (CPU, memory). Find breaking point. Baseline. Compare after change.

**Tool:** k6, Gatling, Locust, JMeter. Script scenarios. Ramp-up. Sustain
load. Spike test. Soak test (extended). Report. CI integration.

**Scenarios:** Typical flow. Mixed read/write. Peak load (2-3x normal). Dependency
slow. Partial failure. Realistic data. Think like production traffic.

**Analysis:** Identify bottleneck. DB? Network? Downstream? Optimize. Retest.
Document capacity. Plan scaling. Alert threshold based on test.
"""  # noqa: E501

version = "0.0.1"
