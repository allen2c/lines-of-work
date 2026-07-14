title = "Tägliche SCADA-Überwachung"

content = """
- Starte jede Schicht mit einem Systemcheck: Überprüfe die Kommunikation aller Wechselrichter, Windturbinen und Messstationen. Status „Online“ muss bei > 95 % der Anlagen gegeben sein.
- Lies die Ertragskurven der letzten 24 Stunden aus: Soll-Leistung vs. Ist-Leistung. Abweichungen > 5 % über 1 Stunde sind meldepflichtig.
- Kontrolliere die Wetterdaten (Windgeschwindigkeit, Globalstrahlung) – bei Abweichungen > 10 % vom Prognosewert prüfe die Sensoren.
- Führe eine Sichtprüfung der Alarme durch: Bestätige alle aktiven Alarme, dokumentiere den Grund und leite Maßnahmen ein.
"""

version = "0.0.1"
