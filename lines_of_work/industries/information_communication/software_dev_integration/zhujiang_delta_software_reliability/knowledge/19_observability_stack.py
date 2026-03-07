"""Observability stack for Zhujiang Delta software reliability."""

title = "可观测性技术栈"

content = """
可观测性通过指标、日志和追踪理解系统行为，是可靠性工程的基础设施。

**指标（Metrics）：** 时序数据，如 QPS、延迟、错误率。用于 SLO 监控、容量规划和趋势分析。

**日志（Logs）：** 结构化日志便于检索。定义日志级别和采样策略，平衡可观测性与成本。

**追踪（Tracing）：** 分布式追踪展示请求跨服务的调用链，定位延迟和故障点。

**关联与告警：** 将指标、日志、追踪关联。告警规则基于 SLO 和业务影响，避免告警疲劳。
"""  # noqa: E501

version = "0.0.1"
