title = "納品フォーマット仕様とメタデータ"

content = """
- マスターファイル：WAV 48 kHz/24 bit、インターリーブ、dither 無し、ヘッド/テイル 0.5 s 無音。
- ステム：Drums、Bass、Guitars、Keys、Vocals、FX 各 WAV 48 kHz/24 bit、同一長。
- 配信用：MP3 320 kbps CBR、AAC 256 kbps VBR、LUFS -14 ±0.5、True Peak -1 dBFS。
- メタデータ：ID3v2.4（Title, Artist, Album, ISRC, Track Number, Year, Genre, Composer, Publisher）、BWAV Chunk（Originator, Timecode）。
- 納品媒体：クラウド共有リンク（有効期限 30 日）、USB‑C SSD（オプション）、納品書 PDF 同封。
"""  # noqa: E501

version = "0.0.1"
