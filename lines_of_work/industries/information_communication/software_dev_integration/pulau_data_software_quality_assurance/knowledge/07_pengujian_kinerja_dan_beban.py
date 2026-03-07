"""Knowledge item: pengujian kinerja dan beban."""

title = "Pengujian Kinerja dan Beban"

content = """
Pengujian kinerja dan beban memvalidasi bahwa sistem memenuhi target latency, throughput,
dan stabilitas di bawah beban yang diharapkan. Penting untuk layanan digital di Indonesia
yang mengalami lonjakan lalu lintas (misalnya saat promo e-commerce atau pembayaran).

**Konteks:** Pengguna Indonesia sering mengakses dari jaringan seluler dengan bandwidth
bervariasi. Aplikasi harus responsif dan stabil meskipun beban tinggi atau koneksi lambat.

**Langkah Utama:**
1) Definisikan SLO kinerja: waktu respons, throughput, error rate.
2) Buat skenario beban realistis berdasarkan data produksi atau proyeksi.
3) Gunakan alat seperti k6, JMeter, atau Locust untuk simulasi beban.
4) Pantau metrik sistem (CPU, memori, I/O) selama pengujian.
5) Identifikasi bottleneck dan rekomendasikan optimasi.

**Kriteria Penerimaan:** SLO terpenuhi di bawah beban target, bottleneck terdokumentasi,
dan rekomendasi perbaikan disampaikan ke tim pengembangan.

**Kegagalan Umum:** Skenario beban tidak realistis, mengabaikan cold start, atau tidak
menguji di lingkungan yang mendekati produksi.
"""

version = "0.0.1"
