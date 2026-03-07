"""Deployment health checks."""

title = "Deployment Health Checks"

content = """
Health checks bepalen of een deployment succesvol is. Definieer checks die binnen een redelijke
tijd (bijv. 5-10 min) een betrouwbaar signaal geven. Te strikte checks blokkeren; te losse
missen problemen.

**Liveness:** Service start en reageert op /health. Basis connectivity.

**Readiness:** Service is klaar voor verkeer. Database connectie, cache, dependencies.
Load balancer stuurt pas verkeer na readiness.

**Post-deploy:** Smoke tests, critical path verificatie, metric baseline vergelijking. Bij
canary: vergelijk error rates tussen canary en baseline. Automatiseer waar mogelijk.
"""

version = "0.0.1"
