"""Release data migration procedures."""

title = "Release Data Migration"

content = """
Data migrations executed during releases require careful planning and rollback capability.
Schema changes, data backfills, and archival jobs can cause downtime or data corruption if
executed incorrectly.

**Planning:** Document migration steps, dependencies, and estimated duration. Identify
backward-compatible vs. breaking changes. Run migrations in staging with production-like
data volumes. Define rollback steps before execution.

**Execution Order:** Apply schema changes before application code when possible, or use
expand-contract patterns. For large backfills, consider batched execution with checkpoints.
Monitor progress and resource usage during migration.

**Rollback:** Ensure migrations are reversible or that rollback procedures are tested.
For destructive migrations, maintain backups and define recovery procedures. Communicate
migration status to stakeholders.
"""

version = "0.0.1"
