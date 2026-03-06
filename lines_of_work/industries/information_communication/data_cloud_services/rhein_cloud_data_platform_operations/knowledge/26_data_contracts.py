title = "Data Contracts"

content = """
Data contracts define the expected schema, semantics, and SLAs between producers
and consumers. A contract specifies column names, types, nullability, and
business rules. Contracts enable independent evolution: producers announce
breaking changes; consumers adapt. Use schema registries (e.g., Confluent Schema
Registry for Kafka) for enforcement. Version contracts semantically. Rhein Cloud
requires contracts for all cross-team data products. Breaking changes require
advance notice and migration support. Contracts reduce integration failures and
clarify ownership.
"""

version = "0.0.1"
