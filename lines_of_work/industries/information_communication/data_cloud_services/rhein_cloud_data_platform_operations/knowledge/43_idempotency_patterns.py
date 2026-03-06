title = "Idempotenzmuster in Datenpipelines"

content = """
Idempotenz bedeutet, dass die mehrfache Ausführung einer Operation dasselbe
Ergebnis liefert wie eine einmalige Ausführung. Bei Pipelines ist das kritisch,
weil Jobs wiederholt laufen können (Retries, manuelle Neustarts). Typische
Ansätze: Upsert-Logik mit eindeutigen Schlüsseln, Merge-Statements, oder
partitionsbasierte Überschreibung. Ohne Idempotenz entstehen Duplikate oder
inkonsistente Zustände. Rhein Cloud verlangt idempotente Pipelines für alle
produktiven Jobs. Die Implementierung hängt von der Zielplattform ab (z.B.
MERGE in Snowflake, Delta MERGE in Databricks).
"""

version = "0.0.1"
