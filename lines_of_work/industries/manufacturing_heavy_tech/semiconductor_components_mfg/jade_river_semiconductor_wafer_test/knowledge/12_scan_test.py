"""Scan test (zh-Hans)."""

title = "扫描测试"

content = """
扫描测试（scan test）利用设计中的可扫描链（scan chain）将内部触发器串成
移位寄存器，通过扫描输入施加测试向量并将响应移出，以检测组合逻辑与
触发器缺陷。

**基本原理：** 测试时芯片处于 scan 模式，向量通过 scan-in 引脚移入链中，
然后施加一个或多个 capture 时钟将结果捕获到触发器，再通过 scan-out 移出
与期望值比对。可达到较高的 stuck-at 与部分 delay 故障覆盖率。

**测试程式：** 向量通常由 ATPG 工具生成，以 STIL 或类似格式交付测试机。
程式需正确配置 scan 时钟、load/unload 时序与 compare 逻辑，并处理
多链、压缩（compression）等设计变体。

**良率与诊断：** Scan fail 可结合 fail  cycle 与逻辑诊断定位可疑网线或
单元，供制程或设计改进；与 CP/FT 的 scan 结果对比可区分为前道还是后道
引入的缺陷。
"""

version = "0.0.1"
