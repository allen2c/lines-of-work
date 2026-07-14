title = "Alat Monitoring dan Metrik Utama"

content = """
- Zabbix: Memonitor perangkat keras (server, switch, UPS, PDU) dengan metrik: suhu CPU, penggunaan RAM, beban disk, status power.
- Prometheus + Grafana: Memonitor layanan cloud (VM, container, database) dengan metrik: CPU usage, memory usage, disk I/O, network throughput, latency API.
- Threshold default:
  - CPU usage >80% selama 5 menit → alert tinggi.
  - Disk usage >90% → alert tinggi.
  - Suhu ruang data >27°C → alert kritis.
  - Kelembaban <40% atau >60% → alert tinggi.
- Dashboard Grafana menampilkan status real-time seluruh klaster. Refresh setiap 30 detik.
- Log monitoring: Semua alert dan aksi dicatat di Elasticsearch untuk audit.
"""  # noqa: E501

version = "0.0.1"
