"""Knowledge item: Datenqualität und Governance."""

title = "Datenqualität und Governance"

content = """
Datenqualität und Governance bilden die Grundlage für zuverlässige Systeme. Ohne konsistente,
valide und nachvollziehbare Daten können Tests und Metriken keine verlässlichen Aussagen liefern.

**Kontext:** In verteilten Systemen fließen Daten durch viele Komponenten. Jede Transformation,
jeder Integrationspunkt und jede Speicherung kann Qualitätsprobleme einführen. Die Governance
definiert Verantwortlichkeiten, Schemata und Validierungsregeln über den gesamten Datenlebenszyklus.

**Hauptmaßnahmen:**
1) Schema-Versionierung und Rückwärtskompatibilität für alle Datenverträge
2) Validierung an Systemgrenzen: Eingabe- und Ausgabedaten vor Verarbeitung prüfen
3) Datenlinie dokumentieren: Herkunft, Transformationen und Abhängigkeiten
4) Qualitätsmetriken: Vollständigkeit, Eindeutigkeit, zeitliche Konsistenz
5) Retentions- und Löschrichtlinien für Test- und Produktionsdaten

**Akzeptanzkriterien:** Governance-Regeln sind dokumentiert, automatisiert geprüft und
bei Verstößen werden Alerts ausgelöst. Jede Datenquelle hat einen definierten Owner.
"""

version = "0.0.1"
