title = "ETag và Caching"

content = """
ETag: validator cho cache. Conditional request. 304 Not Modified. Save
bandwidth. Mekong Delta Tech support ETag cho cacheable resource.

**Flow:** Server return ETag trong response. Client store. Next request
If-None-Match: etag. Server compare. Same = 304, no body. Different = 200,
new body, new ETag. Client update cache. Standard. HTTP cache.

**Generation:** Hash của content. Version. Weak ETag (W/). Change when resource
change. Consistent. Same resource = same ETag. Efficient compare.

**Integration:** GET resource. Cache. Conditional request. Reduce transfer.
Freshness. Stale? Revalidate. API support. Document. Client implement.
Cache control. Max-age. ETag complement. Use when beneficial.
"""  # noqa: E501

version = "0.0.1"
