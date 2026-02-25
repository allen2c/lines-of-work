title = "Xử lý Backpressure"

content = """
Backpressure: downstream slow, upstream phải slow down. Prevent overload.
Integration flow cần backpressure. Mekong Delta Tech implement trong message
flow.

**Recognition:** Downstream latency tăng. Queue build up. Error rate tăng.
Resource exhaustion. Detect. Signal. React. Don't ignore. Cascade failure.

**Strategies:** Block producer. Drop message. Slow consumer. Buffer limit.
Reject. Circuit breaker. Slow down source. Feedback. Adaptive. Per integration.
Trade-off: lose message vs overload. Choose. Document.

**Propagation:** Service A → B → C. C slow. B propagate to A. Stop A sending.
Chain. Coordination. Or B buffer (bounded). Backpressure signal. Implement
correctly.

**Testing:** Simulate slow consumer. Verify backpressure. No OOM. No cascade.
Graceful. Monitor. Tune. Document behavior. Integration contract.
"""  # noqa: E501

version = "0.0.1"
