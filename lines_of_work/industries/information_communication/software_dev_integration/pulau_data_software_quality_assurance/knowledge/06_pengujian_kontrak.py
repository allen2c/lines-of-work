"""Knowledge item: pengujian kontrak."""

title = "Pengujian Kontrak"

content = """
Pengujian kontrak memvalidasi bahwa antarmuka antara layanan atau modul mematuhi spesifikasi
yang disepakati. Penting untuk sistem terdistribusi dan arsitektur mikroservis.

**Konteks:** Pulau Data sering mengintegrasikan aplikasi dengan API pihak ketiga, layanan cloud,
dan modul internal. Perubahan pada satu pihak dapat merusak pihak lain tanpa peringatan.
Pengujian kontrak mendeteksi ketidakcocokan sebelum rilis.

**Langkah Utama:**
1) Dokumentasikan kontrak API: skema request/response, kode status, header wajib.
2) Gunakan alat seperti Pact atau Spring Cloud Contract untuk menghasilkan test.
3) Jalankan pengujian kontrak dalam pipeline CI sebelum pengujian integrasi penuh.
4) Versikan kontrak dan pantau kompatibilitas mundur.
5) Eskalasi ketika kontrak dilanggar oleh pihak ketiga atau tim lain.

**Kriteria Penerimaan:** Semua kontrak kritis terdokumentasi, test otomatis berjalan di CI,
dan pelanggaran dilaporkan dengan jelas kepada pemilik kontrak.

**Kegagalan Umum:** Kontrak tidak diperbarui saat API berubah, mengabaikan edge case,
atau tidak memisahkan kontrak consumer dan provider.
"""

version = "0.0.1"
