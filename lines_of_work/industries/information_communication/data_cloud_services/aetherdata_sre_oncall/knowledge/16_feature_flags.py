title = "Feature Flag Management"

content = """
- All new features are deployed behind feature flags (LaunchDarkly). Flags are toggled off by default.
- During an incident, if a feature flag is suspected, turn it off immediately for the affected service.
- Use the `/feature-flag off <flag_name>` Slack command. Confirm the change in the incident timeline.
- After incident, investigate the flag’s impact. If the flag caused the issue, file a bug and keep it off until fixed.
- Feature flags are reviewed weekly in the SRE team meeting.
"""  # noqa: E501

version = "0.0.1"
