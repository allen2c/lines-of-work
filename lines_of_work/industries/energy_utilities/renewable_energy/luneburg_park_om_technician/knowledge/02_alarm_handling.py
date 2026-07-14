title = "Alarmbearbeitung"

content = """
- Alarme werden im SCADA-System farblich kategorisiert: Rot (kritisch – sofortiges Handeln), Gelb (Warnung – innerhalb 1 Stunde prüfen), Blau (Info – innerhalb der Schicht bearbeiten).
- Bei rotem Alarm (z. B. „Wechselrichter Übertemperatur“) schalte die Anlage ferngesteuert ab, wenn die Temperatur > 85 °C steigt. Sende einen Techniker vor Ort, sofern keine automatische Kühlung anspringt.
- Gelbe Alarme (z. B. „Stringstrom niedrig“) analysiere im Detail: Vergleiche mit Nachbarstrings, prüfe auf Verschattung oder Moduldefekt. Dokumentiere im CMMS.
- Blau-Alarme (z. B. „Kommunikationsverlust einzelner Sensor“) setze auf die To-do-Liste für den nächsten Außeneinsatz.
"""

version = "0.0.1"
