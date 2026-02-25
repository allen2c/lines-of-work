title = "JWT and Token Troubleshooting"

content = """
JWT and bearer tokens authenticate
API and app requests. Expiry,
format, or scope issues cause
401/403 errors. Support helps
within documented auth flows.

**Expiry:** Tokens have limited
lifespan. Guide users to refresh
or re-authenticate. Explain
refresh token flow when
applicable.

**Format:** Malformed tokens
fail validation. Suggest
regenerating. Do not decode
or inspect tokens manually
due to security.

**Scope:** Tokens may have
limited scopes. Verify required
scopes for the operation.
Suggest re-auth with correct
permissions.
"""  # noqa: E501

version = "0.0.1"
