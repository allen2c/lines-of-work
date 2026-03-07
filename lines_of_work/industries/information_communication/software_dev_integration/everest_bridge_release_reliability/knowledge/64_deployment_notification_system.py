"""Deployment notification system for stakeholder awareness."""

title = "Deployment Notification System"

content = """
Notifications keep stakeholders informed before, during, and after deployments. Define what
to notify, when, and to whom. Use automated channels where possible.

**Pre-deployment:** Notify scheduled deployment window, expected duration, and impact (e.g.
brief read-only mode). Include link to release notes and runbook. Send 24–48 hours before
for planned releases.

**During:** For deployments with user impact, send start notification. Optionally send
progress updates for long-running deployments. Alert on failure or rollback.

**Post-deployment:** Send completion notification with version deployed, verification status,
and link to release notes. For incidents, send incident summary and resolution.

**Channels:** Use email, Slack, PagerDuty, or internal status page. Avoid over-notifying;
batch non-critical updates. Document notification templates and recipients.
"""

version = "0.0.1"
