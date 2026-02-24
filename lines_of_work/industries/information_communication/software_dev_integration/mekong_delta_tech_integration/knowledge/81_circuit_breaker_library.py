title = "Circuit Breaker Library"

content = """
Circuit breaker implementation: library hoặc framework. Mekong Delta Tech
dùng resilience4j, Polly, hoặc similar. Chuẩn hóa behavior across services.

**Configuration:** Failure threshold. Wait duration (open state). Half-open
max calls. Sliding window. Per-instance hoặc shared. Config external. Tune
per dependency.

**Integration:** Wrap HTTP client, DB call. Transparent. Fallback callback.
Metrics export. Event (state change). Log. Easy to add to existing code.

**Testing:** Unit test circuit behavior. Integration test với failed dependency.
Verify open, half-open transition. Fallback called. Metrics. Chaos test.

**Monitoring:** Circuit state metrics. Transition count. Fallback count.
Alert on high fallback rate. Dashboard. Correlate với dependency health.
"""  # noqa: E501

version = "0.0.1"
