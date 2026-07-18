title = "ノイズフロア測定と許容基準"

content = """
- 測定環境：全機材電源 ON、マイクミュート、部屋無人、20 秒ピンクノイズ録音。
- 解析：Pro Tools「AudioSuite > Gain > Analyze」で RMS、Peak、スペクトル表示。
- 許容値：全帯域 RMS -90 dBFS 以下、20 Hz‑200 Hz -85 dBFS 以下、ハイフレーク 10 kHz‑20 kHz -95 dBFS 以下。
- 超過時対応：グラウンドループ確認（DI ボックス挿入）、電源フィルタ追加、ケーブル交換、再測定。
- 記録：測定日時、条件、数値を「Noise_Floor_Log.xlsx」に蓄積、トレンド監視。
"""  # noqa: E501

version = "0.0.1"
