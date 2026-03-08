"""Knowledge: Data pipeline fundamentals for platform operations."""

title: str = "Dasar-Dasar Pipeline Data"

content: str = """
Pipeline data memindahkan dan mengolah data dari sumber ke tujuan. Operasi platform
perlu memahami arsitektur untuk troubleshooting.

**Komponen Umum:** Sumber (database, API, file) → ingestion layer → transform layer →
storage (data lake, warehouse) → consumption (BI, ML, aplikasi).

**Pola ETL/ELT:** ETL (Extract-Transform-Load) memproses sebelum menyimpan. ELT
(Extract-Load-Transform) memuat mentah dulu, lalu transform di warehouse.

**Kegagalan Umum:** Timeout koneksi, schema drift, kuota rate-limit terlewati, disk
penuh, dan dependency downstream gagal. Periksa log setiap stage untuk isolasi.
"""  # noqa: E501

version: str = "0.0.1"
