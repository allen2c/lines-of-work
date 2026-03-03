"""Wafer mapping (zh-Hans)."""

title = "晶圆图与映射"

content = """
Wafer map 是将每颗 die 的测试结果（pass/fail 或 bin）以二维方式呈现在晶圆坐标上
的图形，是良率分析、制程诊断与客户交片的重要工具。

**坐标与排片：** 晶圆上的 die 通常按步进坐标（X, Y）或行列号索引。测试数据与
坐标的对应关系由探针台与测试程式的步进逻辑决定，须确保映射一致，否则 wafer map
会错位。

**显示方式：** 不同颜色或符号表示不同 bin 或 fail 类型。可叠加多片、多批做
 composite map 以观察共同模式；也可按测试项单独显示某类 fail 的分布。

**数据格式：** Wafer map 数据常以标准格式（如 STDF 中的 wafer 信息、die 坐标与
 result）或厂内格式存储，供分析软件、MES 与客户使用。坐标与 die 唯一标识需
 可追溯至 lot/wafer/die。
"""

version = "0.0.1"
