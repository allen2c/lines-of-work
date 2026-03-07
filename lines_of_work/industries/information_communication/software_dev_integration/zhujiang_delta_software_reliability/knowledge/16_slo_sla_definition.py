"""SLO/SLA definition for Zhujiang Delta software reliability."""

title = "SLO 与 SLA 定义"

content = """
SLO（服务级别目标）和 SLA（服务级别协议）将可靠性目标量化，指导资源投入和发布决策。

**SLO 指标：** 可用性（如 99.9%）、延迟（P99 < 200ms）、错误率（< 0.1%）。每个核心服务应有明确 SLO。

**错误预算：** 基于 SLO 计算允许的失败量。预算耗尽时收紧发布、加强测试或暂停非关键变更。

**SLA 与业务：** SLA 是与客户或内部承诺的合同条款。SLO 通常比 SLA 更严格，留出缓冲。

**监控与告警：** SLO 需有对应监控和告警。燃烧率告警在预算快速消耗时提前预警。
"""  # noqa: E501

version = "0.0.1"
