"""Knowledge item: contract testing strategy."""

title = "Vertragstest-Strategie"

content = """
Vertragstests stellen sicher, dass Service-Schnittstellen den vereinbarten Vertrag einhalten.
Consumer und Provider definieren gemeinsam das erwartete Verhalten; Tests prüfen die Einhaltung.

**Consumer-Driven Contracts:** Der Consumer definiert Erwartungen an die API; der Provider
muss diese erfüllen. Änderungen am Provider brechen den Vertrag, wenn sie nicht rückwärtskompatibel sind.

**Provider-Verifikation:** Der Provider führt Vertragstests als Teil seiner CI-Pipeline aus.
Bei Vertragsbruch schlägt der Build fehl, bevor Änderungen deployed werden.

**Wichtige Aspekte:** Schema-Validierung, HTTP-Statuscodes, Header, Fehlerformate.
Bei verteilten Systemen reduzieren Vertragstests Integrationsfehler in Production erheblich.
"""

version = "0.0.1"
