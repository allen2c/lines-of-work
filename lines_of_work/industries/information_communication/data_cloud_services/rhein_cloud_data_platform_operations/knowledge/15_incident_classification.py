title = "Incident Classification"

content = """
Incidents werden nach Schweregrad klassifiziert: P1 (kritisch, vollständiger
Ausfall), P2 (hoch, wesentliche Funktionen betroffen), P3 (mittel, Workaround
verfügbar), P4 (niedrig, geringe Auswirkung). Klassifikation bestimmt
Eskalationspfad und Reaktionszeit. Bei Datenplattformen: P1 wenn Pipelines
komplett ausfallen und SLA verletzt wird; P2 bei Teilausfällen oder
Datenqualitätsproblemen mit Geschäftsauswirkung. Klare Definitionen in
Runbooks verhindern Fehlklassifikation. Nach jeder Klassifikation Review, ob
die Einstufung korrekt war.
"""

version = "0.0.1"
