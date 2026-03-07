"""Defect severity and priority for Zhujiang Delta software reliability."""

title = "缺陷严重程度与优先级"

content = """
严重程度与优先级是缺陷分类的两个维度。正确划分有助于合理分配修复资源。

**严重程度：** Critical 导致系统不可用或数据丢失；High 影响核心功能；Medium 影响次要功能；Low 影响较小。

**优先级：** P1 需立即修复；P2 本迭代内修复；P3 可排入后续迭代；P4 可择机处理。

**组合使用：** 高严重度通常对应高优先级，但业务上下文可调整。如影响少量用户的 Critical 可能降为 P2。

**定期回顾：** 根据实际修复节奏与业务反馈，定期校准分类标准，保持团队共识。
"""

version = "0.0.1"
