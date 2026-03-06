title = "Grundlagen von Datenpipelines"

content = """
Eine Datenpipeline ist eine automatisierte Abfolge von Schritten, die Daten von
Quellsystemen extrahieren, transformieren und in Zielsysteme laden. Sie bildet
das Rückgrat jeder Datenplattform und muss zuverlässig, nachvollziehbar und
wartbar sein.

**Extraktion:** Daten werden aus APIs, Datenbanken, Dateisystemen oder
Streaming-Quellen gelesen. Wichtige Aspekte sind inkrementelle vs. vollständige
Ladung, Rate-Limits und Fehlertoleranz bei temporären Ausfällen.

**Transformation:** Rohdaten werden bereinigt, angereichert, aggregiert und
an Zielschemas angepasst. Transformationen sollten idempotent sein, damit
Wiederholungen bei Fehlern keine Duplikate erzeugen.

**Ladung:** Die transformierten Daten werden in Data Lakes, Data Warehouses
oder Streaming-Systeme geschrieben. Schreibstrategien (Append, Upsert, Replace)
müssen zum Use Case passen.

**Orchestrierung:** Ein Scheduler oder Orchestrator (z.B. Airflow) steuert die
Reihenfolge, Abhängigkeiten und Retry-Logik der Pipeline-Schritte.
"""

version = "0.0.1"
