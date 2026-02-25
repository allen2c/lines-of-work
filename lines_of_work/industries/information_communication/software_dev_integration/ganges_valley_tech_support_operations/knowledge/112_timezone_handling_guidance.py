title = "Timezone and Date Handling Guidance"

content = """
Products display and store dates
in various timezones. Support
helps users configure and
interpret dates correctly.

**Storage:** Many systems use
UTC internally. Explain
conversion and display
settings. Warn about
daylight saving transitions.

**Scheduling:** Recurring
jobs, reports, or
notifications use timezone.
Verify user's configured
timezone and suggest
adjustments when wrong.

**API:** API may accept
ISO8601 with timezone.
Document format and
conversion behavior.
"""  # noqa: E501

version = "0.0.1"
