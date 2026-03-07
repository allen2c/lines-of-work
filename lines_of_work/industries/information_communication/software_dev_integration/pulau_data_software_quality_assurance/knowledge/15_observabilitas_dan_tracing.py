"""Knowledge item: observabilitas dan tracing."""

title = "Observabilitas dan Tracing"

content = """
Observabilitas mencakup metrik, log, dan tracing untuk memahami perilaku sistem
dalam produksi. Pengujian harus memvalidasi bahwa sistem dapat diobservasi.

**Konteks:** Tanpa observabilitas yang memadai, insiden sulit didiagnosis dan
waktu pemulihan membengkak. Pengujian pra-rilis harus memastikan bahwa metrik
penting terekspos dan trace tersedia untuk alur kritis.

**Langkah Utama:**
1) Validasi bahwa metrik bisnis dan teknis terekspos (latency, error rate, throughput).
2) Periksa struktur log: konsisten, dapat di-parse, tidak mengandung data sensitif.
3) Uji distributed tracing untuk alur yang melintasi beberapa layanan.
4) Pastikan alert dikonfigurasi untuk kondisi kritis.
5) Verifikasi bahwa dashboard dan runbook tersedia untuk on-call.

**Kriteria Penerimaan:** Alur kritis dapat dilacak end-to-end. Metrik dan alert
mendukung diagnosis insiden.

**Kegagalan Umum:** Log berlebihan atau tidak terstruktur, trace tidak terhubung,
atau alert yang tidak actionable.
"""

version = "0.0.1"
