title = "Output Encoding"

content = """
Output encoding ngăn injection khi render data. Context-dependent (HTML, JS,
URL). Mekong Delta Tech encode output đúng context. Integration API trả data
— client responsible, nhưng API có thể return cho web — care.

**Context:** HTML: escape <, >, &, ", '. JavaScript: escape cho string. URL:
encodeURIComponent. JSON: library handle. SQL: parameterized, not concatenate.
Each context different rules.

**API Response:** JSON serialize handle escaping. But if API return HTML fragment,
client render — ensure encoding. Or API return plain text, client encode. Document
encoding assumption. Content-Type correct.

**Logging:** Log user input? Encode trước khi log. Tránh log injection. Sanitize.
Structured log — field value escaped. Don't execute log as code.
"""  # noqa: E501

version = "0.0.1"
