title: str = "Datenqualitätsdimensionen"

content: str = """
Datenqualität wird entlang mehrerer Dimensionen bewertet. Jede Dimension
beeinflusst die Vertrauenswürdigkeit und Nutzbarkeit der Daten für
Analytics und operative Systeme.

**Vollständigkeit:** Fehlen Werte (Nulls, leere Strings) in erwarteten
Feldern? Vollständigkeits-Checks zählen fehlende Werte pro Spalte und
melden Abweichungen vom erwarteten Anteil.

**Korrektheit:** Entsprechen Werte den definierten Formaten und Regeln?
Beispiele: E-Mail-Format, PLZ-Bereich, Fremdschlüssel-Referenzintegrität.

**Konsistenz:** Stimmen Daten über Quellen und Zeiträume hinweg überein?
Doppelte Einträge mit abweichenden Werten, Inkonsistenzen zwischen
Systemen deuten auf Qualitätsprobleme.

**Aktualität:** Wie aktuell sind die Daten relativ zum Ereigniszeitpunkt?
Latenz-SLAs und Data-Freshness-Metriken messen die Verzögerung.

**Eindeutigkeit:** Gibt es unerwartete Duplikate? Deduplizierung und
Uniqueness-Checks identifizieren doppelte Datensätze.
"""

version: str = "0.0.1"
