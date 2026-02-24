title = "GraphQL Error Format"

content = """
GraphQL trả 200 với errors array. Partial success. Format chuẩn. Integration
handle GraphQL error đúng. Mekong Delta Tech follow spec.

**Structure:** errors array. Mỗi error: message, locations, path, extensions.
message cho human. extensions cho machine (code, etc). Path to field failed.
Locations (line, column). Comprehensive.

**Partial vs Total:** Một số field fail, một số succeed. Client check errors.
Decide handle. Nullable field = null khi error. Non-null = bubble up, parent
null. Document behavior.

**Client Handling:** Parse errors. Check path. Field-level error handling.
User-friendly message. Retry? Based on error type. Log. Correlate. Don't
assume success khi có data — check errors.

**Extensions:** Custom error code. Request ID. Stack trace (dev). Consistent.
Document extensions. Version. Client use for logic.
"""  # noqa: E501

version = "0.0.1"
