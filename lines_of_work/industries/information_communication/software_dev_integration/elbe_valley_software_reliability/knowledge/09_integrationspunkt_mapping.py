"""Knowledge item: Integrationspunkt-Mapping."""

title = "Integrationspunkt-Mapping"

content = """
Integrationspunkte sind die Stellen, an denen Systeme miteinander kommunizieren.
Ein vollständiges Mapping aller Punkte ist Voraussetzung für gezielte Integrationstests.

**Kontext:** Moderne Systeme bestehen aus vielen Microservices, externen APIs und
Datenbanken. Jeder Integrationspunkt ist eine potenzielle Fehlerquelle. Ohne
Übersicht können kritische Pfade ungetestet bleiben.

**Hauptmaßnahmen:**
1) Alle eingehenden und ausgehenden Schnittstellen katalogisieren
2) Abhängigkeiten und Aufrufketten visualisieren (z. B. Service-Mesh, Architekturdiagramme)
3) Kritikalität und Ausfallauswirkung pro Integrationspunkt bewerten
4) Teststrategie pro Punkt: Mock, Stub, Test-Double oder echte Integration
5) Kontinuierliche Aktualisierung bei Änderungen der Architektur

**Akzeptanzkriterien:** Jeder Integrationspunkt ist dokumentiert mit Owner, Vertrag
und Testabdeckung. Kritische Pfade haben End-to-End-Tests oder äquivalente Abdeckung.
"""

version = "0.0.1"
