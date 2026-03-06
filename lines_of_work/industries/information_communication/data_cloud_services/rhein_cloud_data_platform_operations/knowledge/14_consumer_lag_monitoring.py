title = "Consumer Lag Monitoring"

content = """
Consumer Lag misst die Differenz zwischen der neuesten Nachricht in einem
Kafka-Topic und der letzten von einem Consumer verarbeiteten Offset. Hoher Lag
deutet auf Verarbeitungsrückstand hin und kann zu veralteten Daten in
Downstream-Systemen führen. Monitoring-Tools (Kafka Manager, Confluent
Control Center, Datadog) visualisieren Lag pro Consumer-Gruppe und Partition.
Schwellenwert-Alerts bei Überschreitung (z.B. > 10.000 Nachrichten). Ursachen:
zu langsame Verarbeitung, zu wenige Consumer, Backpressure bei Sinks. Skalierung
der Consumer-Gruppe oder Optimierung der Verarbeitungslogik als Gegenmaßnahme.
"""

version = "0.0.1"
