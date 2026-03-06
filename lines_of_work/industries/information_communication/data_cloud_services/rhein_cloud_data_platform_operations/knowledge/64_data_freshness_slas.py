title = "Data-Freshness-SLAs"

content = """
Data-Freshness-SLAs definieren, wie aktuell Daten für Downstream-Consumer sein müssen.
Beispiele: Echtzeit (< 5 Min), Near-Real-Time (< 1 h), Täglich (EOD). Messung über
Last-Update-Timestamps oder Dedicated-Monitoring. Verletzungen triggern Alerts und
eskalieren nach definierten Pfaden. Dokumentation für jeden Datensatz erforderlich.
"""

version = "0.0.1"
