title = "システム連携"

content = """
- 主要連携：OMS↔WMS（REST/JSON、5分バッチ）、WMS↔TMS（CSV/日次）、WMS↔ERP（在庫・仕入、リアルタイムMQ）。
- APIバージョン管理：v1.3固定、破壊的変更は3ヶ月前告知・並行運用期間2週間。
- 障害検知：API応答時間＞3sまたはエラー率＞1%でアラート、自動フェイルオーバー（キャッシュ在庫参照）。
- 連携ドキュメント：OpenAPI仕様書をConfluenceで管理、変更履歴はGitで履歴管理。
"""  # noqa: E501

version = "0.0.1"
