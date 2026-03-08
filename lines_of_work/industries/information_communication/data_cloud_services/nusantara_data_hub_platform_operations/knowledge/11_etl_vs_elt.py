"""Knowledge: ETL vs ELT pattern comparison."""

title: str = "Perbandingan Pola ETL vs ELT"

content: str = """
ETL dan ELT adalah dua pola arsitektur untuk memindahkan dan mengolah data.

**ETL (Extract-Transform-Load):** Transformasi dilakukan di staging layer sebelum
data dimuat ke warehouse. Cocok untuk data yang perlu pembersihan berat atau schema
strict sebelum load.

**ELT (Extract-Load-Transform):** Data mentah dimuat dulu ke warehouse, transformasi
dilakukan di dalam warehouse. Menghemat waktu load dan memanfaatkan compute warehouse.

**Pilihan:** ELT lebih umum untuk cloud data warehouse (BigQuery, Snowflake, Delta Lake).
ETL tetap relevan untuk integrasi legacy atau kebutuhan compliance tertentu.
"""  # noqa: E501

version: str = "0.0.1"
