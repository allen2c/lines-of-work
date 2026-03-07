"""Knowledge item: API-Vertragsdesign."""

title = "API-Vertragsdesign"

content = """
API-Verträge definieren die Schnittstelle zwischen Diensten. Ein klares, versioniertes
Vertragsdesign reduziert Integrationsfehler und ermöglicht automatisierte Vertragstests.

**Kontext:** Änderungen an APIs können Downstream-Systeme brechen. Ohne explizite Verträge
und Versionsstrategie entstehen stille Fehler, die erst in Production sichtbar werden.
OpenAPI, AsyncAPI oder gRPC-Protobuf dienen als maschinenlesbare Vertragsspezifikationen.

**Hauptmaßnahmen:**
1) Verträge vor Implementierung definieren und mit Konsumenten abstimmen
2) Semantische Versionierung: Major für Breaking Changes, Minor für Erweiterungen
3) Deprecation-Policy: Mindestfrist für Ablösung alter Versionen
4) Vertragstests als Teil der CI: Provider und Consumer getrennt validieren
5) Fehlerantworten und Grenzfälle explizit im Vertrag spezifizieren

**Akzeptanzkriterien:** Jede API hat einen veröffentlichten Vertrag. Änderungen werden
gegen Vertragstests geprüft. Breaking Changes erfordern Koordination mit allen Konsumenten.
"""

version = "0.0.1"
