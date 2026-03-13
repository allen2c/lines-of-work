"""Ion implant sequence in flow (ja)."""

title = "フローにおけるイオン注入シーケンス"

content = """
イオン注入はウェル形成、チャネルドーピング、ソース・ドレイン、 extension、
halo など多段階で行われます。注入順序は thermal budget とマスク層に依存します。

**拡散:** 高温工程により注入プロファイルが拡散します。 shallow extension は
後続の thermal budget を抑える必要があります。

**マスク:** フォトレジストやハードマスクで注入領域を制御。マスクエッジでの
チャネリングやスカッタリングが design rule に影響する場合、マージンを
設けます。
"""  # noqa: E501

version = "0.0.1"
