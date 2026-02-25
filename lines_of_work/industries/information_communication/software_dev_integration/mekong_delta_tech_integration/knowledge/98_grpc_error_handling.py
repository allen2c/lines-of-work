title = "gRPC Error Handling"

content = """
gRPC dùng status codes và metadata. Khác HTTP. Integration cần handle đúng.
Mekong Delta Tech standardize gRPC error.

**Status Codes:** OK, INVALID_ARGUMENT, NOT_FOUND, UNAVAILABLE, etc. Map
business error to code. Consistent. Document. Client handle by code. Don't
abuse UNAUTHENTICATED vs PERMISSION_DENIED.

**Details:** Structured error details. Protocol Buffer. Type URL. Client
parse. Retryable vs not. Localized message. Debug info. Don't leak internal.

**Metadata:** Trailers. Error details in metadata. Correlation ID. Request
info. Client read. Log. Propagate. Standard metadata keys.

**Client:** Check status. Parse details. Retry based on code. Fallback.
Circuit breaker. Don't ignore error. Handle UNAVAILABLE, DEADLINE_EXCEEDED.
"""  # noqa: E501

version = "0.0.1"
