title = "Multi-Tenant Isolation and Data Boundaries"

content = """
SaaS products isolate tenant data.
Support understands boundaries and
never accesses or references
other tenants' data.

**Access Control:** Agents use
elevated access only for the
ticket's tenant. Verify
tenant context before any
administrative action.

**Cross-Tenant:** Data sharing
or migration between tenants
requires explicit customer
request and approval. Follow
data handling procedures.

**Incidents:** Tenant-specific
incidents are isolated. Do not
imply other tenants are
affected without confirmation.
"""  # noqa: E501

version = "0.0.1"
