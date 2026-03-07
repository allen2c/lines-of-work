"""Knowledge item: Unit-Testing-Standards."""

title = "Unit-Testing-Standards"

content = """
Unit-Tests prüfen einzelne Funktionen oder Klassen in Isolation, typischerweise mit Mocks
für externe Abhängigkeiten. Sie müssen schnell, deterministisch und wartbar sein.

**Standards:** Jeder Test hat einen klaren Arrange-Act-Assert-Aufbau. Testnamen beschreiben
das erwartete Verhalten (z. B. „sollte Fehler werfen wenn Eingabe leer ist“). Keine
Testinterdependenzen — Tests dürfen in beliebiger Reihenfolge laufen. Flaky Tests werden
sofort behoben oder entfernt.

**Zuverlässigkeitsbezug:** Unit-Tests sind die erste Verteidigungslinie gegen Regressions.
Sie decken Randfälle und Edge Cases ab, die in höheren Testebenen oft übersehen werden.
Für Elbe Valley gilt: Kritische Geschäftslogik muss unit-getestet sein, bevor sie in
den Integrations- oder E2E-Bereich gelangt.
"""

version = "0.0.1"
