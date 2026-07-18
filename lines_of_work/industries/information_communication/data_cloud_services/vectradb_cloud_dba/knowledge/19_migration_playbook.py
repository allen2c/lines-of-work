title = "Database Migrations"

content = """
- Cross-engine migration: use pgloader (PostgreSQL from MySQL), mysql-workbench (MySQL from PostgreSQL via CSV staging), or the engine vendor DM tool. Plan for 2x peak load during cutover.
- Cross-region migration: logical replication via pglogical for PostgreSQL or mongo-sync for MongoDB; verify with row-count diff plus checksum on the 100 largest tables.
- Major version upgrade on a live cluster: pg_upgrade --link --check first, then --jobs 4 for parallel restore of catalog, then ANALYZE on the new cluster, then cutover with a 30 s read-only window.
- Cutover window: announce at T-24 h and T-1 h, freeze writes at T-0, drain connections, point app to new endpoint, unfreeze, monitor lag for 1 h.
"""  # noqa: E501

version = "0.0.1"
