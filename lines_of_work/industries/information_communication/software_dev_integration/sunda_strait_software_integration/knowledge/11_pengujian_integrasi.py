title = "Pengujian Integrasi"

content = """
Pengujian integrasi memvalidasi bahwa alur end-to-end antara sistem berfungsi benar.
Tanpa pengujian yang memadai, bug terdeteksi di produksi dengan dampak bisnis tinggi.

**Contract Testing:** Konsumen dan penyedia API menyepakati kontrak (format, schema).
Pact, OpenAPI, atau Postman dapat digunakan. Memvalidasi kompatibilitas tanpa menjalankan
semua sistem bersamaan. Lakukan sebelum deploy untuk mencegah breaking changes.

**Integration Test:** Jalankan sistem nyata atau stub yang realistis. Uji alur lengkap:
permintaan masuk, transformasi, panggilan ke sistem eksternal, respons. Gunakan environment
terisolasi; jangan uji terhadap produksi. Seed data konsisten untuk reproducibility.

**Chaos dan Resilience:** Uji perilaku saat sistem eksternal lambat atau down. Latency
injection, fault injection. Pastikan circuit breaker, timeout, dan fallback berfungsi.
"""  # noqa: E501

version = "0.0.1"
