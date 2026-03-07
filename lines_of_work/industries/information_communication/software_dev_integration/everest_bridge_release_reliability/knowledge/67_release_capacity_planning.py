"""Release capacity planning for sustainable delivery."""

title = "Release Capacity Planning"

content = """
Capacity planning ensures the organisation can deliver releases without overloading teams or
infrastructure. Balance release frequency with team capacity and operational overhead.

**Team Capacity:** Account for development, testing, review, deployment, and post-release
monitoring. Avoid stacking multiple high-risk releases in the same window. Plan for
vacation and support load.

**Infrastructure:** Ensure staging and production can handle deployment traffic. Consider
database migration windows, cache invalidation, and batch job schedules. Plan for
infrastructure changes that require coordination.

**Dependencies:** Map cross-team dependencies. Schedule dependent releases in sequence
or coordinate parallel releases. Buffer time for integration issues.
"""

version = "0.0.1"
