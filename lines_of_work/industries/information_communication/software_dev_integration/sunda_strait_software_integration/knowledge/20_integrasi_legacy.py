title = "Integrasi dengan Sistem Legacy"

content = """
Banyak perusahaan memiliki sistem lama (mainframe, ERP on-premise, database warisan) yang
harus diintegrasikan dengan aplikasi modern. Tantangannya: protokol kuno, dokumentasi
kurang, dan tim yang mengenal sistem menipis.

**Assessment:** Inventarisasi interface yang tersedia — file transfer, database direct,
API wrapper jika ada. Dokumentasi dan runbook. Tim yang masih memahami sistem. Identifikasi
data kritis dan frekuensi perubahan.

**Adapter Pattern:** Bangun layer adapter yang menerjemahkan antara format modern (REST,
JSON) dan format legacy (flat file, XML, proprietary). Adapter menangani transformasi,
retry, dan logging. Isolasi logika legacy dari aplikasi baru.

**Strategi Incremental:** Jangan big-bang. Mulai dengan read-only integrasi. Tambah write
secara bertahap. Pertimbangkan strangler fig pattern — ganti fungsi satu per satu sambil
mempertahankan legacy berjalan. Rencanakan sunset legacy dengan roadmap jelas.
"""  # noqa: E501

version = "0.0.1"
