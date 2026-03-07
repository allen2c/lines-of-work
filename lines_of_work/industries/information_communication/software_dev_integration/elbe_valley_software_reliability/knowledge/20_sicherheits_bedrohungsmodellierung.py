"""Knowledge item: security threat modeling."""

title = "Sicherheits-Bedrohungsmodellierung"

content = """
Threat Modeling identifiziert potenzielle Angriffsvektoren und Schwachstellen vor der Implementierung.
STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, DoS, Elevation of Privilege)
ist ein etabliertes Framework.

**Prozess:** Systemgrenzen und Datenflüsse dokumentieren, Bedrohungen pro Komponente
auflisten, Risiken priorisieren, Gegenmaßnahmen definieren und in Tests überführen.

**Integration in Qualität:** Sicherheitsanforderungen als Teil der Quality Gates;
Authentifizierung, Autorisierung, Verschlüsselung und Input-Validierung explizit testen.

**Regelmäßige Überprüfung:** Bei Architekturänderungen Threat Model aktualisieren.
"""

version = "0.0.1"
