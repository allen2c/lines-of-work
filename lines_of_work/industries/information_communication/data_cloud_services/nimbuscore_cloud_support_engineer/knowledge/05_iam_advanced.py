title = "Cross-Account Roles, SSO, and Federation Issues"

content = """
- Cross-account assume-role failures are most often caused by: stale External ID, mismatched `nc:RequestedRegion` condition, or a trust policy that has not been republished after a customer org rename.
- SSO via NC Identity Federation (SAML 2.0) issues usually trace to a certificate expiry on the IdP side; the customer's admin can confirm by decoding the SAML response at `https://nc-idp-debug.local/`.
- Session duration default is 1 hour; max is 12 hours for human users and 6 hours for service identities.
- If a customer claims a role worked yesterday and fails today, the top three causes are: (1) IAM policy rollback by their admin, (2) role session name contains an unsupported character, (3) the role's trust policy references a deleted principal.
- Document the `RequestId`, `Error Code`, and the `EncodedMessage` from the response; these are required for any T3 escalation.
"""  # noqa: E501

version = "0.0.1"
