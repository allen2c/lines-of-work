"""Release environment isolation to prevent cross-environment contamination."""

title = "Release Environment Isolation"

content = """
Environment isolation ensures that development, staging, and production do not
interfere with each other. Proper isolation reduces risk of configuration drift and
accidental production impact.

**Network Isolation:** Separate networks or namespaces for each environment. Restrict
cross-environment access. Use firewall rules to enforce boundaries.

**Data Isolation:** Use separate databases and storage per environment. Avoid sharing
credentials or connection strings. Sanitize data when copying between environments.

**Access Control:** Limit production access to authorized personnel. Use different
credentials per environment. Audit access and changes.
"""

version = "0.0.1"
