title = "Request Timeout"

content = """
Timeout ngăn request chờ vô hạn khi downstream chậm hoặc hang. Quan trọng cho
integration stability. Cấu hình đúng là balance giữa reliability và user experience.

**Timeout Hierarchy:** Client timeout < Load balancer < Service timeout < DB timeout.
Mỗi layer có timeout riêng. Outer layer nên dài hơn inner. Document timeout chain.

**Values:** API thường 5-30s. DB query 1-10s. External call phụ thuộc SLA. Quick
fail (2-5s) cho optional data. Longer cho critical path. Test với slow dependency.

**Timeout Handling:** Khi timeout, cancel in-flight request nếu có thể. Return
504 hoặc timeout-specific error. Don't leave orphan operations. Idempotency giúp
client retry safe.

**Propagation:** Không mask timeout. Propagate với context (trace ID). Log với
duration. Alert khi timeout rate cao. Correlation với downstream latency.
"""  # noqa: E501

version = "0.0.1"
