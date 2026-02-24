title = "Avro Schema"

content = """
Avro là format phổ biến trong Kafka ecosystem. Schema-embedded hoặc schema
registry. Good cho event streaming. Mekong Delta Tech dùng Avro với Confluent
Schema Registry.

**Schema Definition:** JSON format. Record, enum, array, map, union. Named types.
Schema evolution rules: add optional, backward/forward compatible. Reader schema
có thể khác writer — resolve at read.

**Schema Registry:** Central schema store. Producer register schema, get id.
Embed schema id trong message. Consumer fetch schema by id. Versioning, compatibility
check. Prevent breaking change.

**Performance:** Binary encoding. Compact. Fast serialization. Compare to JSON.
Schema in header có overhead. Consider for high-throughput Kafka.

**Evolution:** Add field với default: compatible. Delete field with default:
compatible. Change type: incompatible. Test compatibility với registry before
deploy. Multiple version trong cluster during migration.
"""  # noqa: E501

version = "0.0.1"
