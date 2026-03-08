"""Knowledge: Observability pillars — metrics, logs, and traces."""

title: str = "Observability: Metrik, Log, dan Trace"

content: str = """
Observability terdiri dari tiga pilar: metrik, log, dan trace.

**Metrik:** Ukuran numerik agregat (CPU, memory, request rate, error count). Gunakan
untuk dashboards dan alerting. Golongan: RED (rate, error, duration) untuk request;
USE (utilization, saturation, error) untuk resource.

**Log:** Catatan peristiwa diskrit dari aplikasi dan infrastruktur. Centralized logging
memudahkan pencarian lintas layanan. Retensi standar: 7–30 hari untuk operasional.

**Trace:** Merekam perjalanan request lintas layanan (distributed tracing). Penting untuk
debug latensi pada arsitektur mikroservis.

**Best Practice:** Korelasi metrik, log, dan trace melalui identifier bersama (request_id,
trace_id) mempercepat root cause analysis.
"""  # noqa: E501

version: str = "0.0.1"
