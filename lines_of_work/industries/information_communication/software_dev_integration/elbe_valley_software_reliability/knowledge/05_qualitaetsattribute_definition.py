"""Knowledge item: Qualitätsattribute-Definition."""

title = "Qualitätsattribute-Definition"

content = """
Qualitätsattribute (z. B. Verfügbarkeit, Latenz, Durchsatz, Fehlertoleranz) müssen messbar
und testbar definiert werden. Vage Formulierungen wie „schnell genug“ führen zu
nicht überprüfbaren Erwartungen.

**Kontext:** ISO 25010 und ähnliche Modelle liefern Kategorien. Für den Betrieb müssen
konkrete, messbare Ziele abgeleitet werden, die in SLOs und Testkriterien münden.

**Vorgehen:**
1) Relevante Qualitätsattribute für den Service identifizieren
2) Messbare Ziele mit Einheiten und Schwellenwerten definieren
3) Testmethoden zuordnen (z. B. Lasttest für Durchsatz, Chaos für Resilienz)
4) Trade-offs zwischen Attributen dokumentieren (z. B. Latenz vs. Konsistenz)
5) Akzeptanzkriterien für jedes Attribut festlegen

**Akzeptanzkriterien:** Alle kritischen Attribute haben messbare Ziele, Testmethoden
sind zugeordnet, und Trade-offs sind dokumentiert.
"""

version = "0.0.1"
