title = "Postmortem Template"

content = """
- **Title**: [Date] - [Incident ID] - [Brief Description]
- **Summary**: 2-3 sentences describing what happened and impact.
- **Timeline**: UTC timestamps of key events (alert, escalation, mitigation, resolution).
- **Root Cause**: Detailed technical explanation.
- **Impact**: Number of affected customers, duration, error budget consumed.
- **Action Items**: List of tasks with owner and due date, categorized as "fix", "prevent", "detect", "process".
- **Lessons Learned**: What went well, what went wrong, what to improve.
- Postmortem must be reviewed by the SRE team within 5 business days.
"""  # noqa: E501

version = "0.0.1"
