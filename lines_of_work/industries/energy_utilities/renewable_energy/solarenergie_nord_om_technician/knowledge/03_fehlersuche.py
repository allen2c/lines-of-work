title = "Systematische Fehlersuche an PV-Anlagen"

content = """
- Beginne mit der SCADA-Übersicht: Welche Strings/Wechselrichter zeigen Ertragsminderung? Filtere nach Zeitraum (letzte 24h, 7 Tage).
- Gehe zum betroffenen Wechselrichter: Prüfe LED-Status, Fehlerspeicher auslesen (z. B. „DC-Überspannung“, „Isolationsfehler“).
- Führe Stringmessungen durch (siehe 02_stringmessung) und vergleiche mit Nachbarstrings.
- Bei Verdacht auf Moduldefekt: Thermografie-Aufnahme (siehe 19_thermografie) oder IV-Kennlinienmessung (siehe 20_iv_kennlinien).
- Dokumentiere Fehlerursache, durchgeführte Maßnahmen und Ersatzteilbedarf im CMMS.
"""

version = "0.0.1"
