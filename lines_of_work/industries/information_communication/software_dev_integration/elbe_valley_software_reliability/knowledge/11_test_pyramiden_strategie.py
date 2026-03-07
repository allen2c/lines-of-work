"""Knowledge item: Test-Pyramiden-Strategie."""

title = "Test-Pyramiden-Strategie"

content = """
Die Test-Pyramide strukturiert die Testabdeckung nach Aufwand und Ausführungsgeschwindigkeit.
Viele schnelle Unit-Tests bilden die Basis, weniger Integrations- und End-to-End-Tests die Spitze.

**Struktur:** Unit-Tests prüfen isolierte Logik ohne externe Abhängigkeiten. Integrations-Tests
validieren die Zusammenarbeit von Komponenten. E2E-Tests simulieren Nutzerflüsse über das
gesamte System. Die Pyramide verhindert, dass langsame, flaky E2E-Tests die Feedback-Schleife
verlangsamen.

**Zuverlässigkeitsbezug:** Für Elbe Valley bedeutet dies, dass kritische Pfade (Zahlung,
Authentifizierung, Datenkonsistenz) auf allen Ebenen abgedeckt sein müssen. Die Pyramide
ist ein Werkzeug, kein Dogma — bei verteilten Services können Integrations-Tests mehr
Gewicht haben als bei monolithischen Anwendungen.
"""

version = "0.0.1"
