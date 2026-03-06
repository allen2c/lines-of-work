title = "Change Data Capture (CDC)"

content = """
CDC captures only changed records from source systems, reducing load and enabling
near-real-time replication. Common patterns: log-based CDC (Debezium, Fivetran)
reads database transaction logs; trigger-based CDC uses database triggers.
Considerations: source system support, latency requirements, schema evolution.
CDC requires careful handling of deletes, updates, and late-arriving data.
Idempotency and ordering guarantees are critical. Rhein Cloud uses CDC for
operational databases syncing to the data lake; batch loads remain for
historical or non-logged sources.
"""

version = "0.0.1"
