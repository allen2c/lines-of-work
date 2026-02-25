title = "Pagination and Cursor-Based API Handling"

content = """
APIs use pagination for large
result sets. Support helps users
handle cursors, limits, and
page tokens correctly.

**Pagination Types:** Offset,
cursor, or page-based.
Document product-specific
behavior. Explain when to
use each.

**Common Errors:** Invalid
cursor, expired token, or
exceeding max page size.
Suggest retry with valid
cursor or smaller page size.

**Best Practices:** Recommend
cursor-based when available
for consistency. Avoid
deep offset pagination for
large datasets.
"""  # noqa: E501

version = "0.0.1"
