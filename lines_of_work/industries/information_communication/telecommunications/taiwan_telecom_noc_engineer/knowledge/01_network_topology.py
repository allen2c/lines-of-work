title = "北台電信網路拓撲概覽"

content = """
- 無線接取網路（RAN）：採用 Nokia AirScale 與 Ericsson Radio System，支援 4G LTE（Band 1/3/7/8/28）及 5G NR（n1/n78/n79）。基地台分為宏站（Macro）、微站（Small Cell）及室內涵蓋（DAS）。
- 傳輸網路：骨幹以 100G/200G DWDM 光纖環為主，匯聚層使用 10G/25G IP-MPLS，接取層以 GPON 及微波（6-38GHz）連接偏遠站點。備援路由採用 1+1 或 1:1 保護。
- 機房分級：核心機房（Tier III）、區域機房（Tier II）、戶外機櫃（IP55）。每個基地台至少配備 4 小時電池備援，重要站點另備柴油發電機。
- 監控系統：使用 Nokia NMS（NetAct）與自研 OSS 平台，整合告警、效能、派工模組。
"""

version = "0.0.1"
