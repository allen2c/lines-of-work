title = "Penanganan Error dan Strategi Retry"

content = """
Jaringan dan sistem terdistribusi gagal. Integrasi yang handal harus menangani kegagalan
sementara dan permanen dengan jelas, mencegah kehilangan data dan kaskade kegagalan.

**Klasifikasi Error:** Transient (timeout, 503, network blip) — retry masuk akal. Permanent
(400, 404, 422) — retry tidak membantu; perbaiki permintaan atau data. Rate limit (429) —
backoff dan retry setelah header Retry-After atau interval eksponensial.

**Exponential Backoff:** Tunggu 1s, 2s, 4s, 8s... antara retry. Jitter (randomisasi) hindari
thundering herd saat banyak klien retry bersamaan. Batasi jumlah retry maksimum.

**Idempotensi:** Pastikan operasi aman diulang. Gunakan idempotency key pada permintaan
create/update. Server harus mengenali duplikat dan mengembalikan hasil yang sama tanpa
efek samping ganda. Log setiap retry untuk analisis.
"""  # noqa: E501

version = "0.0.1"
