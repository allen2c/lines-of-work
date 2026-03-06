title: str = "Schema-Design und Evolution"

content: str = """
Schema-Design bestimmt die Struktur und Typen der Daten in Pipelines und
Speichern. Ein klares Schema ermöglicht Validierung, Dokumentation und
stabile Konsumenten. Schema-Evolution erlaubt Änderungen ohne komplette
Neuschreibungen.

**Schema-First vs Schema-on-Read:** Schema-First verlangt eine definierte
Struktur vor dem Schreiben; Schema-on-Read interpretiert bei Lesezeit.
Data Lakes nutzen oft Schema-on-Read; Data Warehouses Schema-First.

**Evolution-Strategien:** Backward-kompatible Änderungen (neue optionale
Felder) erlauben alte Konsumenten weiterzuarbeiten. Forward-kompatible
Änderungen erfordern, dass neue Felder von alten Konsumenten ignoriert
werden können. Breaking Changes erfordern Versionierung und Migration.

**Schema Registry:** Apache Kafka nutzt Confluent Schema Registry oder
ähnliche Dienste, um Avro/Protobuf-Schemas zu versionieren und zu
verteilen. Änderungen werden geprüft gegen Kompatibilitätsregeln.
"""

version: str = "0.0.1"
