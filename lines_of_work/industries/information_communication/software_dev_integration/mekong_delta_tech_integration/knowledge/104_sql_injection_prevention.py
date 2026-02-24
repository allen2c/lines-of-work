title = "Phòng chống SQL Injection"

content = """
SQL injection critical security risk. Integration với DB. Mekong Delta Tech
enforce parameterized query everywhere. Never concatenate user input.

**Parameterized Query:** Placeholder. Bind parameter. Driver escape. No
interpretation. Prepared statement. Use always. No exception. Code review.
Lint rule.

**ORM:** ORM use parameterized. Don't raw query với concat. If raw, parameterize.
Escape khi absolutely must (rare). Avoid. Validate. Whitelist. Input validation
complement, not replace.

**Dynamic Query:** Table name, column — whitelist. Not from user. Validate
against known list. Careful. Audit. If user input, severe限制. Document.
Dangerous. Prefer static.

**Testing:** SQL injection test. Automated. Pentest. Fuzzing. Checklist. Never
ship với vulnerability. Security gate.
"""  # noqa: E501

version = "0.0.1"
