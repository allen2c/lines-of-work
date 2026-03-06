title = "Exactly-Once-Semantik in Streaming"

content = """
Exactly-once garantiert, dass jede Nachricht genau einmal verarbeitet wird,
auch bei Fehlern und Neustarts. Kafka unterstützt dies über transaktionale
Producer, Consumer-Offsets in derselben Transaktion und idempotente Consumer.
Bei Spark Structured Streaming wird das über Checkpointing und
Write-Ahead-Logs erreicht. Die Implementierung ist komplex und erfordert
sorgfältige Konfiguration. At-least-once ist einfacher, erfordert aber
idempotente Senken. Rhein Cloud nutzt exactly-once dort, wo Duplikate
inakzeptabel sind (z.B. Finanztransaktionen).
"""

version = "0.0.1"
