title = "Integration and Webhook Support"

content = """
Integrations (webhooks, APIs, Zapier, etc.) extend product functionality.
When they fail, support must distinguish configuration errors from product
bugs or third-party issues.

**Common Failures:** Authentication expiry, payload changes, endpoint
deprecation, or rate limits. Guide users through re-authentication
and configuration checks.

**Logs and Debugging:** Request webhook delivery logs, response codes,
and payload samples when investigating. Many products provide developer
or webhook logs in the dashboard.

**Third-Party Limits:** Integration partners have their own rate limits
and SLAs. Escalate when the issue appears to be on the partner side.
"""  # noqa: E501

version = "0.0.1"
