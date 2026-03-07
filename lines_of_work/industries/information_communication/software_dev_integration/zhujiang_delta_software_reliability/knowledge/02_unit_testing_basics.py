"""Unit testing basics for Zhujiang Delta software reliability."""

title = "单元测试基础"

content = """
单元测试用于在隔离环境下验证单个代码单元（函数、类方法）的正确性。对快速反馈和早期缺陷发现至关重要。

**范围：** 验证每个单元是否履行单一职责。对外部依赖使用 mock 或 stub 隔离。

**命名：** 遵循 test_<函数>_<场景>_<预期> 模式。测试意图应能从名称中体现。

**AAA 模式：** 按 Arrange（准备）、Act（执行）、Assert（断言）组织。每个测试保持单一断言焦点。

**覆盖率：** 覆盖关键路径和边界情况。优先有意义的测试而非盲目追求 100% 覆盖率。
"""

version = "0.0.1"
