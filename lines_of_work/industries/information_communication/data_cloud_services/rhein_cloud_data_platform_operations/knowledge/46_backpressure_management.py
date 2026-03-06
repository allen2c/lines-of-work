title = "Backpressure und Durchsatzsteuerung"

content = """
Backpressure entsteht, wenn ein Downstream-System langsamer ist als die
Datenquelle. Ohne Steuerung können Puffer überlaufen oder Ressourcen
erschöpft werden. Kafka nutzt Consumer-Lag als natürlichen Puffer; zu hoher
Lag deutet auf Backpressure hin. Spark und Flink bieten konfigurierbare
Backpressure-Mechanismen. Maßnahmen: Skalierung der Consumer, Throttling
der Producer, oder temporäre Pausen. Rhein Cloud überwacht Consumer-Lag
und reagiert bei Schwellenwerten mit Skalierung oder Alarmierung.
"""

version = "0.0.1"
