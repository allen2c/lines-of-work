title = "Nullpunkte, Bezugssysteme und M-Codes"

content = """
- Maschinennullpunkt M: Hersteller-Nullpunkt, unveränderlich; erreicht über Referenzpunktfahrt.
- Werkstücknullpunkt W: Bezugspunkt der Zeichnung, wird über G54 (Sinumerik) bzw. Preset (Heidenhain) angefahren.
- Werkzeuglängen- und -radiuskorrektur aus der Werkzeugtabelle, korrigiert die Bahnplanung automatisch.
- M-Funktionen (Auswahl): M0 Programmhalt, M1 optionaler Halt, M3/M4 Spindel re/li, M5 Spindel stopp, M6 Werkzeugwechsel, M8/M9 KSS ein/aus, M30 Programmende mit Rückspulen.
- Bezugspunkt-Setzstrategie bei komplexen Teilen: 3-2-1-Aufspannung (Haupt-, Sekundär-, Tertiärebene) oder Pass-Stift-Bezugselement.
- Sinumerik: G54–G59 Standardsätze, G505–G599 erweiterte Sätze; für jedes Aufspannen eigene G-Verschiebung.
- Heidenhain: Preset-Tabelle aktivieren, Preset auf Werkstücknullpunkt setzen.
- Korrektur im laufenden Programm: G10 (Sinumerik) oder manuell in der Werkzeugtabelle, danach Kommentar im Programm.
- Bei Nullpunkt-Verschiebung immer im Trockenlauf kontrollieren, bevor ein Werkstück gespannt wird.
"""  # noqa: E501

version = "0.0.1"
