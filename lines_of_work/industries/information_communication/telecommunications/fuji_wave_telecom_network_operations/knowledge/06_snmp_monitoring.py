title = "SNMP監視の仕組み"

content = """
ネットワーク機器の状態監視にはSNMP（Simple Network Management Protocol）が広く用いられる。
Fuji Wave Telecomの監視基盤もSNMPを主要な収集手段としている。

**OIDとMIB:** 各監視項目はOID（Object Identifier）で一意に識別される。MIBで定義された
標準OIDと、ベンダー固有のOIDを区別して理解する必要がある。

**ポーリング方式:** 監視サーバが定期的にget/walkで機器から情報を取得する。ポーリング間隔が
短いと機器負荷が増えるため、クリティカルな項目と通常項目で間隔を分ける。

**トラップ:** 機器が異常を検知した際に、主動的にトラップを送信する。トラップの遅延や欠落の
可能性があるため、ポーリングと併用して状態を把握する。
"""  # noqa: E501

version = "0.0.1"
