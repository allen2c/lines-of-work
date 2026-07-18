title = "Connection Pooling Configuration"

content = """
- PostgreSQL: PgBouncer in transaction pooling mode, default pool_size = vCPU * 4, reserve_pool 10 percent, server_idle_timeout 600 s. DNS points app to PgBouncer VIP, not the primary directly.
- MySQL: ProxySQL in front with mysql-default_qps 10, max_connections matched to backend max_connections 300.
- MongoDB: built-in connection pooler, maxPoolSize 100 per app instance, minPoolSize 10.
- ClickHouse: HTTP and native interfaces, max_connections 4096, keep_alive_timeout 3 s; recommend clients use clickhouse-driver with chunked reads.
- Connection storm alert: open connections above 80 percent of max_connections for more than 5 min triggers SEV3.
"""  # noqa: E501

version = "0.0.1"
