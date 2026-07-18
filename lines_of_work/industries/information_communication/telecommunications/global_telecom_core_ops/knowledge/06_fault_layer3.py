title = "網路層故障排除步驟"

content = """
*   使用 ping 與 traceroute 測試網元間連線性，確認延遲與封包損失率。
*   檢查路由表（Routing Table）與 BGP 鄰居狀態，確保路徑無中斷。
*   驗證 VLAN 設定與 IP 地址配置，排除子網掩碼錯誤導致之通訊失敗。
*   抓取封包（Packet Capture）分析 SIP 或 Diameter 信令是否完整傳輸。
*   若發現路由迴圈，立即隔離異常節點並通知網路架構師調整策略。
"""  # noqa: E501

version = "0.0.1"
