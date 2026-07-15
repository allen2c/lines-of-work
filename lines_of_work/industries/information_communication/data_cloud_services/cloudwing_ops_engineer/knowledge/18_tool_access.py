title = "常用工具与访问方式"

content = """\
- 堡垒机：JumpServer v3.10，所有SSH/RDP操作必须通过堡垒机，禁止直接SSH。堡垒机记录所有命令并录像，保留180天。
- 配置管理：Ansible Tower（AWX）用于批量执行任务，Playbook存储在GitLab，执行前需在AWX中创建作业模板。
- 容器管理：Rancher v2.8管理多个Kubernetes集群，通过RBAC控制权限。生产集群仅运维工程师有操作权限，开发人员只读。
- 云厂商控制台：阿里云RAM角色、腾讯云CAM角色、华为云IAM角色，使用SSO登录（Azure AD）。禁止使用根账号或长期AccessKey。临时AccessKey有效期最长1小时。
- 日志查询：Kibana（ELK）用于搜索日志，常用查询：`kubernetes.namespace: "prod" AND message: "ERROR"`。日志保留180天，超过后自动归档至冷存储。
"""

version = "0.0.1"
