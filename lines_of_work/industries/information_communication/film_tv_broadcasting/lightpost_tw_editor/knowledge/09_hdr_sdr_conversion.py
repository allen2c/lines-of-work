title = "HDR與SDR轉換規範"

content = """
- 台灣電視台目前仍以SDR（Rec.709）為主，但部分OTT平台（如Netflix）要求HDR（Rec.2020 PQ）。
- 若原始素材為HDR（如HLG或PQ），需使用「Color Space Transform」轉換為SDR，並手動調整亮度與對比。
- 轉換時，使用「Tone Mapping」功能（如「Luminance Mapping」或「Reinhard」），目標峰值亮度為100 nits。
- 輸出HDR版本時，需確認監視器支援HDR（至少1000 nits），並使用「HDR Scopes」檢查亮度分佈。
- 同時交付HDR與SDR版本時，需在檔名標註「_HDR」與「_SDR」。
"""

version = "0.0.1"
