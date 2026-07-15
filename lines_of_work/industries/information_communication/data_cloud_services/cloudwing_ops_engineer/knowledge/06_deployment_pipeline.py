title = "部署流水线规范"

content = """\
- 所有基础设施变更必须通过IaC（Terraform v1.5+，Ansible 2.15+）执行，禁止手动操作。代码仓库为GitLab，分支策略：main（生产）、staging（预发布）、dev（开发）。
- CI/CD流程：开发提交代码至dev分支 → GitLab CI自动运行lint、terraform plan、ansible-playbook --syntax-check → 合并至staging后自动部署到预发布环境 → 集成测试通过后，创建Merge Request至main → 运维工程师审核后合并，触发生产部署。
- 生产部署窗口：每周二、四凌晨02:00-06:00（UTC+8）。部署前需在Jira中提交变更申请（CR），包含变更描述、影响范围、回滚方案、测试结果。CAB（变更咨询委员会）每周一、三下午14:00审批。
- 部署后自动运行冒烟测试（Smoke Test），验证关键端点（如健康检查/health、API /v1/ping）返回200。若失败，自动回滚至上一版本，并通知工程师。
"""

version = "0.0.1"
