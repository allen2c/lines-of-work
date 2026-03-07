"""Knowledge item: Integrationstest-Protokoll."""

title = "Integrationstest-Protokoll"

content = """
Integrationstests validieren die Zusammenarbeit von Komponenten über Schnittstellen hinweg.
Sie erfordern eine kontrollierte Testumgebung mit echten oder nahezu echten Abhängigkeiten.

**Protokoll:** Vor dem Test: Umgebung bereitstellen, Testdaten laden, Abhängigkeiten
(APIs, Datenbanken) prüfen. Während des Tests: Szenarien ausführen, Antworten und
Seiteneffekte verifizieren. Nach dem Test: Ressourcen bereinigen, Ergebnisse protokollieren.

**Zuverlässigkeitsbezug:** Integrationstests decken Fehler auf, die Unit-Tests nicht
finden: Vertragsbrüche, Timeouts, falsche Serialisierung, Race Conditions. Für Elbe Valley
sind Integrationstests für alle externen API- und Datenbank-Integrationen verpflichtend.
Bei Fehlschlägen muss die Ursache (Code vs. Umgebung vs. Abhängigkeit) klar identifiziert
werden können.
"""

version = "0.0.1"
