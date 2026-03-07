"""Secrets management during releases."""

title = "Secrets Management Releases"

content = """
Secrets (API keys, certificates, credentials) must be managed securely across environments.
Releases should not introduce secret sprawl or expose credentials in artifacts or logs.

**Rotation:** Plan secret rotation as part of release when credentials change. Coordinate
with dependent services to avoid downtime. Use short-lived tokens where possible.

**Environment Parity:** Ensure each environment has the correct secrets for its purpose.
Staging should use non-production credentials. Never promote production secrets to dev.

**Verification:** After deployment, verify services can access required secrets. Log
access attempts (not values) for audit. Document which secrets each release depends on.
"""

version = "0.0.1"
