"""Multi-site test (zh-Hans)."""

title = "多工位测试"

content = """
多工位（multi-site）测试指在同一时刻对多颗 die 施加测试，由测试机
的多个 channel 或 site 并行驱动与采集，从而成倍提高产能。

**硬件要求：** 探针卡需具备多组探针与对应 pad 接触；测试机需有
足够引脚与资源支持多 site 的激励与比较。各 site 的电气特性
应一致，否则需做 site 间校准或补偿。

**程式设计：** 程式需为多 site 分配资源、同步施加向量并汇总
结果。注意资源冲突（如共享电源、共享总线）与时序约束；
多 site 下的 test time 与单 site 的比值取决于瓶颈资源。

**良率与诊断：** 多 site 测试的 fail 需正确归属到对应 die，
 wafter map 与数据文件中的 site/die 映射须准确，以便
 后续分析与复测。
"""

version = "0.0.1"
