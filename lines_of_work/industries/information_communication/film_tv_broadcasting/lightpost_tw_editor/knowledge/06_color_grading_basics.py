title = "一級調光基本原則"

content = """
- 使用DaVinci Resolve的「Color」頁面，先進行一級調光：調整曝光、對比、白平衡、飽和度。
- 使用波形監視器（Waveform）與向量示波器（Vectorscope）確保亮度範圍在0-100 IRE（Rec.709）或0-1023（10-bit）。
- 膚色線（Flesh Line）應落在向量示波器的膚色區域（約130度方向）。
- 黑位設定：確保陰影不低於0 IRE（避免裁切），白位不超過100 IRE（避免過曝）。
- 使用「Color Space Transform」功能進行色彩空間轉換（如S-Log3 to Rec.709）。
"""

version = "0.0.1"
