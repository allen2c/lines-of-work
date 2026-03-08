"""Knowledge: SLA and uptime monitoring fundamentals."""

title: str = "Pemantauan SLA dan Uptime"

content: str = """
SLA (Service Level Agreement) mendefinisikan komitmen ketersediaan dan kinerja layanan.
Pemantauan uptime adalah tanggung jawab inti operasi platform.

**Definisi Uptime:** Persentase waktu di mana layanan dapat diakses dan berfungsi
normal. Uptime 99.9% setara dengan downtime maksimal ~8.76 jam per tahun.

**Metrik Utama:** Availability (persentase uptime), latency (p50, p95, p99), error rate
(4xx/5xx per total request), dan throughput (requests/detik).

**Check Kesehatan:** Endpoint health-check harus diuji dari beberapa lokasi/region untuk
mendeteksi outage parsial. Interval polling standar: 1–5 menit bergantung sensitivitas.

**Pelaporan:** Review SLA harian dan mingguan. Laporkan breach ke tim Product dan
Customer Success untuk kompensasi atau kredibilitas kontrak.
"""  # noqa: E501

version: str = "0.0.1"
