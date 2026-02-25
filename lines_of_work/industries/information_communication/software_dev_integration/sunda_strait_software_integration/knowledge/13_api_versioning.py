title = "Versioning API untuk Kompatibilitas"

content = """
API berevolusi. Versioning yang terencana memungkinkan perubahan tanpa merusak konsumen
yang ada. Tanpa strategi, upgrade menjadi risky dan konsumen terpaksa mengikuti perubahan
mendadak.

**Strategi Umum:** URL path (/v1/resource, /v2/resource) — paling eksplisit. Header
(Accept: application/vnd.api+json;version=2). Query parameter (?version=2) — kurang
disarankan untuk REST. Pilih satu dan konsisten.

**Breaking vs Non-Breaking:** Non-breaking: tambah field opsional, tambah endpoint.
Breaking: hapus/ubah field, ubah semantik, ubah kode status. Breaking changes = versi baru.
Komunikasikan deprecation jangka panjang (misalnya 6-12 bulan) sebelum menghapus versi lama.

**Dokumentasi:** Changelog untuk setiap versi. OpenAPI/Swagger per versi. Beri panduan
migrasi untuk konsumen yang pindah dari v1 ke v2. Pertahankan versi lama hingga tidak
ada konsumen aktif (monitoring penggunaan).
"""  # noqa: E501

version = "0.0.1"
