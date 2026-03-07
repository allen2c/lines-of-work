"""Database migration in releases knowledge item."""

title = "Database Migration in Releases"

content = """
Database migrations are high-risk changes. They can cause data loss, downtime, or
irreversible schema changes. They require careful planning and execution within
the release process.

**Backward Compatibility:** Migrations must be backward compatible with the previous
application version. Deploy application code that supports both old and new schema
before running migrations that break compatibility. Use expand-contract or parallel
change patterns.

**Rollback Plan:** Every migration needs a rollback script. Test rollback in staging.
Document rollback steps and estimated duration. For large tables, rollback may be
impractical; plan for forward-only fixes instead.

**Execution Order:** Run migrations as part of the deployment pipeline, before or
during application deployment, according to the migration strategy. Ensure migrations
run in a defined order. Use migration versioning (e.g., Flyway, Alembic).

**Monitoring:** Monitor migration duration and lock contention. Long-running
migrations may block deployments or cause timeouts. Use online migration tools for
large tables when available.

**Audit:** Log migration execution, duration, and outcome. Retain for compliance and
incident review.
"""

version = "0.0.1"
