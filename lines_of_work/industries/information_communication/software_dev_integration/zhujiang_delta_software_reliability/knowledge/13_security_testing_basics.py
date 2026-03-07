"""Security testing basics for Zhujiang Delta software reliability."""

title = "安全测试基础"

content = """
安全测试识别认证、授权、数据保护和注入类漏洞。可靠性工程需将安全纳入质量门禁。

**常见漏洞：** SQL 注入、XSS、CSRF、不安全的反序列化、敏感数据泄露。使用 OWASP Top 10 作为检查清单。

**认证与授权：** 验证密码策略、会话管理、权限边界。确保横向和纵向越权被阻止。

**依赖扫描：** 对依赖库进行 CVE 扫描，在 CI 中集成。已知高危漏洞需在发布前修复或 documented waiver。

**渗透与合规：** 对关键服务进行定期渗透测试。金融、医疗等受监管行业需满足合规要求。
"""  # noqa: E501

version = "0.0.1"
