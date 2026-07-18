title = "信号フローとルーティング設計"

content = """
- マイク → プリアンプ（Neve 1073）ゲイン 30‑45 dB → ラインレベル → Apollo X16 ラインイン（Ch1‑8） → Pro Tools トラック入力。
- ライン入力（シンセ、サンプラー）は TRS バランス → Apollo ラインイン（Ch9‑16）直接。
- モニターバス：コンソール Main L/R → Genelec 8341A、Cue Mix 1/2 → ヘッドフォン分配器（Beyerdynamic DT 770 Pro ×4）。
- インサートポイント：EQ（FabFilter Pro-Q 3）、コンプレッサー（SSL G-Master Buss）をプロセッサーとして挿入可能。
- タイムコード：MTC 入力（Ch17）→ Pro Tools シンクマスター、外部マスターレコーダー同期用。
"""  # noqa: E501

version = "0.0.1"
