title = "Data-Warehouse-Konzepte"

content = """
Ein Data Warehouse ist ein optimierter Speicher für strukturierte, analytische
Daten. Es unterstützt Abfragen über große Datenmengen und bildet die Basis
für BI, Reporting und Data Science.

**Star- und Schneeflocken-Schema:** Faktentabellen enthalten Messwerte;
Dimensionstabellen beschreiben Kontexte (Zeit, Kunde, Produkt). Star-Schema
hat flache Dimensionen; Schneeflocken normalisiert Dimensionen weiter.

**DWH vs. Data Lake:** Das Warehouse ist schema-on-write, stark strukturiert
und für SQL-Abfragen optimiert. Der Lake speichert Rohdaten; das Warehouse
wird oft aus dem Lake gespeist (Medallion-Architektur).

**Cloud-Warehouses:** Snowflake, BigQuery, Redshift und Azure Synapse bieten
getrennte Compute- und Speicher-Skalierung. Abrechnung erfolgt nach
Verbrauch; Kapazitätsplanung unterscheidet sich von On-Premise.
"""

version = "0.0.1"
