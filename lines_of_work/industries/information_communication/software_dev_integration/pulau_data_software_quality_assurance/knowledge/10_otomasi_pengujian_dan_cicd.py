"""Knowledge item: otomasi pengujian dan CI/CD."""

title = "Otomasi Pengujian dan CI/CD"

content = """
Otomasi pengujian terintegrasi dengan CI/CD memungkinkan feedback cepat dan konsisten
setiap kali kode berubah. Mengurangi risiko regresi dan mempercepat siklus rilis.

**Konteks:** Tim Pulau Data menggunakan GitHub Actions, GitLab CI, atau Jenkins.
Pengujian otomatis berjalan pada setiap commit atau pull request. Hanya kode yang
lulus pengujian yang dapat digabung atau dirilis.

**Langkah Utama:**
1) Integrasikan unit test, pengujian integrasi, dan pengujian kontrak dalam pipeline.
2) Gunakan paralelisasi untuk mempercepat eksekusi.
3) Konfigurasi quality gate: blokir merge jika test gagal atau coverage turun.
4) Simpan artefak: log, screenshot, trace untuk debugging.
5) Pertahankan stabilitas test: flaky test merusak kepercayaan pada pipeline.

**Kriteria Penerimaan:** Pipeline menjalankan test otomatis pada setiap perubahan,
quality gate ditegakkan, dan flaky test di bawah ambang yang ditentukan.

**Kegagalan Umum:** Test lambat memblokir developer, flaky test diabaikan, atau
quality gate dilewati tanpa proses pengecualian yang jelas.
"""

version = "0.0.1"
