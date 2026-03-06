title = "Schema Registry und Schema-Evolution"

content = """
Eine Schema Registry speichert Avro- oder Protobuf-Schemas und ermöglicht
versionierte, zentrale Schema-Verwaltung. Producer und Consumer referenzieren
Schemas per ID statt sie inline zu übertragen. Schema-Evolution (Hinzufügen
oder Entfernen von Feldern) muss rückwärts- und vorwärtskompatibel geplant
werden. Confluent Schema Registry und AWS Glue Schema Registry sind
gängige Optionen. Rhein Cloud nutzt Schema Registry für Kafka-Topics.
Änderungen werden vor Produktionseinsatz getestet und dokumentiert.
"""

version = "0.0.1"
