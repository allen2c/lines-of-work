title = "オートメーション作成・管理手順"

content = """
- モード：Touch → Write → Latch → Read の順で切替、最終は Read 固定。
- パラメータ別レイヤー：Volume、Pan、Send Level、Plugin Parameter（EQ Gain、Comp Threshold）を個別レーンに記録。
- スナップショット：セッション終了時に「Automation Snapshot」保存、バージョン名 `Auto_v01` 等。
- 編集ルール：微調整 0.1 dB 単位、フェードイン/アウト 10 ms 以上、クリップ境界で自動スムージング。
- 共有：アシスタントに「Automation Export」で `.xml` 出力、レビュー後再インポート。
"""  # noqa: E501

version = "0.0.1"
