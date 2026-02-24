title = "Tích hợp Database"

content = """
Integration thường cần đọc/ghi database. Direct DB connection, replication,
hoặc qua API. Chọn approach ảnh hưởng coupling và scalability.

**API vs Direct:** Prefer API khi có. Decoupling. Direct DB khi performance
critical, same org, trusted. Stored procedure, view. Document schema. Version
migration carefully.

**Connection Pooling:** Limit connections. Pool size = f(concurrency, DB limit).
Connection leak = eventual exhaustion. Timeout. Monitor pool usage.

**Read Replicas:** Read từ replica để scale. Write to primary. Replication lag.
Eventual consistency. Don't read-after-write từ replica. Use primary cho critical
read. Document consistency model.

**Transaction:** Scope transaction correctly. Don't hold long. Distributed
transaction avoid khi có thể. Saga cho cross-DB. Retry transaction với care.
"""  # noqa: E501

version = "0.0.1"
