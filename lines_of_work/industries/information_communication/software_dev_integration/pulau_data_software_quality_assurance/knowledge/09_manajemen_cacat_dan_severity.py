"""Knowledge item: manajemen cacat dan severity."""

title = "Manajemen Cacat dan Severity"

content = """
Manajemen cacat mencakup pelacakan, klasifikasi, prioritisasi, dan penutupan cacat.
Severity yang konsisten memungkinkan tim memutuskan apa yang harus diperbaiki terlebih dahulu.

**Konteks:** Pulau Data menggunakan Jira atau GitHub Issues untuk pelacakan. Severity
harus selaras dengan dampak bisnis: blocker menghentikan rilis, critical mempengaruhi
fitur utama, major/minor mempengaruhi pengalaman pengguna dengan tingkat berbeda.

**Langkah Utama:**
1) Laporkan cacat dengan langkah reproduksi yang jelas, lingkungan, dan dampak.
2) Klasifikasikan severity sesuai matriks: dampak x frekuensi.
3) Tetapkan owner dan tenggat waktu berdasarkan severity.
4) Lacak cacat hingga tertutup dan verifikasi perbaikan.
5) Analisis pola cacat berulang untuk perbaikan proses.

**Kriteria Penerimaan:** Semua cacat terdokumentasi dengan severity, owner, dan status.
Blocker dan critical ditutup atau diakui sebelum rilis. Pola cacat dianalisis berkala.

**Kegagalan Umum:** Severity tidak konsisten antar tim, langkah reproduksi tidak lengkap,
atau cacat tertunda tanpa alasan terdokumentasi.
"""

version = "0.0.1"
