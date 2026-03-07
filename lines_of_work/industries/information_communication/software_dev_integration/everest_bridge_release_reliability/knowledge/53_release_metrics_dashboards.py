"""Release metrics dashboards."""

title = "Release Metrics Dashboards"

content = """
Release dashboards geven inzicht in release gezondheid en trends. Track: release frequency,
lead time (commit tot productie), deployment success rate, rollback rate, en mean-time-to-recovery.

**Per release:** Deployment duur, gate passage tijden, post-release error rates, en feature
adoption (indien van toepassing). Vergelijk met baseline van vorige releases.

**Aggregatie:** Wekelijkse of maandelijkse trends voor management. DORA metrics (deployment
frequency, lead time, MTTR, change fail rate) zijn een gangbare standaard.

**Actie:** Dashboards moeten actie mogelijk maken. Bij afwijkingen: link naar runbook of
incident. Review dashboards in release retrospectives.
"""

version = "0.0.1"
