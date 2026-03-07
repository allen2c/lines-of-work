"""Rollback automation for releases."""

title = "Rollback Automation"

content = """
Geautomatiseerde rollback vermindert mean-time-to-recovery bij mislukte deployments. Definieer
rollback scripts of pipeline stages die de vorige werkende versie herstellen.

**Prerequisieten:** Vorige artifact versie moet traceerbaar en beschikbaar zijn. Database
migrations moeten backward-compatible zijn of een down-migration hebben. Configuratie moet
versioned zijn.

**Trigger criteria:** Automatische rollback bij health check failures, error rate spikes, of
expliciete abort door operator. Handmatige rollback blijft beschikbaar voor edge cases.

**Verificatie:** Na rollback: smoke tests, metric verificatie, en log check. Documenteer
rollback in audit trail. Post-mortem als rollback frequent voorkomt.
"""

version = "0.0.1"
