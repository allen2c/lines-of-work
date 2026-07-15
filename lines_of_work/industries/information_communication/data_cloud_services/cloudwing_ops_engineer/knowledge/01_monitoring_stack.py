title = "监控栈概览"

content = """\
- 云翼科技采用混合监控架构：Prometheus + Thanos 作为指标存储，Grafana 作为可视化面板，Alertmanager 负责告警路由。针对阿里云、腾讯云、华为云、AWS中国区，分别部署云厂商原生监控代理（CloudMonitor、CloudWatch等）作为补充。
- 日志监控使用 ELK（Elasticsearch 7.17 + Logstash + Kibana）集中采集系统日志、应用日志、安全日志，保留周期为180天（等保要求）。关键业务日志需实时解析并触发告警（如错误日志关键字"FATAL"、"OOM"）。
- 网络监控通过 Prometheus Blackbox Exporter 探测公网/内网端点，每30秒一次，超时5秒视为失败。丢包率>1%或延迟>200ms触发Warning，>5%或>500ms触发Critical。
- 所有监控数据需打上标签：env（prod/staging/dev）、region（cn-beijing/cn-shanghai/cn-shenzhen）、service（web/db/cache）、team（ops/security）。标签规范遵循公司《监控元数据标准v2.3》。
"""

version = "0.0.1"
