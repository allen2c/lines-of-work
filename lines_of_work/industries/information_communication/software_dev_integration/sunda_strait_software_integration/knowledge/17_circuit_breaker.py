title = "Circuit Breaker untuk Ketahanan Integrasi"

content = """
Circuit breaker mencegah sistem terus memanggil layanan yang gagal, memberikan waktu
pemulihan dan menghindari kaskade kegagalan. Pola fundamental untuk integrasi yang tangguh.

**State:** Closed: permintaan mengalir normal. Open: permintaan langsung gagal tanpa
memanggil upstream; terjadi setelah threshold kegagalan. Half-Open: setelah timeout, uji
beberapa permintaan; jika sukses, tutup; jika gagal, buka lagi.

**Threshold dan Timeout:** Fail threshold: berapa kegagalan berturut-turut atau persentase
dalam window sebelum membuka. Timeout di state Open: kapan mencoba half-open. Sesuaikan
dengan karakteristik upstream (lambat vs down total).

**Implementasi:** Resilience4j, Polly, atau custom. Per circuit per dependency. Fallback:
return cached, default, atau degraded response saat open. Metric untuk state transition;
alert saat circuit membuka terlalu sering — mungkin indikasi masalah upstream kronis.
"""  # noqa: E501

version = "0.0.1"
