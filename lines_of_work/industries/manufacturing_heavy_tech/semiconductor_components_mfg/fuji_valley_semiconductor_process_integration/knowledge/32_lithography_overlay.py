"""Lithography overlay in integration (ja)."""

title = "統合におけるリソグラフィ overlay"

content = """
overlay は、複数マスク層の位置合わせ精度です。多重パターニングや
多層配線では overlay がデバイス機能と歩留まりに直接影響します。

** overlay budget:** 各層ペアに許容 overlay を割り当て、マスク製作、
露光装置、アライメントの寄与を分解します。

** design rule:** overlay 誤差を考慮した enclosure、 spacing、
anti-spacing を design rule で定義し、最悪 overlay でも短絡や
パターン欠損が発生しないようにします。
"""  # noqa: E501

version = "0.0.1"
