"""Knowledge item: UU PDP dan kepatuhan data."""

title = "UU PDP dan Kepatuhan Data"

content = """
Undang-Undang Perlindungan Data Pribadi (UU PDP) Indonesia mengatur pengumpulan,
penyimpanan, dan pemrosesan data pribadi. Pengujian harus memastikan kepatuhan tanpa
membocorkan data sensitif.

**Konteks:** Klien di Indonesia wajib mematuhi UU PDP. Pelanggaran dapat mengakibatkan
denda dan kerusakan reputasi. Pengujian yang menggunakan data produksi atau data uji
yang tidak dianonimisasi menimbulkan risiko kepatuhan.

**Langkah Utama:**
1) Gunakan data sintetis atau teranonimisasi untuk pengujian.
2) Validasi bahwa fitur menghormati hak akses, koreksi, dan penghapusan data.
3) Periksa enkripsi dalam transit dan saat istirahat.
4) Dokumentasikan alur data dan basis hukum pemrosesan.
5) Hindari log atau dump yang mengandung data pribadi.

**Kriteria Penerimaan:** Pengujian tidak menggunakan data pribadi nyata. Fitur data
divalidasi untuk kepatuhan UU PDP.

**Kegagalan Umum:** Data produksi di lingkungan uji, log yang mengekspos PII, atau
pengabaian persetujuan dan hak subjek data.
"""

version = "0.0.1"
