"""Handoff to assembly (zh-Hans)."""

title = "与封装交接"

content = """
晶圆测试完成后，合格 die 或 wafer 需向封装（assembly）环节
交接，确保流向、数量与数据一致，并满足客户与生产排程。

**交接内容：** 物理上为测试通过的 wafer 或已标记的 die；
 数据上为测试结果、wafer map、bin 信息、lot/wafer ID
 及客户要求的格式与字段。封装据此进行排程、打标与
 追溯。

**规格符合性：** 交接前确认测试规格、程式版本与
 客户特殊要求均已满足；异常批或工程批
 不得混入量产交接 unless 经批准。

**追溯链：** 从测试到封装的 lot/wafer/die 标识
 需连续可查，便于客诉或 FA 时回溯到
 测试条件与数据。
"""

version = "0.0.1"
