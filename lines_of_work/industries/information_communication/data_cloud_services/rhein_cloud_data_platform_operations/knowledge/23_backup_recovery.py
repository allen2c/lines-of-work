title = "Backup and Recovery"

content = """
Data platform backups must cover databases, object storage, and configuration.
Snowflake provides Time Travel and Fail-safe; object storage (S3, ADLS) uses
versioning and cross-region replication. Backup retention aligns with RPO
requirements and compliance. Recovery procedures must be documented and tested
periodically. For pipelines, idempotent design allows replay from source or
checkpoint. Configuration (Airflow DAGs, dbt models) lives in version control;
restore from Git. Document RTO and RPO per data product and validate with
disaster recovery drills.
"""

version = "0.0.1"
