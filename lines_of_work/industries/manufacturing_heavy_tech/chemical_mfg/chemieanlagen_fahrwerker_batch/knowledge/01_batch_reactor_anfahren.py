title = "Batch-Reaktor Anfahrprozedur"

content = """
- Vor dem Anfahren: Sichtprüfung der Anlage (Ventile, Flansche, Manometer), Überprüfung der Medienversorgung (Dampf, Kühlwasser, Stickstoff, Druckluft).
- Rezeptur aus dem MES laden: Chargennummer, Rohstoffchargen, Sollwerte für Temperatur, Druck, Rührerdrehzahl, pH-Wert.
- Schrittweise Befüllung: zuerst Vorlage (Lösungsmittel), dann Feststoffe über Dosierschnecke, zuletzt Katalysator. Rührer auf 50 U/min starten.
- Heizung zuschalten: Dampfventil langsam öffnen, Temperaturrampe max. 2 °C/min. Überwachung des Druckanstiegs (max. 0,5 bar über Soll).
- Nach Erreichen der Reaktionstemperatur: Haltezeit gemäß Rezeptur (z. B. 120 Minuten bei 80 °C). Alle 15 Minuten pH-Wert und Temperatur protokollieren.
- Nach Reaktionsende: Kühlung aktivieren (Kühlwasser 15 °C), bis Produkttemperatur unter 40 °C. Probe entnehmen (siehe 08_probenahme).
"""

version = "0.0.1"
