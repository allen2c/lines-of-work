title = "On-Call Schedule"

content = """
- Follow-the-sun rotation: three shifts (APAC, EMEA, AMER). Each shift is 12 hours (8am-8pm local time) with a primary and secondary responder.
- Primary handles all alerts; secondary is backup and handles SEV1 escalations if primary is overwhelmed.
- Schedule is managed via PagerDuty. Handoff occurs at shift start and end.
- During handoff, review open incidents, ongoing investigations, and any pending runbook updates.
- On-call shifts last one week. After a week, you are off for at least two weeks (no on-call).
- If you need to swap shifts, coordinate in #sre-schedule at least 48 hours in advance.
"""  # noqa: E501

version = "0.0.1"
