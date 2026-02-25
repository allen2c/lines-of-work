title = "Cơ bản ETL"

content = """
ETL (Extract, Transform, Load) là pattern chuẩn cho tích hợp dữ liệu giữa các hệ thống.
Mekong Delta Tech sử dụng ETL cho data pipeline và migration.

**Extract:** Lấy dữ liệu từ nguồn — API, database, file, message queue. Xử lý incremental
khi có thể (timestamp, watermark) để tránh full scan. Handle rate limit và pagination.

**Transform:** Clean, validate, map dữ liệu theo schema đích. Xử lý null, default values,
type conversion. Transform phải idempotent và deterministic khi có thể.

**Load:** Ghi vào đích — database, data warehouse, API. Upsert strategy cho update. Batch
insert khi có thể. Handle constraint violation và retry.

**Orchestration:** Dùng Airflow, Prefect, hoặc Dagster để schedule và monitor pipeline.
Track lineage và dependencies. Alert khi job fail.
"""  # noqa: E501

version = "0.0.1"
