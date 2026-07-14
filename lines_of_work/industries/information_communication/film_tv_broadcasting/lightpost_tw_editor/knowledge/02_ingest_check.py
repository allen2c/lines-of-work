title = "素材匯入檢查流程"

content = """
- 接收素材後，立即使用「MediaInfo」或「DaVinci Resolve」檢查檔案格式、解析度、幀率、編碼。
- 確認無壞檔：使用「ffmpeg -v error」指令掃描所有影片檔，或使用「DaVinci Resolve」的「Media Management」功能。
- 若發現壞檔，立即通知攝影組並保留原始檔案，勿刪除。
- 記錄素材清單（Excel或Google Sheets），包含：檔名、時間長度、解析度、幀率、色彩空間、音軌數量。
- 對於RAW檔（如R3D、BRAW），需確認攝影機韌體版本與DaVinci Resolve相容性。
"""

version = "0.0.1"
