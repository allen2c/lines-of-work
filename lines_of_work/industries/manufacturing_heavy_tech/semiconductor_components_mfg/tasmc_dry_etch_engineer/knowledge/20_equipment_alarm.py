title = "機台警報"

content = """
- 常見機台警報代碼：RF Alarm（如RF Overload、Reflected Power High）、Vacuum Alarm（如Pressure Not Reaching Setpoint、Leak Rate High）、Gas Alarm（如MFC Flow Error、Gas Cylinder Empty）、Temperature Alarm（如ESC Temperature Out of Range）。
- 警報處理流程：1) 查看警報訊息與建議排除步驟（機台觸控螢幕顯示）；2) 嘗試重置（Reset）或執行機台自動恢復程序；3) 若無法排除，記錄警報代碼與時間，通知設備工程師；4) 若警報導致產品異常，立即Hold Lot。
- 警報頻率監控：每週統計各腔體警報次數，若某腔體警報次數異常增加（如>5次/週），需進行根本原因分析，可能為硬體老化或製程參數不匹配。
- 警報歷史查詢：透過機台Log系統可查詢過去30天警報紀錄，用於趨勢分析與預防保養規劃。
"""  # noqa: E501

version = "0.0.1"
