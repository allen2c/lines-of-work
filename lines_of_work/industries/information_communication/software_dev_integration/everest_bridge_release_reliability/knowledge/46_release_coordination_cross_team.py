"""Cross-team release coordination practices."""

title = "Release Coordination Cross-Team"

content = """
When multiple teams share dependencies or deployment windows, coordination prevents
conflicts and failed deployments. Establish a release calendar, dependency map, and
communication channels.

**Calendar:** Maintain a shared release calendar. Teams reserve slots and declare
dependencies. Avoid overlapping high-risk releases when possible.

**Dependency Map:** Document which services depend on others. Order releases so
downstream consumers deploy after upstream providers. Use version contracts (e.g. API
compatibility) to allow independent release ordering when possible.

**Communication:** Use a dedicated channel for release status. Announce start, completion,
and any blockers. Run a release sync meeting for complex multi-team releases.
"""

version = "0.0.1"
