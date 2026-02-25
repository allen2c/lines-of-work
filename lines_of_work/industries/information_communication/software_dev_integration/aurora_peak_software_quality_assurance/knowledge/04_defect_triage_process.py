title = "Defect Triage and Severity Classification"

content = """
Defect triage ensures we prioritize fixes correctly and communicate
impact clearly. Severity reflects the effect on the system; priority
reflects business urgency. Both inform release decisions.

**Severity Levels:** Critical (system unusable, data loss risk), High
(major feature broken), Medium (workaround exists), Low (cosmetic or
minor). In financial systems, severity for money-related bugs is
often elevated regardless of frequency.

**Triage Cadence:** We hold triage meetings before each sprint or
release cycle. Defects are assigned severity, ownership, and target
release. Blocking defects are escalated immediately to leadership.

**Reproducibility and Information:** A well-documented defect includes
steps to reproduce, expected vs actual result, environment, and logs.
Incomplete reports delay resolution; we encourage developers and QA
to collaborate on reproduction.
"""  # noqa: E501

version = "0.0.1"
