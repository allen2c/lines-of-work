title = "音效與對白同步"

content = """
- 使用「Auto Sync」功能（基於波形或時間碼）將獨立錄音的音軌與影片同步。
- 若無時間碼，手動對齊波形中的拍板聲（Clapper）或明顯的瞬態聲音。
- 同步後，檢查音畫延遲：使用「Audio Waveform」與「Video Frame」對比，確保誤差小於1幀（25fps下為40ms）。
- 多軌音訊（如對白、環境音、音樂）需分別放置於不同音軌，並標明軌道名稱（如Dialogue、Ambience、Music）。
- 輸出前，將所有音軌合併為立體聲（Stereo）或5.1環繞聲，並設定峰值音量不超過-3dBFS。
"""

version = "0.0.1"
