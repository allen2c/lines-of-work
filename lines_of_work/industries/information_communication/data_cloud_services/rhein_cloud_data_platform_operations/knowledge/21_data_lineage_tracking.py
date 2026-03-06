title = "Data Lineage Tracking"

content = """
Data lineage describes the flow of data from source systems through transformations
to final consumption. Tracking lineage is essential for impact analysis, compliance
audits, and debugging. Rhein Cloud uses automated lineage from dbt, Airflow, and
data catalog tools. Lineage should capture table-to-table, column-to-column, and
job-to-job dependencies. When a source schema changes, lineage helps identify
affected downstream pipelines and consumers. Document both technical lineage
(actual data flow) and business lineage (logical data products).
"""

version = "0.0.1"
