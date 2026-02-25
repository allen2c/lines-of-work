title = "Input Validation"

content = """
Input validation ngăn invalid hoặc malicious data vào system. Defense in depth.
Mekong Delta Tech validate mọi input tại integration boundary.

**Validation Layers:** Syntax (well-formed JSON). Schema (structure, types).
Business rules (range, format). Security (injection, XSS). Validate early.
Fail fast với clear error.

**Common Issues:** SQL injection (parameterized query). NoSQL injection (validate
input to query). XSS (escape output). Path traversal. Oversized payload. Rate
limit. Document max size, format.

**Error Messages:** Don't leak internals. "Invalid input" not "SQL syntax error".
Field-level error. User-friendly. Detailed error cho developer (in non-prod).

**Library:** Use validation library. Schema-based. Don't hand-roll. Consistent
validation logic. Reuse schema (OpenAPI, JSON Schema).
"""  # noqa: E501

version = "0.0.1"
