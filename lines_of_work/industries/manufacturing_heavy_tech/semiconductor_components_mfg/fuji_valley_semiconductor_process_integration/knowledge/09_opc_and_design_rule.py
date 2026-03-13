"""OPC and design rule linkage (ja)."""

title = "OPC と design rule の連携"

content = """
OPC（ Optical Proximity Correction ）は、リソグラフィの光学限界を補正し、
設計意図に近いパターンをウェーハ上に転写するための処理です。

**design rule との関係:** OPC が適用可能な範囲が design rule の
最小 feature や spacing を制約します。 OPC が収束しないデザインは
製造不可とし、 design rule で禁止または警告します。

**検証:** OPC 後のマスクパターンとシミュレーション結果を、統合フローの
検証ステップに含めます。
"""  # noqa: E501

version = "0.0.1"
