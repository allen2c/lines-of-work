"""Knowledge item: Abhängigkeitsrisiko-Management."""

title = "Abhängigkeitsrisiko-Management"

content = """
Externe und interne Abhängigkeiten bergen Risiken: Ausfälle, Breaking Changes,
Sicherheitslücken oder Lizenzänderungen. Systematisches Management reduziert Überraschungen.

**Kontext:** Kein System steht allein. Bibliotheken, Frameworks, SaaS-Dienste und
interne Services können jederzeit ausfallen oder sich ändern. Die Auswirkung hängt
von der Kritikalität und der Kopplung ab.

**Hauptmaßnahmen:**
1) Abhängigkeitsinventar: Alle direkten und indirekten Abhängigkeiten erfassen
2) Regelmäßige Aktualisierungen und Sicherheits-Scans (z. B. Dependabot, Snyk)
3) Wrapper oder Adapter für kritische externe Dienste, um Austauschbarkeit zu ermöglichen
4) Circuit Breaker und Fallbacks für externe Aufrufe
5) Dokumentation der Abhängigkeitsentscheidungen und Upgrade-Pfade

**Akzeptanzkriterien:** Abhängigkeiten sind kategorisiert nach Kritikalität. Es gibt
einen definierten Prozess für Updates und Notfall-Reaktionen bei Ausfällen.
"""

version = "0.0.1"
