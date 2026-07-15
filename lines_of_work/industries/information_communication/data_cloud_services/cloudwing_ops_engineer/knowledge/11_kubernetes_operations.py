title = "Kubernetes集群运维要点"

content = """\
- 集群版本：生产环境使用Kubernetes v1.28，预发布v1.29。升级需遵循先升级控制平面再升级节点，每次升级一个次要版本。升级前需备份etcd快照。
- 节点管理：使用节点池（Node Pool）管理不同规格实例（通用型、计算型、内存型）。节点自动修复：若节点NotReady超过5分钟，自动驱逐Pod并重启节点。若连续3次重启失败，标记为故障并通知工程师。
- Pod资源限制：所有Pod必须设置requests和limits，CPU超卖比例不超过1:3，内存超卖比例不超过1:2。违反限制的Pod将被拒绝调度。使用Vertical Pod Autoscaler（VPA）建议值，但需人工审核后应用。
- 网络策略：默认拒绝所有入站流量，仅允许通过Ingress暴露的服务。使用Calico网络策略实现微隔离，每季度审计一次策略有效性。
"""

version = "0.0.1"
