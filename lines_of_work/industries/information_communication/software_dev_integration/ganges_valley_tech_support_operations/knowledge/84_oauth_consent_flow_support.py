title = "OAuth and Consent Flow Support"

content = """
OAuth and consent flows enable third-party
integrations. Configuration errors or
user revocations cause connection
failures. Support troubleshoots within
documented flows.

**Common Issues:** Redirect URI
mismatch, scope requested vs granted,
or expired consent. Verify app
configuration against docs.

**User Revocation:** Users can revoke
access in their account settings.
Guide them to re-authorize if
intentional. Check provider status
for OAuth provider issues.

**Escalation:** Complex OAuth debugging
goes to Engineering. Provide client ID,
scopes, and error messages.
"""  # noqa: E501

version = "0.0.1"
