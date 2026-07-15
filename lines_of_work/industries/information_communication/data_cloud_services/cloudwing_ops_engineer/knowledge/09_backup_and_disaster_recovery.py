title = "备份与灾备策略"

content = """\
- 数据备份：核心数据库（MySQL、PostgreSQL）每日全量备份（凌晨01:00），每6小时增量备份。备份保留30天，异地备份（跨地域）保留7天。备份文件加密（AES-256），存储至对象存储（阿里云OSS、腾讯云COS）。
- 应用配置备份：所有Terraform状态文件、Ansible playbook、Docker Compose文件每日自动备份至GitLab仓库，并同步至异地仓库。
- 灾备切换：每季度执行一次灾备演练，模拟主地域（cn-beijing）故障，切换至备地域（cn-shanghai）。RTO目标≤30分钟，RPO≤15分钟。演练后需输出报告，改进切换流程。
- 备份恢复测试：每月随机抽取一个数据库备份进行恢复测试，验证数据完整性。测试结果记录在Confluence，失败需立即修复。
"""

version = "0.0.1"
