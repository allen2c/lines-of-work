title = "Dasar ETL untuk Integrasi Data"

content = """
ETL (Extract, Transform, Load) adalah pola untuk memindahkan data dari sumber ke tujuan
dengan transformasi di antaranya. Umum untuk integrasi data warehouse, migrasi, dan
sinkronisasi skala besar.

**Extract:** Baca data dari sumber — database, API, file. Full extract vs incremental
(berdasarkan timestamp atau CDC). Pertimbangkan beban pada sumber; jadwalkan di off-peak.
Tangani schema drift dan perubahan format.

**Transform:** Bersihkan, validasi, pemetaan, agregasi. Normalisasi dan deduplikasi.
Enkripsi atau masking untuk data sensitif. Business rules dan kalkulasi turunan. Transform
bisa di aplikasi atau di engine (dbt, Spark, Pandas).

**Load:** Tulis ke target. Replace, append, atau upsert. Bulk load untuk volume besar.
Validasi integritas pasca-load. Metadata: kapan run, record count, checksum untuk audit.
"""  # noqa: E501

version = "0.0.1"
