title = "Health Check Endpoint"

content = """
Health check cho phép load balancer và orchestrator quyết định route traffic.
Integration phụ thuộc health check của upstream. Mekong Delta Tech standardize
health check format.

**Liveness:** Service đang chạy. Simple check. Trả 200. Dùng để restart container
khi crash. Không check dependency — avoid restart loop khi DB down.

**Readiness:** Service sẵn sàng nhận traffic. Check DB connection, cache, critical
dependency. Trả 200 khi ready, 503 khi not. Load balancer stop sending traffic
khi not ready. Kubernetes probe.

**Deep Health:** Optional. Check tất cả dependency. Detailed status per dependency.
Dùng cho operator dashboard. Không dùng cho routing — có thể fail do non-critical.

**Dependency Check:** Khi readiness check DB, có timeout. Don't block trên slow
dependency. Circuit breaker. Consider separate endpoint cho dependency status.
"""  # noqa: E501

version = "0.0.1"
