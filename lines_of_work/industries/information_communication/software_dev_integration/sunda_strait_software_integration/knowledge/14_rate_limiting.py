title = "Rate Limiting dalam Integrasi"

content = """
Rate limiting melindungi API dari overload dan menyediakan fair usage. Saat mengintegrasikan
dengan API pihak ketiga, memahami dan menghormati limit mereka menghindari throttling atau
pemblokiran. Saat memaparkan API sendiri, rate limiting melindungi infrastruktur.

**Bentuk Limit:** Permintaan per detik, per menit, per hari. Per IP, per API key, per pengguna.
Burst allowance untuk lonjakan singkat. Respons 429 Too Many Requests dengan header
Retry-After atau X-RateLimit-Reset.

**Strategi Klien:** Monitor header X-RateLimit-Remaining, X-RateLimit-Limit. Backoff saat
mendekati limit. Queue permintaan di sisi klien; jangan kirim melebihi kapasitas. Gunakan
connection pooling dan reuse untuk efisiensi.

**Implementasi Server:** Token bucket, sliding window, fixed window. Redis untuk state
shared di multi-instance. Return 429 dengan pesan jelas. Dokumentasikan limit di API docs.
"""  # noqa: E501

version = "0.0.1"
