"""Design rule overview (ja)."""

title = "design rule の概要"

content = """
design rule は、製造プロセスで実現可能な幾何学的・電気的制約を設計者に
提供するルールの集合です。

**幾何学ルール:** 最小 line width、 space、 pitch、 enclosure、 overlap など。
リソグラフィとエッチングの能力に基づいて定義します。

**電気ルール:** 寄生容量、リーク、耐圧などの電気特性に紐づく制約。
プロセスパラメータとデバイス特性の相関から導出します。

**改訂:** プロセス改善や検証結果に応じて design rule を改訂する場合、
バージョン管理し、顧客への通知と PDK 更新を行います。
"""  # noqa: E501

version = "0.0.1"
