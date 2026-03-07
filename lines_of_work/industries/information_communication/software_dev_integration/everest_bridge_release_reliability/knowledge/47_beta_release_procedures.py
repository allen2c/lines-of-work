"""Beta release procedures for early validation."""

title = "Beta Release Procedures"

content = """
Beta releases allow validation with a limited audience before full production rollout.
Define who receives beta (internal, partners, opt-in users) and what feedback is collected.

**Criteria:** Beta is appropriate when the change is feature-complete but needs real-world
validation. Not for half-built features or untested code. Define success criteria to
graduate from beta to general availability.

**Process:** Use feature flags or separate beta environment. Collect metrics, error rates,
and user feedback. Document known issues and workarounds. Set a timeline for beta duration.

**Promotion:** When beta criteria are met, follow normal release process for GA. Archive
beta feedback for future reference.
"""

version = "0.0.1"
