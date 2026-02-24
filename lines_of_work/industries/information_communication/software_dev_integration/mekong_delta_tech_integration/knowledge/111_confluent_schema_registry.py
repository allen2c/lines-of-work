title = "Confluent Schema Registry"

content = """
Schema Registry central schema store cho Kafka. Avro, Protobuf, JSON Schema.
Versioning, compatibility. Mekong Delta Tech dùng Confluent Schema Registry.

**Workflow:** Producer register schema, get ID. Embed ID in message. Consumer
fetch schema by ID. Decode. Compatibility check on register. Reject breaking.
Migration path. Multiple version coexist.

**Compatibility:** BACKWARD, FORWARD, FULL. Choose per topic. BACKWARD: new
consumer read old. FORWARD: old read new. FULL: both. Configure. Test. Document.

**Admin:** List subjects. Versions. Delete (soft). Compatibility test. API.
CLI. Monitor. Schema evolution. Document. Partner coordinate. Change process.

**Failure:** Registry down. Cache schema. Offline. Fallback. Circuit breaker.
Retry. Don't block produce/consume. Resilient. Test registry failure.
"""  # noqa: E501

version = "0.0.1"
