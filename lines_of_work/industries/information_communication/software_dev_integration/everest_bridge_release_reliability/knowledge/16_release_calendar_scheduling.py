"""Release calendar and scheduling knowledge item."""

title = "Release Calendar and Scheduling"

content = """
A release calendar coordinates deployments across teams, reduces conflicts, and sets
expectations for stakeholders. It balances predictability with flexibility for urgent
changes.

**Cadence:** Define a release cadence (e.g., weekly, biweekly, monthly) aligned with
business needs and team capacity. Communicate the schedule widely. Stick to it unless
emergency overrides.

**Windows:** Specify deployment windows (day, time, duration) when releases are permitted.
Avoid high-traffic periods and critical business events. Account for time zones in
global teams.

**Freezes:** Plan release freezes for holidays, fiscal closes, or major events. Announce
freezes well in advance. Define the process for emergency releases during freezes.

**Coordination:** For multi-team or multi-service releases, use a shared calendar. Identify
dependencies and sequence. Avoid same-window deployments of interdependent services
without explicit coordination.

**Communication:** Publish the calendar in a central location. Send reminders before
release windows. Update stakeholders when the schedule changes.
"""

version = "0.0.1"
