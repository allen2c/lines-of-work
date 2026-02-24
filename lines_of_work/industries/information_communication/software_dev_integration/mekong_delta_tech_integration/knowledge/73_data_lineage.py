title = "Data Lineage"

content = """
Data lineage track nguồn và flow của data. Quan trọng cho integration, compliance,
debug. Mekong Delta Tech document lineage cho critical data.

**What:** Source system, transformation, destination. Field-level. Flow diagram.
Metadata. When data flow. Who responsible. Dependency.

**Why:** Debug data issue. Impact analysis (change source → affect what).
Compliance (PDPA, data flow). Trust. Onboarding. Documentation.

**How:** Manual documentation. Automated (metadata collection). Tool: OpenLineage,
custom. Tag in pipeline. Store in catalog. Query lineage. Visualize.

**Integration:** Each integration step record. ETL job lineage. API data flow.
Event flow. Keep updated. Review when architecture change.
"""  # noqa: E501

version = "0.0.1"
