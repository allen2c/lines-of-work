"""Knowledge item: resilience and retry handling."""

title = "Resilience und Retry-Handling"

content = """
Resilience-Patterns sorgen dafür, dass Systeme bei Teilausfällen weiterhin funktionieren.
Retry-Logik, Circuit Breaker und Timeouts sind zentrale Mechanismen.

**Retry:** Exponentielles Backoff mit Jitter vermeidet Thundering-Herd bei wiederkehrenden
Fehlern. Maximalversuche und Timeout-Grenzen definieren, um endlose Wiederholungen zu verhindern.

**Circuit Breaker:** Nach einer Fehlerschwelle den Aufruf sofort ablehnen statt erneut zu versuchen.
Nach einer Erholungsphase (Half-Open) erneut testen, ob der Service wieder verfügbar ist.

**Tests:** Fehlerinjektion (z. B. Netzwerkausfall, langsame Antworten) in Tests einbauen,
um Resilience-Verhalten zu verifizieren.
"""

version = "0.0.1"
