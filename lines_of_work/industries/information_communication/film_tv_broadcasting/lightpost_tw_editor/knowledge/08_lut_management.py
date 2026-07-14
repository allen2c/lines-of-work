title = "LUT管理與套用"

content = """
- 所有LUT檔案統一存放於NAS「/Volumes/LightPost_Assets/LUTs/」資料夾，依攝影機品牌分類（如Sony、ARRI、RED）。
- 套用LUT前，必須確認素材的色彩空間與LUT的輸入色彩空間匹配，否則會產生錯誤色彩。
- 使用「LUT」節點而非「Color Space Transform」時，需注意LUT不包含色域映射，可能導致色偏。
- 客戶提供的LUT需先進行測試，確認無過度裁切或異常色調，並記錄測試結果。
- 輸出交付時，若客戶要求保留LUT效果，需在調光完成後套用LUT並鎖定（Lock）節點。
"""

version = "0.0.1"
