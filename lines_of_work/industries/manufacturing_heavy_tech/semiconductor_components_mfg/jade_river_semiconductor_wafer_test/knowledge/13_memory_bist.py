"""Memory BIST (zh-Hans)."""

title = "内存内建自测"

content = """
内存 BIST（Built-In Self-Test）是芯片内嵌的电路，对嵌入式存储器（SRAM、
eDRAM 等）执行预设的读写与比对序列，无需测试机提供大量向量即可检测
存储单元与周边逻辑缺陷。

**测试流程：** 测试机通过少量引脚启动 BIST、选择测试算法（如 March）、
等待 BIST 完成并读取 pass/fail 或错误信息。BIST 在片内产生地址、数据
与比较，可大幅减少测试时间与引脚数。

**算法与覆盖：** March 类算法可检测单元 stuck-at、transition 与 coupling
等故障。不同产品可能支持多种算法或配置，测试程式须与设计文档一致。

**良率分析：** BIST fail 可带出 fail 地址或 bit 信息，用于区分单比特
失效、整行/整列失效或系统性失效，支持制程与设计诊断。
"""

version = "0.0.1"
