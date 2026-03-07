"""Smoke testing after deployment."""

title = "Post-Deploy Smoke Testing"

content = """
Smoke tests zijn minimale verificaties direct na deployment om te bevestigen dat de
applicatie start en kernfunctionaliteit bereikbaar is. Ze moeten snel zijn (minuten)
en geautomatiseerd. Test critical paths: health endpoint, login, core API, en
database connectivity. Falende smoke tests blokkeren de release als succesvol;
initieer rollback of fix. Integreer smoke tests in de deployment pipeline.
"""

version = "0.0.1"
