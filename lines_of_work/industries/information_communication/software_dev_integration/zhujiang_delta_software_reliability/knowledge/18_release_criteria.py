"""Release criteria for Zhujiang Delta software reliability."""

title = "发布标准"

content = """
发布标准定义构建何时可进入生产。珠江三角洲的 Go/No-Go 决策基于这些可验证的准则。

**测试通过率：** 所有关键和阻塞级测试必须通过。非关键失败需有 documented waiver。

**覆盖率：** 满足最低代码覆盖率阈值。新代码不得降低覆盖率。

**缺陷状态：** 存在未解决的严重或高优先级缺陷时阻止发布。低优先级项需有跟踪工单。

**文档与流程：** 发布说明、部署步骤和回滚流程需保持最新。
"""  # noqa: E501

version = "0.0.1"
