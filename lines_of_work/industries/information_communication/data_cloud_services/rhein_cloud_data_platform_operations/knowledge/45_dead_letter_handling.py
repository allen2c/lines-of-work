title = "Dead-Letter-Queue und Fehlerbehandlung"

content = """
Nachrichten oder Datensätze, die nicht verarbeitet werden können, landen in
einer Dead-Letter-Queue (DLQ). Gründe: Schema-Inkompatibilität, ungültige
Daten, Timeouts. Die DLQ muss überwacht werden; anhaltendes Wachstum deutet
auf systematische Probleme hin. Prozess: Fehler analysieren, Ursache beheben,
Daten ggf. reparieren und erneut verarbeiten. Rhein Cloud nutzt dedizierte
Kafka-Topics oder S3-Pfade als DLQ. Jeder Eintrag wird mit Fehlergrund und
Zeitstempel protokolliert. Regelmäßige Reviews der DLQ-Inhalte sind Teil
des Betriebsprozesses.
"""

version = "0.0.1"
