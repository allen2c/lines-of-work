title = "データセンターネットワークトポロジ"

content = """
- 基本構成：Leaf-Spineアーキテクチャ。Spineスイッチ4台（冗長）、Leafスイッチ各ラック2台（A系/B系）。全Leafが全Spineと接続（ECMP）。
- 冗長性：各テナントは2つのLeafに接続（Active/ActiveまたはActive/Standby）。BGP EVPN VXLANでオーバーレイネットワークを構築。
- 外部接続：キャリア回線はルーター（PE）を経由し、Spineに接続。インターネット接続はファイアウォールクラスターを経由。
- 管理ネットワーク：帯域外管理（OOB）用の独立したスイッチ群。全機器の管理IPはOOB経由でアクセス。
"""  # noqa: E501

version = "0.0.1"
