"""Deployment runbook standards for consistent execution."""

title = "Deployment Runbook Standards"

content = """
Runbooks standardise deployment steps so any qualified engineer can execute a release safely.
Each runbook should be release-specific or template-based for a given service.

**Structure:** Prerequisites (access, tools, approvals), pre-deployment checks, deployment steps
in order, post-deployment verification, rollback steps, and contact information. Use numbered
steps. Include expected outcomes and how to verify each step.

**Maintenance:** Update runbooks when deployment process changes. Version runbooks with the
release. Review runbooks in release retrospectives. Automate where possible but keep manual
override steps documented.

**Accessibility:** Store runbooks in a central location. Link from release tickets. Ensure
runbooks are executable in the target environment (correct commands, correct order).
"""

version = "0.0.1"
