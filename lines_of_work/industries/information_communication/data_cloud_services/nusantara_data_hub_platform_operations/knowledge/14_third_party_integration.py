"""Knowledge: Third-party integration validation and operations."""

title: str = "Validasi dan Operasi Integrasi Pihak Ketiga"

content: str = """
Platform data sering bergantung pada integrasi pihak ketiga: API eksternal, SaaS,
dan layanan cloud. Operasi harus memantau dan memvalidasi integrasi ini.

**Health Check:** Uji koneksi ke endpoint pihak ketiga secara berkala. Monitor rate
limit usage dan quota. Alert jika SLA pihak ketiga dilanggar.

**Dependency Mapping:** Dokumentasikan setiap integrasi: vendor, endpoint, credentials
location, retry policy. Identifikasi single point of failure.

**Failure Handling:** Siapkan fallback atau circuit breaker. Komunikasikan outage
pihak ketiga ke pelanggan yang terdampak. Coordinate dengan vendor support jika perlu.
"""  # noqa: E501

version: str = "0.0.1"
