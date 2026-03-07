"""Knowledge item: Domänenmodell-Validierung."""

title = "Domänenmodell-Validierung"

content = """
Das Domänenmodell bildet die Geschäftslogik ab. Validierung stellt sicher, dass
Invarianten und Geschäftsregeln zuverlässig eingehalten werden.

**Kontext:** Fehler im Domänenmodell führen zu inkonsistenten Zuständen, falschen
Berechnungen oder Verletzungen von Geschäftsregeln. Diese Fehler sind oft schwer
zu reproduzieren und können große finanzielle oder rechtliche Folgen haben.

**Hauptmaßnahmen:**
1) Invarianten explizit definieren und in Unit-Tests abdecken
2) Grenzfälle und Randbedingungen systematisch identifizieren
3) State-Machine-Tests für komplexe Workflows
4) Property-based Testing für numerische und logische Regeln
5) Integration mit Event-Sourcing und CQRS prüfen, falls eingesetzt

**Akzeptanzkriterien:** Alle Geschäftsregeln haben automatisierte Tests. Keine
Invariante bleibt ungeprüft. Änderungen am Modell erfordern Aktualisierung der Tests.
"""

version = "0.0.1"
