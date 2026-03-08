"""Knowledge: Data lakehouse architecture concepts."""

title: str = "Konsep Arsitektur Data Lakehouse"

content: str = """
Data lakehouse menggabungkan fleksibilitas data lake dengan tata kelola data warehouse.
Platform Nusantara Data Hub menggunakan pola ini.

**Lake:** Penyimpanan data mentah dalam format terbuka (Parquet, ORC). Skema-on-read
memungkinkan fleksibilitas. Cocok untuk data belum terstruktur atau berubah-ubah.

**House:** Layer terstruktur dengan ACID, indexing, dan optimasi query. Mendukung
BI dan analytics dengan performa tinggi.

**Unified:** Satu platform untuk batch, streaming, ML, dan BI. Mengurangi duplikasi
dan complexity integrasi.
"""  # noqa: E501

version: str = "0.0.1"
