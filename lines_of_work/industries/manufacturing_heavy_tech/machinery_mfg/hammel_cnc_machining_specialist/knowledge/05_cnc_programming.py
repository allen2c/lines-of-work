title = "CNC-Programmierung (DIN/ISO, Klartext, CAM)"

content = """
- DIN/ISO-Code (Sinumerik/Fanuc): G0 Eilgang, G1 Linear, G2/G3 Kreis im Uhrzeigersinn/gegen, G41/G42 Fräserradiuskorrektur, G43 Werkzeuglängenkorrektur, G54–G59 Nullpunktverschiebebungen, G90/G91 absolut/incremental, M3/M4 Spindel re/li, M6 Werkzeugwechsel, M8/M9 KSS ein/aus, M30 Programmende.
- Heidenhain-Klartext (TNC 640): L Linear, CC/C Kreismittelpunkt, CYCL DEF Zyklen, TOOL CALL Werkzeugaufruf, BLK FORM RohteildEFINITION, FN-Funktionen für Parameterprogrammierung.
- CAM-Workflow: 3D-Modell (SolidWorks) → CAM-Setup (Mastercam/SolidCAM) → Postprozessor → NC-Programm → Simulation (Vericut) → Freigabe AV → Werkstatt.
- Eigenständige Programmänderungen nur mit Kommentarzeile und Schichtleiter-Sichtfreigabe; alte Versionen nicht überschreiben.
- Nullpunkt G54 immer auf Werkstück-Nullpunkt laut Zeichnung setzen, niemals auf Maschinen-Nullpunkt produzieren.
- Werkzeugtabelle pflegen: T-Nummer, L (Länge), R (Radius), DR/ER (Verschleiß), Standzeit, max. Drehzahl, max. Zustellung.
- Vor jedem Echtlauf: Trockenlauf ohne Material mit aktiver Vorschubbegrenzung 25 %.
"""  # noqa: E501

version = "0.0.1"
