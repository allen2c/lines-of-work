title = "SLO và Monitoring"

content = """
SLO (Service Level Objective) define target reliability. Monitoring verify
SLO. Integration có SLO để manage expectation. Mekong Delta Tech define SLO
cho API và integration dependencies.

**SLO Definition:** Availability: 99.9% requests success. Latency: p99 < 500ms.
Error budget: 0.1% = 43 min downtime/month. Document SLO. Agree với stakeholder.

**Metrics:** Request rate, error rate, latency histogram. Per endpoint. Per
dependency. RED metrics. Export to Prometheus. Grafana dashboard. Track
trend.

**Alerting:** Alert when SLO at risk. Burn rate. Budget remaining. Page on-call
khi critical. Runbook. Don't alert on every breach — use multi-window. Alert
tuning.

**Integration Dependency:** Downstream SLO affects us. Composite SLO. Chain
of dependency. Monitor dependency. Circuit breaker when dependency degraded.
"""  # noqa: E501

version = "0.0.1"
