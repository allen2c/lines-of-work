title = "Arsitektur Integrasi: Pola dan Pendekatan"

content = """
Arsitektur integrasi menentukan bagaimana sistem-sistem yang berbeda saling terhubung dan
bertukar data. Memilih pola yang tepat berdampak pada keandalan, skalabilitas, dan
kemudahan pemeliharaan.

**Pola Point-to-Point:** Setiap sistem terhubung langsung dengan sistem lain. Cocok untuk
skenario sederhana dengan sedikit sistem, tetapi menjadi sulit dipertahankan ketika jumlah
koneksi bertambah. Kompleksitas tumbuh secara kuadrat dengan penambahan sistem.

**Pola Hub-and-Spoke:** Sistem pusat (hub) menjadi perantara. Semua sistem berbicara
melalui hub. Keuntungan: satu titik untuk transformasi, routing, dan pemantauan. Risiko:
hub menjadi bottleneck dan single point of failure; perlu dirancang untuk high availability.

**Pola Event-Driven:** Sistem mempublikasikan event ke message broker; sistem lain
berlangganan event yang relevan. Decoupling tinggi, skalabilitas horizontal alami. Cocok
untuk arsitektur mikrolayanan dan integrasi asinkron. Memerlukan disiplin dalam desain
event schema dan idempotensi.
"""  # noqa: E501

version = "0.0.1"
