"""Knowledge item: regresi dan pengujian smoke."""

title = "Regresi dan Pengujian Smoke"

content = """
Pengujian regresi memastikan bahwa perubahan baru tidak merusak fungsionalitas yang
sudah berjalan. Pengujian smoke adalah subset cepat untuk memvalidasi build dasar.

**Konteks:** Setiap commit atau merge berpotensi memperkenalkan regresi. Smoke test
memberikan umpan balik cepat; regresi penuh membutuhkan waktu lebih lama tetapi
memberikan jaminan lebih komprehensif sebelum rilis.

**Langkah Utama:**
1) Pilih subset smoke: alur kritis, login, pembayaran, integrasi utama.
2) Jalankan smoke pada setiap build; regresi penuh sebelum rilis.
3) Prioritaskan test case berdasarkan dampak bisnis dan frekuensi penggunaan.
4) Pertahankan suite regresi yang dapat dijalankan dalam waktu yang dapat diterima.
5) Lacak flakiness dan perbaiki atau karantina test yang tidak stabil.

**Kriteria Penerimaan:** Smoke lulus sebelum merge; regresi lulus sebelum rilis.
Flakiness di bawah ambang yang ditentukan.

**Kegagalan Umum:** Smoke terlalu panjang, regresi tidak dijalankan karena waktu,
atau test flaky yang mengaburkan hasil.
"""

version = "0.0.1"
