title = "Circuit Breaker Pattern"

content = """
Circuit breaker ngăn cascade failure khi downstream service liên tục fail. Cho phép
hệ thống fail fast và recovery khi service đích phục hồi.

**States:** Closed (normal), Open (reject calls), Half-Open (test recovery). Chuyển
Open khi failure count vượt threshold. Sau timeout, chuyển Half-Open để thử một request.

**Threshold Configuration:** Failure count hoặc failure rate. Time window để tính.
Timeout trước khi thử lại. Tune theo SLA và recovery time của downstream.

**Fallback:** Khi circuit open, return fallback: cached data, default value, hoặc
degraded response. Log fallback để monitor. Có thể queue request cho retry sau.

**Monitoring:** Alert khi circuit open. Track open/close frequency. Correlate với
downstream health. Dùng với timeout và retry — circuit breaker là layer ngoài cùng.
"""  # noqa: E501

version = "0.0.1"
