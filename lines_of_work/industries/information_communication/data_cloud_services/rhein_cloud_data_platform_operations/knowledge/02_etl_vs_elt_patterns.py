title = "ETL vs. ELT-Muster"

content = """
ETL (Extract, Transform, Load) und ELT (Extract, Load, Transform) beschreiben
zwei grundlegende Architekturmuster für Datenintegration. Die Wahl beeinflusst
Latenz, Kosten und Flexibilität.

**ETL:** Transformationen erfolgen vor dem Laden, typischerweise in einem
dedizierten Transformations-Server oder Spark-Cluster. Gut geeignet für
strukturierte Daten mit klar definierten Schemas. Die Last liegt auf der
Transformations-Infrastruktur; das Zielsystem bleibt schlank.

**ELT:** Rohdaten werden zuerst in den Zielspeicher (z.B. Data Lake, Warehouse)
geladen; Transformationen laufen dort mittels SQL oder dbt. Nutzt die Skalierung
des Cloud-Warehouses. Ideal für flexible Schemas und schnelle Iteration, da
neue Transformationen ohne erneute Extraktion hinzugefügt werden können.

**Hybrid:** Viele Plattformen nutzen ELT für Batch-Workloads und behalten ETL
für Echtzeit- oder Streaming-Szenarien, wo Vorverarbeitung vor dem Schreiben
erforderlich ist.
"""

version = "0.0.1"
