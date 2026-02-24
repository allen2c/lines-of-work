title = "Nén Response"

content = """
Compression giảm bandwidth. gzip, brotli. API response có thể lớn. Mekong
Delta Tech enable compression. Config. Trade-off CPU.

**Encoding:** gzip phổ biến. Brotli better ratio. Accept-Encoding request.
Content-Encoding response. Client decompress. Transparent. Library. Middleware.
Configure. Default gzip. Level. Balance ratio vs CPU.

**When:** Compress text (JSON, XML). Don't compress binary (image, already
compressed). Min size threshold. Overhead cho small response. Config. 1KB?
Document. Measure. Tune.

**Caching:** Compress per request. Or cache compressed. Vary: Content-Encoding.
CDN. Origin. Consider. Test. Monitor. Bandwidth save. Latency? CPU. Trade-off.
"""  # noqa: E501

version = "0.0.1"
