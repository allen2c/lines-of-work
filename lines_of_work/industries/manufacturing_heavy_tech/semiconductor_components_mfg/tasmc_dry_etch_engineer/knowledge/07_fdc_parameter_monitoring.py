title = "FDC參數監控"

content = """
- FDC（Fault Detection and Classification）系統監控即時參數：RF Forward Power、Reflected Power、DC Bias、氣體流量（MFC）、腔體壓力、溫度（腔體壁、ESC、晶圓）、電極間距、He背壓（用於冷卻晶圓）。
- 每個參數設定上下警告界限（Warning Limit，±3σ）與行動界限（Action Limit，±5σ）。當參數超出警告界限時，系統自動發出黃燈警報；超出行動界限時發出紅燈警報並可能自動暫停機台。
- 每日需檢視所有腔體的FDC趨勢圖，特別注意緩慢漂移（Drift）現象，例如RF功率逐漸下降可能預示匹配網路老化。
- 若FDC顯示異常，需在30分鐘內到機台確認，並記錄於FDC日誌。若為持續性漂移，需開立Work Order請設備工程師檢查。
"""  # noqa: E501

version = "0.0.1"
