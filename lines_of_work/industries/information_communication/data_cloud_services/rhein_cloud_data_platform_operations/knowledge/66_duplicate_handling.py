title = "Duplikatbehandlung"

content = """
Duplikate entstehen durch Retries, Mehrfach-Loads oder fehlende Idempotenz. Strategien:
Deduplizierung per Business-Key, MERGE/Upsert mit Last-Write-Wins, Hash-basierte
Erkennung. Dokumentation der gewählten Strategie pro Tabelle. Bei Streaming:
Exactly-Once-Semantik und idempotente Consumer sicherstellen.
"""

version = "0.0.1"
