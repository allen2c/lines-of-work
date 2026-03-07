"""Knowledge item: quality gates dan kriteria rilis."""

title = "Quality Gates dan Kriteria Rilis"

content = """
Quality gates adalah titik pemeriksaan wajib yang harus dilewati sebelum kode atau fitur
maju ke tahap berikutnya. Kriteria rilis menentukan kapan produk siap untuk produksi.

**Konteks:** Dalam lingkungan Agile dengan rilis sering, quality gates mencegah cacat
kritis lolos ke produksi. Tanpa gates yang jelas, tekanan deadline dapat mendorong
rilis prematur dan meningkatkan risiko insiden.

**Langkah Utama:**
1) Definisikan gates untuk setiap tahap: commit, PR, staging, pre-production.
2) Tetapkan metrik yang dapat diukur: coverage, lint, keamanan, performa.
3) Dokumentasikan kriteria Go/No-Go untuk rilis produksi.
4) Otomasi pengecekan gates dalam pipeline CI/CD.
5) Tinjau dan perbarui gates secara berkala berdasarkan insiden dan umpan balik.

**Kriteria Penerimaan:** Gates terdokumentasi, terotomasi, dan dipatuhi. Keputusan
rilis didasarkan pada bukti, bukan tekanan waktu semata.

**Kegagalan Umum:** Gates yang terlalu longgar, bypass tanpa persetujuan, atau metrik
yang tidak mencerminkan risiko nyata.
"""

version = "0.0.1"
