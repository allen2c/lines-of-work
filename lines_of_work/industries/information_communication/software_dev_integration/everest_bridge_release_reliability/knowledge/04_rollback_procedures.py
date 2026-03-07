"""Rollback procedures knowledge item."""

title = "Rollback Procedures"

content = """
Rollback is the ability to revert a release when it causes unacceptable impact. Every
release must have a defined, tested rollback path before deployment.

**Automated Rollback:** Prefer automated rollback triggers (e.g. error rate spike, latency
degradation) with clear thresholds. Automation reduces decision latency and human error
during incidents.

**Manual Rollback:** When automation is not sufficient, follow a documented runbook. Steps
typically include: stop traffic to new version, revert to previous artifact or configuration,
verify service restoration, and communicate status. Practice rollbacks in staging.

**Data Considerations:** Stateless services can often roll back by redeploying the previous
version. Stateful changes (schema migrations, data format changes) may require forward
compatibility or dedicated rollback migrations. Plan for these cases explicitly.
"""

version = "0.0.1"
