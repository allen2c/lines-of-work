title = "Database and Query Support Boundaries"

content = """
Some products expose database or query interfaces.
Support helps with syntax, permissions, and
performance within documented capabilities.
Complex tuning or schema design is out of scope.

**Query Help:** Explain documented query
language, common patterns, and error messages.
Suggest alternatives when a query fails.

**Performance:** Basic indexing and limit
guidance is in scope. Deep performance
investigation escalates to Engineering or
DB specialists.

**Data Integrity:** Do not write or suggest
queries that modify production data without
explicit customer request and safeguards.
"""  # noqa: E501

version = "0.0.1"
