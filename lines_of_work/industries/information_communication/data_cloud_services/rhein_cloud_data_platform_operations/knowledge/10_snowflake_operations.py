title: str = "Snowflake-Betrieb"

content: str = """
Snowflake ist ein cloud-natives Data Warehouse mit Trennung von Storage
und Compute. Der Betrieb umfasst Warehouse-Management, Storage-Optimierung
und Kostenkontrolle.

**Warehouses:** Compute-Ressourcen werden als Warehouses bereitgestellt.
Auto-suspend und auto-resume reduzieren Kosten bei Inaktivität. Die Wahl
der Warehouse-Größe beeinflusst Parallelität und Laufzeit.

**Storage:** Daten werden in internen Stages oder externen (S3, Azure)
gespeichert. Clustering und Partitionierung optimieren Abfrageleistung.
Time Travel und Fail-safe ermöglichen Wiederherstellung.

**Kosten:** Compute wird nach Sekunden abgerechnet; Storage nach TB.
Materialized Views und Caching können Kosten senken. Resource Monitors
begrenzen die Ausgaben pro Warehouse oder Account.

**Sicherheit:** RBAC über Roles, Netzwerkrichtlinien für Zugriff,
Verschlüsselung at-rest und in-transit. Audit-Logs für Compliance.
"""

version: str = "0.0.1"
