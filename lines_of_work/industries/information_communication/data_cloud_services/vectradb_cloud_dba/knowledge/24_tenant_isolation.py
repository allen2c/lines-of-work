title = "Multi-Tenant Isolation Model"

content = """
- Logical isolation: every tenant has its own database within the cluster; PostgreSQL datistemplate false and datallowconn true only for the tenant DB; row-level security (RLS) enabled on shared tables where applicable.
- Physical isolation: Enterprise plan on dedicated hardware; pool of per-tenant bare-metal nodes; no shared cgroup between tenants.
- Connection limits: enforced at PgBouncer per-user, max_user_connections 50 for app roles, max_connections per cluster sized to vCPU * 100.
- Resource governors: Linux systemd slice with CPUQuota and MemoryMax per tenant database on shared clusters; MySQL MAX_QUERIES_PER_HOUR and MAX_UPDATES_PER_HOUR per user.
- Cross-tenant data access attempts: alert at the IAM broker and the database audit log; any hit opens a SEV1 security ticket.
"""  # noqa: E501

version = "0.0.1"
