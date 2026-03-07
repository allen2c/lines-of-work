"""Knowledge item: End-to-End-Nutzerflüsse."""

title = "End-to-End-Nutzerflüsse"

content = """
E2E-Tests simulieren reale Nutzerinteraktionen über die gesamte Anwendung hinweg —
von der Oberfläche bis zu Backend-Services und Datenbanken. Sie sind die langsamsten
und fragilsten Tests, liefern aber das höchste Vertrauen für Release-Entscheidungen.

**Best Practices:** Kritische Pfade priorisieren (Checkout, Registrierung, Kernfunktionen).
Tests stabil gestalten: explizite Wartezeiten, robuste Selektoren, Vermeidung von
zeitbasierten Assertions. Bei Fehlschlägen: Screenshots, Logs und Reproduktionsschritte
sicherstellen.

**Zuverlässigkeitsbezug:** E2E-Tests sind die letzte Bestätigung vor dem Release. Für Elbe
Valley gilt: Mindestens die Top-5-Nutzerflüsse müssen E2E-abgedeckt sein. Flaky E2E-Tests
werden entweder repariert oder durch zuverlässigere Integrations-Tests ersetzt — niemals
einfach ignoriert.
"""

version = "0.0.1"
