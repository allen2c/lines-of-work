"""Thermal budget in integration (ja)."""

title = "統合における thermal budget"

content = """
thermal budget は、ウェーハが高温に曝される累積条件（温度×時間）の許容範囲です。
先行工程で形成した構造が後続の高温工程で劣化しないよう制御します。

**制約例:** シリサイド形成後の高温酸化は、シリサイドの相変化や
アグロメレーションを招くため避けます。 shallow junction の拡散防止のため、
後工程の thermal budget を抑制します。

**解析:** 各工程の温度と時間を積算し、先行構造への影響を評価。必要に応じて
フロー順序の変更や低温プロセスの採用を検討します。
"""  # noqa: E501

version = "0.0.1"
