title = "機台概覽"

content = """
- 負責機台：LAM 2300（Dielectric Etch）、Applied Materials eMax（Conductor Etch）、TEL SCCM（用於特殊薄膜蝕刻）。每台機台配置4~6個反應腔（Chamber），每個腔體獨立控制RF功率、氣體流量、壓力與溫度。
- 關鍵參數範圍：RF Source Power 200~1500W，Bias Power 50~500W，腔體壓力 5~100 mTorr，氣體種類包含CF₄、CHF₃、O₂、Ar、Cl₂、BCl₃等，流量範圍 10~500 sccm。
- 機台狀態監控：透過FDC系統每0.1秒記錄一次參數，並與SPC管制圖連動。每日需檢視所有腔體的FDC趨勢，確認無異常漂移。
- 保養週期：腔體清潔（Wet Clean）每2000 RF小時或每週一次；預防火花清潔（Preventive Plasma Clean）每批產品後執行。耗材如聚焦環（Focus Ring）、靜電吸盤（ESC）壽命約3000~5000 RF小時，需定期更換。
"""  # noqa: E501

version = "0.0.1"
