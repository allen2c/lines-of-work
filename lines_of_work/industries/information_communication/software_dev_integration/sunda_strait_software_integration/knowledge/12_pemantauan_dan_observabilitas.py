title = "Pemantauan dan Observabilitas Integrasi"

content = """
Integrasi yang berjalan di banyak sistem memerlukan visibilitas untuk mendeteksi masalah,
mendiagnosis root cause, dan memastikan SLA. Observabilitas mencakup logs, metrics, dan traces.

**Logs:** Log setiap panggilan keluar (endpoint, timestamp, durasi, status). Log error
dengan konteks lengkap (request ID, correlation ID). Hindari log data sensitif. Struktur
(log JSON) memudahkan agregasi dan pencarian.

**Metrics:** Rate (permintaan/detik), latency (p50, p95, p99), error rate. Metrik bisnis:
jumlah record yang disinkronkan, backlog queue. Dashboard untuk visualisasi; alert untuk
threshold yang dilanggar.

**Distributed Tracing:** Trace ID merambat melalui seluruh chain panggilan. Zipkin, Jaeger,
atau vendor cloud. Memungkinkan melihat latency per hop dan mengidentifikasi bottleneck.
Korelasi dengan logs via trace ID.
"""  # noqa: E501

version = "0.0.1"
