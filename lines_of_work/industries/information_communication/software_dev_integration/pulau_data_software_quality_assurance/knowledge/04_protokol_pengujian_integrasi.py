"""Knowledge item: protokol pengujian integrasi."""

title = "Protokol Pengujian Integrasi"

content = """
Pengujian integrasi memverifikasi bahwa komponen sistem bekerja sama dengan benar. Protokol
yang terdefinisi memastikan pengujian dapat diulang dan hasilnya dapat dipercaya.

**Konteks:** Aplikasi modern terdiri dari banyak layanan: API, basis data, antrean pesan,
layanan pihak ketiga. Integrasi yang salah menyebabkan cacat yang sulit dilacak ke satu
komponen. Protokol yang jelas mengurangi waktu debug.

**Elemen Protokol:**
- **Lingkungan:** Dev/staging yang mirip produksi; data uji yang konsisten.
- **Urutan:** Ketergantungan antar komponen; urutan startup dan shutdown.
- **Isolasi:** Pengujian tidak saling mengganggu; cleanup setelah setiap run.
- **Waktu tunggu:** Timeout yang memadai untuk operasi asinkron.

**Praktik:** Gunakan container (Docker) untuk konsistensi. Dokumentasikan skenario integrasi
kritis. Otomasi dalam pipeline CI untuk deteksi dini.

**Kegagalan Umum:** Lingkungan yang tidak stabil, data uji yang berubah-ubah, atau timeout
terlalu pendek menyebabkan flaky test.
"""

version = "0.0.1"
