title = "SSL and Certificate-Related Issues"

content = """
SSL/TLS errors can block access to web applications. Common causes
include expired certificates, misconfiguration, or corporate
proxy inspection. Support troubleshoots within scope.

**User Environment:** Corporate proxies often intercept HTTPS.
Recommend users try from a non-corporate network or contact IT
to whitelist the domain. Personal devices and home networks
rule out proxy issues.

**Certificate Warnings:** Browsers show warnings for expired
or mismatched certs. If the issue is on our side, escalate to
Infrastructure. Do not advise users to bypass security warnings.
"""  # noqa: E501

version = "0.0.1"
