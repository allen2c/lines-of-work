title = "CNC-Grundlagen und Steuerungstechnik"

content = """
CNC (Computer Numerical Control) steuert Werkzeugmaschinen durch digitale
Programme. Achsenbewegungen, Vorschübe und Spindeldrehzahlen werden
numerisch vorgegeben.

**Koordinatensystem:** Kartesisches XYZ-System. Z-Achse meist in Spindelrichtung.
Zusätzliche Achsen A, B, C für Schwenk- und Drehbewegungen bei Mehrachsenmaschinen.

**Programmierung:** G-Code (ISO 6983) oder werkzeugmaschinenspezifische Syntax.
Absolute (G90) oder inkrementelle (G91) Programmierung. Work Offsets (G54–G59)
für Nullpunktverschiebung.

**Interpolation:** Gerade (G01), Kreis (G02/G03), Spirale. Vorschub F in mm/min
oder mm/U bei Drehen. Spindeldrehzahl S in min⁻¹.

**CAD/CAM:** Geometrie aus CAD, Werkzeugwege durch CAM generiert. Postprozessor
erzeugt maschinenspezifischen Code. Simulation vor Produktion empfohlen.

**Steuerungstypen:** Punktsteuerung, Streckensteuerung, Bahnsteuerung (kontinuierlich).
Moderne Steuerungen mit Echtzeit, Antriebsregelung, Überwachungsfunktionen.
"""

version = "0.0.1"
