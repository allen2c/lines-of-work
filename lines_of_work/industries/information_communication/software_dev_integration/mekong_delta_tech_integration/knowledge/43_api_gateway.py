title = "API Gateway"

content = """
API Gateway là entry point cho API. Xử lý cross-cutting concerns: auth, rate limit,
routing, transformation. Mekong Delta Tech dùng API gateway trước backend services.

**Routing:** Route by path, host, header. Version routing (/v1, /v2). Canary,
A/B test. Load balance to backend. Service discovery integration.

**Authentication:** Validate JWT, API key tại gateway. Extract user/session.
Forward to backend. Reject unauthenticated early. Offload auth logic từ service.

**Rate Limiting:** Centralized rate limit. Per client, per endpoint. Sliding
window. Return 429. Config-driven. Different limit per plan/tier.

**Transformation:** Request/response transformation. Protocol translation.
Legacy support. Cache response. Compress. Add headers. Gateway có thể là bottleneck
— scale horizontally, optimize.
"""  # noqa: E501

version = "0.0.1"
