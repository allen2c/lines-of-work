"""Lithography and etch module interaction (ja)."""

title = "リソグラフィとエッチングの相互関係"

content = """
リソグラフィで転写したパターンは、エッチングで基板・薄膜に転移されます。
両者の整合が pattern fidelity を決定します。

**選択比:** エッチングのマスク材と被エッチ材の選択比が不十分だと、
マスク消耗により転写パターンが崩れます。マスク厚とエッチ深度のバランスを
 design rule に反映します。

** LER/LWR:** リソグラフィの Line Edge Roughness はエッチ後も残るため、
電気特性に影響します。多重パターニングでは分割パターン間の LER 相関も
考慮します。
"""  # noqa: E501

version = "0.0.1"
