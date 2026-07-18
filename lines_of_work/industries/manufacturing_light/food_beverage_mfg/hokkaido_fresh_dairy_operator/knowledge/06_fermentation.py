title = "発酵工程（ヨーグルト・チーズ）"

content = """
- ヨーグルト：42℃で発酵、スターター（Lactobacillus bulgaricus, Streptococcus thermophilus）を添加。pHが4.5に達したら冷却開始（約4～5時間）。
- チーズ（カマンベール）：30℃で発酵、スターター（Penicillium candidum, Lactococcus lactis）を添加。pHが4.6に達したらカードカット。
- 発酵タンクは二重構造で温水循環。温度制御はPIDコントローラー、精度±0.5℃。
- pHはインラインセンサーで連続測定、1時間ごとに手動でも確認。pHメーターは毎日校正（pH4.0と7.0標準液）。
- 発酵過多（pHが目標より0.1以上低い）は酸味過剰、製品廃棄の可能性。早期発見が重要。
"""  # noqa: E501

version = "0.0.1"
