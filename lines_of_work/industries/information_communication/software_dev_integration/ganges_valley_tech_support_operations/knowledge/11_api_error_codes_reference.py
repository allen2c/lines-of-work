title = "API Error Codes and Common Responses"

content = """
APIs return standardized error codes. Understanding them helps diagnose issues and
provide accurate guidance without unnecessary escalation.

**HTTP Status Classes:** 4xx indicates client error (bad request, auth failure,
not found); 5xx indicates server error. 401/403 point to authentication or
authorization; 429 indicates rate limiting.

**Application-Specific Codes:** Many APIs include custom error codes in the response
body. Reference the product's API documentation for code meanings. Document new
codes when encountered.

**Rate Limiting:** 429 responses often include Retry-After headers. Advise users on
throttling behavior and recommended retry intervals.
"""  # noqa: E501

version = "0.0.1"
