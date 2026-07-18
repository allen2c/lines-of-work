title = "メタデータタグ付け規則"

content = """
- 必須フィールド：Title、Artist、Album Artist、Album、Track Number、Total Tracks、Year、Genre、ISRC、Composer、Publisher、Copyright、Encoded By「SoundForge Studio」。
- ISRC 形式：`JP-XXX-YY-NNNNN`（XXX=事業者コード、YY=年、NNNNN=連番）、発行管理台帳で重複防止。
- BWAV Chunk：Originator「SFJ」、OriginatorReference「YYYYMMDD_ProjectCode」、TimecodeReference「24fps」。
- アートワーク：JPEG 3000×3000 px、sRGB、ファイル名 `cover.jpg`、埋め込み ID3v2.4 APIC フレーム。
- チェックリスト：納品前「Metadata_Checklist.xlsx」全項目✔、不備あれば修正後再エンコード。
"""  # noqa: E501

version = "0.0.1"
