"""Retest policy (zh-Hans)."""

title = "复测政策"

content = """
复测（retest）指对初次测试结果为 fail 的 die 或 wafer 再次测试。
合理的复测政策可减少误杀、提高良率，同时控制测试成本与流程复杂度。

**复测触发：** 可针对特定 fail 类型（如仅 contact fail）、
整片 fail 或随机 fail 比例过高时触发。有时对初测 fail 的
 die 自动复测一次，若通过则视为 pass 并记录为 retest pass。

**次数与条件：** 复测次数通常限制为 1～2 次，避免无限重测
掩盖真实缺陷。复测时需保证程式、探针卡与机台状态一致，
必要时清洁或重新对准。

**数据记录：** 复测结果与初测结果都需保留，用于区分
 consistent fail 与 intermittent/contact 相关 fail，
 并用于良率分析与程式优化。
"""

version = "0.0.1"
