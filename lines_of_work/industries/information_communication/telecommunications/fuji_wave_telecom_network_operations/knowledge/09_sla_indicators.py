title = "SLA指標と稼働率"

content = """
企業向けサービスのSLA（Service Level Agreement）には、稼働率、MTTR、MTBF等の指標が
定められる。運用担当はこれらの達成状況を常に意識する。

**稼働率:** 可用時間／（可用時間＋不可用時間）で表す。月次99.9%であれば、月の停波時間は
約43分以内に収める必要がある。計画停止は別扱いとする契約が多い。

**MTTR:** Mean Time To Repair。障害発生から復旧までの平均時間。切り分けの迅速さと
復旧手順の整備がMTTR短縮につながる。

**MTBF:** Mean Time Between Failures。障害発生間隔の平均。機器の品質と保守状態に依存する。
定期点検と予防的部品交換でMTBFを維持する。
"""  # noqa: E501

version = "0.0.1"
