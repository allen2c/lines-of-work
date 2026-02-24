title = "Capacity Planning cho API"

content = """
Capacity planning: estimate load, provision resource. Integration API cần plan.
Mekong Delta Tech plan capacity cho growth.

**Estimate:** Historical growth. Partner pipeline. Seasonality. Event. Forecast.
Buffer. Peak vs average. Document assumption. Review quarterly. Update.

**Load Test:** Verify capacity. Stress test. Find limit. Benchmark. Resource
per RPS. Scale factor. Document. Monitor utilization. Alert before limit.
Headroom. Plan scaling trigger.

**Scaling:** Horizontal. Auto-scale. Metric (CPU, RPS, latency). Scale up/down.
Cool down. Cost. Right-size. Reserve capacity cho critical? Hybrid. Test
scale. Failover. Multi-region.

**Integration:** Partner volume. Rate limit per partner. Aggregate. Peak
concurrent. Plan. Communicate. SLA. Upgrade path. Document.
"""  # noqa: E501

version = "0.0.1"
