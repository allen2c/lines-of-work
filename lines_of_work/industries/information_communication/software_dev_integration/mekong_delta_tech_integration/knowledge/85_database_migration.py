title = "Database Migration trong Integration"

content = """
Integration thường cần DB schema change. Migration phải safe, reversible.
Mekong Delta Tech follow migration best practice.

**Expand-Contract:** Add column (nullable) → deploy → backfill → add constraint
→ deploy. Remove: add new, migrate, remove old. No big-bang. Both version
work during transition.

**Zero-Downtime:** Migration không lock table (when possible). Online migration
tool. Batch update. Index create concurrently. Test on copy of prod data.
Estimate duration.

**Rollback:** Backward compatible change. Forward migration only when safe.
Rollback plan. Backup. Test rollback. Document. Some change one-way —
careful.

**Integration:** Shared DB với partner? Coordinate. Contract. Version. Separate
DB preferred. API layer abstraction. Migration in integration layer.
"""  # noqa: E501

version = "0.0.1"
