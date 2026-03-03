"""Failure analysis handoff (zh-Hans)."""

title = "失效分析交接"

content = """
晶圆测试发现的异常或客户退回需进行失效分析（FA）时，测试部门需
按规范提供样本与数据，便于 FA 团队定位根因。

**样本选择：** 根据 fail 模式、wafer map 与客户要求选择具代表性的
 fail die（及必要时 good die 对照）。记录 die 坐标、lot/wafer ID、
 测试程式版本与关键测试结果，随样本一起移交。

**数据提供：** 测试数据文件、wafer map、fail 项与 cycle 信息、
 参数分布等。若 FA 需要特定格式或额外量测，测试方配合
 提取或重测。

**流程与追溯：** 样本移交需有交接单或系统记录，确保 FA 结果
 可回溯到具体 lot/wafer/die 与测试条件。FA 结论反馈回
 测试与制程，用于界限调整、程式优化或制程改进。
"""

version = "0.0.1"
