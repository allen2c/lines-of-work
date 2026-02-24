title = "FTTHアーキテクチャ概要"

content = """
FTTH（Fiber To The Home）は光ファイバを顧客宅まで引き込むアクセス方式である。
Fuji Wave Telecomの主流サービスであり、GE-PON方式を採用している。

**OLTとONU:** 局側のOLT（Optical Line Terminal）が複数顧客の光信号を多重化する。
宅内のONU（Optical Network Unit）が光を電気信号に変換し、ルーターやPCと接続する。

**光スプリッター:** 1本の光ファイバを複数顧客で共有するため、光スプリッターで分岐する。
分岐比は1:32や1:64が一般的。分岐点が物理障害の多発箇所となり得る。

**波長分割:** 上り・下りで異なる波長を使用する。上り1310nm、下り1490nmがGE-PONの標準。
OLT側の光レベル監視により、光経路の劣化を早期に検知できる。
"""  # noqa: E501

version = "0.0.1"
