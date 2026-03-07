"""API testing knowledge for Zhujiang Delta software reliability."""

title = "API 测试"

content = """
API 测试验证服务接口的契约、响应格式和错误处理。在高流量 API 驱动服务中，接口稳定性直接影响业务可用性。

**契约验证：** 确认请求与响应的 schema 符合文档定义。使用 OpenAPI 或类似规范生成并执行契约测试。

**状态码与错误处理：** 验证正常路径返回 2xx，错误路径返回正确的 4xx/5xx 及错误体格式。边界条件（空输入、超长字段、非法字符）需覆盖。

**性能与限流：** 在接近生产负载下测试响应时间、吞吐量和限流行为。识别慢端点与超时风险。

**认证与授权：** 验证 token、API key 和权限控制逻辑。确保未授权请求被正确拒绝。
"""  # noqa: E501

version = "0.0.1"
