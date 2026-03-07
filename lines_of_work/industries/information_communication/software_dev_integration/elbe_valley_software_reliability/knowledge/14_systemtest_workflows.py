"""Knowledge item: Systemtest-Workflows."""

title = "Systemtest-Workflows"

content = """
Systemtests prüfen das Verhalten des Gesamtsystems unter realistischen Bedingungen.
Sie laufen typischerweise gegen Stage- oder Test-Umgebungen, die Production nachempfunden sind.

**Workflows:** End-to-End-Szenarien abbilden: Nutzeranmeldung, kritische Geschäftsprozesse,
Datenexport, Benachrichtigungen. Last- und Stresstests gehören ebenfalls in diese Kategorie.
Systemtests sind langsamer und ressourcenintensiver als Unit- oder Integrationstests.

**Zuverlässigkeitsbezug:** Systemtests validieren, dass alle Komponenten zusammen funktionieren.
Sie decken Konfigurationsfehler, Netzwerkprobleme und Skalierungsgrenzen auf. Für Elbe Valley
müssen alle kritischen User Journeys vor jedem Release durch Systemtests abgedeckt sein.
Flaky Systemtests werden priorisiert behoben, da sie das Vertrauen in die Pipeline untergraben.
"""

version = "0.0.1"
