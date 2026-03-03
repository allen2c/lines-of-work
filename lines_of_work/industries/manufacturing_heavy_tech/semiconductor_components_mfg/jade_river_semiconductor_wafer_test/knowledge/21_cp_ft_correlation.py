"""CP-FT correlation (zh-Hans)."""

title = "CP与FT相关性"

content = """
CP（晶圆测试）与 FT（成品测试）相关性是衡量晶圆测试有效性与一致性的
关键指标，用于发现误杀、漏杀与测试条件差异。

**理想关系：** CP pass 的 die 在封装后 FT 也应 pass；CP fail 的 die
不应流入封装。实际中因接触差异、封装损伤、测试程式差异等，会存在
一定 CP pass/FT fail 或少数 CP fail/FT pass 的情况。

**CP pass / FT fail：** 可能原因包括封装或组装引入的损伤、FT 测试
条件更严、或 CP 未覆盖的缺陷。需通过失效分析与数据统计区分
系统性还是随机性，并改进封装或测试流程。

**CP fail / FT pass：** 多为 CP 误杀，可能来自接触不良、程式
界限过严或设备波动。需优化 CP 条件、复测政策或界限，以减少
良率损失与不必要的封装浪费。
"""

version = "0.0.1"
