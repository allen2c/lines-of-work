title = "測試分類站（Test & Sort）操作"

content = """
- 測試機台（Tester）與分類機（Handler）連線，依測試程式（Test Program）對每顆IC進行功能測試、DC參數測試、AC參數測試。測試項目數依產品複雜度，一般100-500項。
- 分類結果分為：Pass（良品）、Fail（不良品，細分為不同Bin code，如Bin1開路、Bin2短路、Bin3漏電流過大等）。每顆IC會雷射標記（Laser Mark）Bin code。
- 換線時需更換測試插座（Socket）與分類機的料管（Tube）或托盤（Tray）。插座壽命約10萬次測試，需定期清潔（每5000次用壓縮空氣吹淨）。
- 測試溫度設定：常溫25°C、高溫85°C、低溫-40°C（依客戶規格）。溫度穩定度需在±3°C內，每小時記錄溫度曲線。
- 常見異常：Contact Fail（接觸不良，導致誤判）、Overkill（良品被誤判為不良，目標<0.5%）、Underkill（不良品被誤判為良品，目標0%）。每批需執行Golden Sample比對。
"""  # noqa: E501

version = "0.0.1"
