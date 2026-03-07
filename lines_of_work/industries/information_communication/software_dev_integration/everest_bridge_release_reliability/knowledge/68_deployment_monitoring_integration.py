"""Deployment monitoring integration for release visibility."""

title = "Deployment Monitoring Integration"

content = """
Monitoring during and after deployment provides early warning of problems. Integrate
deployment events with observability tools so teams can correlate changes with metrics.

**Deployment Events:** Emit deployment start, success, and rollback events to monitoring
and logging systems. Tag metrics and traces with release version. This enables
before-after comparison and quick identification of regressions.

**Dashboards:** Create release-specific dashboards showing key metrics (error rate, latency,
throughput) for the deployed version. Set baseline from pre-deployment and compare.

**Alerting:** During deployment window, consider temporary alert sensitivity or dedicated
release channel. Avoid alert fatigue; ensure alerts are actionable. Document runbook
links in alerts.
"""

version = "0.0.1"
