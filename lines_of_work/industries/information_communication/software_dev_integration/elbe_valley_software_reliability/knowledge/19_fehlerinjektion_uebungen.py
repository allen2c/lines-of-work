"""Knowledge item: fault injection drills."""

title = "Fehlerinjektion-Übungen"

content = """
Fehlerinjektion simuliert Ausfälle und Störungen, um die Reaktion des Systems zu prüfen.
Chaos Engineering nutzt kontrollierte Experimente, um Schwachstellen zu finden.

**Typen:** Netzwerk-Latenz, Paketverlust, Service-Ausfall, CPU-Spikes, Speicherdruck.
Tools wie Chaos Monkey oder Gremlin automatisieren Injektion in definierten Umgebungen.

**Sicherheit:** Nur in Stage/Pre-Production; niemals ohne Genehmigung in Production.
Blast-Radius begrenzen; Rollback-Plan und Monitoring vor dem Experiment bereithalten.

**Lernziele:** Welche Abhängigkeiten sind Single Points of Failure? Wie schnell erholt
sich das System? Sind Alerts und Runbooks korrekt?
"""

version = "0.0.1"
