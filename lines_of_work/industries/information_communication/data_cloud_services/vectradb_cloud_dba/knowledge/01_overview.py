title = "Service Catalog and Cluster Inventory"

content = """
- Engines supported in production: PostgreSQL 16.2 and 16.3, MySQL 8.0.36, MongoDB 7.0.5, ClickHouse 23.8 LTS. Redis 7.2 is offered as a limited preview and is out of scope.
- Three plan tiers: Starter (1 vCPU, 2 GB RAM, 20 GB SSD, single node), Pro (4 vCPU, 16 GB RAM, 200 GB SSD, one replica), Enterprise (16 to 64 vCPU, 64 to 512 GB RAM, 1 to 5 TB NVMe, two replicas plus one delayed, optional cross-region read replica).
- Regions: us-east-1, us-west-2, eu-west-1 (Frankfurt), eu-north-1 (Stockholm), ap-southeast-1 (Singapore), ap-southeast-2 (Sydney). Data residency is locked at provision time; cross-region failover is opt-in per tenant contract.
- Every cluster is tagged with tier, engine, plan, region, compliance_scope (none, GDPR, ISO27001, SOC2+HIPAA), and business_owner. Tags are the source of truth for billing and SLO mapping.
"""  # noqa: E501

version = "0.0.1"
