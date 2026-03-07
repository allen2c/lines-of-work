"""Knowledge item: pola retry dan ketahanan."""

title = "Pola Retry dan Ketahanan"

content = """
Sistem terdistribusi menghadapi kegagalan sementara: timeout jaringan, layanan
sibuk, atau rate limiting. Pola retry dan backoff yang tepat meningkatkan ketahanan.

**Konteks:** Integrasi dengan API pihak ketiga, layanan cloud, atau antrean pesan
sering gagal secara transien. Retry tanpa batas atau tanpa backoff dapat memperburuk
masalah dan menyebabkan cascading failure.

**Langkah Utama:**
1) Identifikasi operasi yang dapat di-retry (idempotensi).
2) Terapkan exponential backoff dengan jitter untuk menghindari thundering herd.
3) Tetapkan batas retry dan fallback (circuit breaker, dead letter).
4) Uji skenario kegagalan: simulasi timeout, 5xx, unavailability.
5) Monitor metrik retry dan failure rate untuk mendeteksi degradasi.

**Kriteria Penerimaan:** Retry policy terdokumentasi dan teruji. Sistem pulih dari
kegagalan transien tanpa intervensi manual.

**Kegagalan Umum:** Retry pada operasi non-idempoten, backoff terlalu agresif atau
pasif, atau tidak menguji skenario kegagalan.
"""

version = "0.0.1"
