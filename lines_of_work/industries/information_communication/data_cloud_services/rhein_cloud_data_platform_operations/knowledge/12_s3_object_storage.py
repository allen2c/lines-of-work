title = "S3 und Object Storage"

content = """
Object Storage (AWS S3, Azure Blob, GCS) speichert Daten als unveränderliche
Objekte mit Metadaten. Keine Verzeichnisstruktur im klassischen Sinne, sondern
flache Namespaces mit Präfixen. Lifecycle-Policies automatisieren Übergänge
zwischen Storage-Klassen (Standard, IA, Glacier). Versionierung schützt vor
versehentlichem Überschreiben. Cross-Region-Replication für Disaster Recovery.
Verschlüsselung (SSE-S3, SSE-KMS) für Daten im Ruhezustand. Preise pro GB und
Anfrage; große Objekte und viele kleine Anfragen beeinflussen die Kosten.
"""

version = "0.0.1"
