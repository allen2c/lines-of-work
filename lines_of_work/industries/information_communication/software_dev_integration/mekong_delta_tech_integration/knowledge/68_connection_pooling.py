title = "Connection Pooling"

content = """
Connection reuse qua pool. TCP, HTTP, DB connection expensive to create.
Pool improve performance. Mekong Delta Tech configure pool cho mọi integration.

**HTTP Pool:** Keep-alive. Reuse TCP connection. Connection per host. Pool size
= concurrency. Timeout idle connection. Don't leak connection. HttpClient
with pool (requests.Session, okhttp ConnectionPool).

**DB Pool:** Connection pool (HikariCP, etc). Min/max pool size. Tune based
on DB max connections, app concurrency. Connection validation. Leak detection.
Timeout. Monitor pool metrics.

**Message Broker:** Connection reuse. Channel pool. Prefetch. Don't create
connection per message. Connection per thread/worker. Reconnect logic.
"""  # noqa: E501

version = "0.0.1"
