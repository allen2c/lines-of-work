title = "Phát triển SDK"

content = """
SDK wrapper API cho developer. Giảm boilerplate, type safety, best practice built-in.
Mekong Delta Tech cung cấp SDK cho popular languages khi API có user base đủ lớn.

**Design:** SDK = thin wrapper hoặc rich client. Thin: map method to HTTP. Rich:
retry, auth refresh, validation, helpers. Chọn theo complexity. Keep API as source
of truth. SDK generate từ OpenAPI khi có thể.

**Error Handling:** Map HTTP error sang typed exception. Retry logic. Don't swallow
error. Provide context (request_id, status code). Document exception hierarchy.

**Documentation:** Readme, quick start, API reference (from OpenAPI). Examples.
Changelog. Version với API. Publish to package manager (npm, PyPI).

**Testing:** Test against real API (sandbox) hoặc mock. Contract test. Integration
test. Multi-version test khi support nhiều API version.
"""  # noqa: E501

version = "0.0.1"
