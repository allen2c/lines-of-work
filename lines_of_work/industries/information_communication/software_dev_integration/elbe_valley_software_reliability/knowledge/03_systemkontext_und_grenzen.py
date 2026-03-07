"""Knowledge item: Systemkontext und Grenzen."""

title = "Systemkontext und Grenzen"

content = """
Der Systemkontext definiert, wo das System beginnt und endet, welche externen Abhängigkeiten
existieren und welche Risiken außerhalb der direkten Kontrolle liegen.

**Kontext:** Ohne klare Systemgrenzen sind Risikoanalyse und Testplanung nicht möglich.
Externe APIs, Drittanbieter-Services und Infrastruktur-Komponenten müssen explizit erfasst werden.

**Vorgehen:**
1) Systemgrenzen und Schnittstellen zu externen Systemen dokumentieren
2) Abhängigkeiten nach Kritikalität und Kontrollierbarkeit bewerten
3) Annahmen über externe Systeme (Verfügbarkeit, Latenz) festhalten
4) Mock- und Stub-Strategien für nicht kontrollierbare Abhängigkeiten definieren
5) Risikoregister für Grenzfälle und Integrationspunkte pflegen

**Akzeptanzkriterien:** Kontextdiagramm existiert, alle kritischen Abhängigkeiten sind
dokumentiert, und Annahmen sind für Stakeholder nachvollziehbar.
"""

version = "0.0.1"
