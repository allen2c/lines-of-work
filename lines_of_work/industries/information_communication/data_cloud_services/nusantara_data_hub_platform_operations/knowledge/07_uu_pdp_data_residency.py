"""Knowledge: UU PDP and data residency requirements in Indonesia."""

title: str = "UU PDP dan Persyaratan Data Residency Indonesia"

content: str = """
Undang-Undang Perlindungan Data Pribadi (UU PDP) mengatur pemrosesan data pribadi
di Indonesia. Operasi platform harus memastikan kepatuhan.

**Data Residency:** Data pribadi warga Indonesia harus diproses dan disimpan di
wilayah Indonesia kecuali ada pengecualian berdasarkan persetujuan atau perjanjian
internasional.

**Prinsip:** Keterbatasan pengumpulan, tujuan spesifik, kebutuhan minimum, akurasi,
pembatasan penyimpanan, keamanan, dan akuntabilitas.

**Implikasi Operasional:** Pilih region/lokasi data center di Indonesia. Validasi
bahwa backup dan disaster recovery tidak memindahkan data ke luar wilayah tanpa
izin. Dokumentasikan alur data untuk audit.
"""  # noqa: E501

version: str = "0.0.1"
