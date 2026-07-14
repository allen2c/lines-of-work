title = "OSS 工具操作指南"

content = """
- NetAct（Nokia）：用於告警監控、配置管理、效能報表。常用指令：`alarm list severity=critical`、`cell status site=TPE001`。
- 自研 OSS 平台：整合 Google Maps 顯示站點狀態，支援 OTDR 軌跡查詢、電池電壓歷史曲線。
- 工單系統（ServiceNow）：建立、更新、查詢工單，使用「NOC-」前綴。必填欄位：站點 ID、告警代碼、影響範圍。
- 遠端登入工具：透過 SSH 或串列終端機（Console Server）連線至基地台設備，執行 CLI 指令（如 `show interface`、`reset rru`）。
- 備份還原：每日自動備份基地台配置至 FTP 伺服器，保留 30 天。還原前需確認版本相容性。
"""

version = "0.0.1"
