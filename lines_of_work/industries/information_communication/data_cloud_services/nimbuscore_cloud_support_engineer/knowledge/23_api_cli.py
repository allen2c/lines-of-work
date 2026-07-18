title = "API, CLI, and SDK Support"

content = """
- The NimbusCore CLI is `nc` (e.g., `nc ec2 describe-instances`). Output formats: `json`, `text`, `table`. Recommend `json` for any script that will be parsed.
- The CLI paginates by default with `--page-size` and `--max-items`; advise customers to use these instead of parsing partial output.
- API rate limits: 100 requests/second per account per service by default; the soft alert is at 80%. Bursts above the limit return HTTP 429 with a `Retry-After` header.
- For SDK issues, first confirm the SDK version; many "bugs" are actually resolved in newer releases. The current LTS is 1.34.x.
- Never have a customer paste a full request body into chat; ask for the headers, the resource path, and a redacted body instead.
"""  # noqa: E501

version = "0.0.1"
