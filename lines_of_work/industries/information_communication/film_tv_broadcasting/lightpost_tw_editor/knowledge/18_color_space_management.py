title = "色彩空間管理"

content = """
- 專案色彩空間設定：在DaVinci Resolve的「Project Settings」中設定「Color Science」為「DaVinci YRGB Color Managed」。
- 輸入色彩空間：根據攝影機選擇（如Sony S-Log3、ARRI LogC、RED Log3G10）。
- 時間線色彩空間：若為SDR設定為Rec.709 Gamma 2.4；若為HDR設定為Rec.2020 ST.2084。
- 輸出色彩空間：與時間線一致，除非客戶要求特定轉換。
- 使用「Color Space Transform」節點進行轉換時，需勾選「Use DRT」以獲得更好的色調映射。
"""

version = "0.0.1"
