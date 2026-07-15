title = "告警规则与阈值"

content = """\
- 计算资源：CPU使用率（平均1分钟）≥80%持续5分钟 → Warning；≥90%持续2分钟 → Critical。内存使用率≥85%持续3分钟 → Warning；≥92%持续1分钟 → Critical。磁盘IO等待时间≥20ms持续5分钟 → Warning；≥50ms持续2分钟 → Critical。
- 存储资源：根分区（/）使用率≥85%持续10分钟 → Warning；≥92%持续5分钟 → Critical。数据盘使用率≥90%持续15分钟 → Warning；≥95%持续5分钟 → Critical。inode使用率≥80%持续10分钟 → Warning；≥90%持续5分钟 → Critical。
- 网络资源：入/出带宽使用率≥80%持续5分钟 → Warning；≥95%持续2分钟 → Critical。TCP连接数（ESTABLISHED）超过基线值（历史均值+3σ）持续5分钟 → Warning；超过+5σ → Critical。
- 中间件：Redis内存使用率≥80%持续5分钟 → Warning；≥90%持续2分钟 → Critical。MySQL慢查询数（>1秒）每分钟超过50条持续3分钟 → Warning；超过200条 → Critical。Nginx 5xx错误率≥1%持续1分钟 → Warning；≥5%持续30秒 → Critical。
- 告警静默规则：计划内变更期间（变更窗口）自动静默相关资源告警，静默时长不超过6小时。静默需在变更申请中注明，并通知值班人员。
"""

version = "0.0.1"
