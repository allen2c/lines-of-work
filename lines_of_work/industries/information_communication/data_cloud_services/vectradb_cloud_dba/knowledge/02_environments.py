title = "Environment Tiers and Isolation"

content = """
- Four environment tiers: dev, staging, pre-prod, prod. All prod clusters run in isolated VPCs with dedicated security groups; staging and pre-prod share a non-production VPC.
- Network policy: prod databases accept connections only from the tenant production application VPC via VPC peering or Transit Gateway. No public IP, no SSH bastion; access is via bastion-prod-use1.vectradb.internal with MFA plus SSH key.
- Maintenance windows are tenant-defined in UTC; defaults are Sun 02:00 to 04:00 for prod, any time for dev.
- Naming convention: tenant_slug-env-engine-shard, for example acme-prod-pg-01. Schemas inside a database follow app_<service>_<env> to keep blast radius small.
"""  # noqa: E501

version = "0.0.1"
