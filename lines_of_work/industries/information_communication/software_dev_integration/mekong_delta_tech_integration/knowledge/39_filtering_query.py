title = "Filtering và Query"

content = """
List endpoint thường cần filter và sort. Design query API cho flexibility và
performance. Mekong Delta Tech follow pattern chuẩn cho filterable resources.

**Query Parameters:** ?status=active&created_after=2024-01-01. One param per
filter. Array: ?tags=vue&tags=react. Combine filters với AND. Document supported
filters. Validate và reject unknown.

**Operators:** Equality thường đủ. Có thể extend: _gt, _lt, _gte, _lte cho range.
_like cho search. _in cho multiple values. Prefix để tránh conflict (filter_).
Consistent naming.

**Sort:** ?sort=created_at&order=desc. Hoặc sort=-created_at (minus = desc).
Multiple sort: sort=status,created_at. Validate sort field. Default sort
(document). Index DB cho sort field.

**Performance:** Filter field nên có index. Avoid filter on non-indexed field
cho large table. Consider full-text search cho text. Limit result set.
"""  # noqa: E501

version = "0.0.1"
