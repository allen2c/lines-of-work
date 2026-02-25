title = "Chiến lược Caching"

content = """
Cache giảm load backend và latency. Integration layer có thể cache response từ
upstream. Strategy đúng balance freshness và performance.

**Cache Invalidation:** Hard problem. TTL-based: đơn giản, stale possible. Event-based:
invalidate on change, complex. Hybrid. Document cache behavior cho client.

**Cache Location:** Client cache (browser), CDN, reverse proxy, application cache.
Mỗi layer có scope. Private vs shared. Cache key: URL, headers (Vary).

**Integration Caching:** Cache upstream API response. TTL based on data volatility.
Cache key: request params. Stale-while-revalidate. Don't cache personalized,
sensitive. Respect Cache-Control từ upstream.

**Consistency:** Cache inconsistency với source. Eventually consistent OK cho
many cases. Strong consistency cần careful invalidation. Document cho client.
"""  # noqa: E501

version = "0.0.1"
