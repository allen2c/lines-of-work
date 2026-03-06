title = "Data-Lake-Architektur"

content = """
Ein Data Lake ist ein zentraler Speicher für Rohdaten in ihrem ursprünglichen
Format. Im Gegensatz zum Data Warehouse werden Daten nicht vorab strukturiert;
Schema-on-Read ermöglicht flexible Analysen.

**Zonen:** Typische Zonierung umfasst Raw (unveränderte Quelldaten), Staging
(vorläufig bereinigt), Curated (business-ready) und Sandbox (experimentell).
Daten fließen von Raw zu Curated; Rückwärtsbewegungen vermeiden.

**Formate:** Parquet und Delta Lake sind Standard für analytische Workloads
wegen Kompression, Spaltenorientierung und Schema-Evolution. JSON und CSV
bleiben für Rohdaten üblich.

**Metadaten:** Ein Data Catalog (z.B. Apache Atlas, AWS Glue) verwaltet
Linieage, Klassifikation und Zugriffsrechte. Ohne Katalog degeneriert der
Lake zu einem „Data Swamp“.
"""

version = "0.0.1"
