title = "タイムコード同期手順"

content = """
- マスタークロック：Apollo X16 内部クロック（48 kHz）、Word Clock 出力→ SSL コンソール、外部レコーダー。
- MTC 入力：Ch17 に SMPTE 24 fps 入力、Pro Tools「Sync Mode」= MTC、Offset 0 フレーム。
- 確認手順：セッション開始前 1 分間「Timecode Verify」再生、Pro Tools カウンターと外部機器表示一致確認。
- ドリフト許容：±1 フレーム/分以内、超過時はクロックソース切替（内部→外部）再校正。
- 記録：同期ログ（日時、ドリフト量、対応）をメンテナンスノートに記入。
"""  # noqa: E501

version = "0.0.1"
