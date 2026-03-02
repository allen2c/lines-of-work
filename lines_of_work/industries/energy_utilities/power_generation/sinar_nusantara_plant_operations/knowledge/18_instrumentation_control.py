title = "Instrumentasi dan Sistem Kontrol"

content = """
Instrumentasi mengukur parameter proses (tekanan, suhu, flow, level, getaran, dll.) dan
mengirim sinyal ke sistem kontrol. DCS (Distributed Control System) memproses sinyal,
menjalankan logic kontrol, dan memungkinkan operator memantau dan mengendalikan pembangkit.

**Kalibrasi:**
Instrument harus dikalibrasi berkala untuk memastikan akurasi. Drift menyebabkan pembacaan
salah dan keputusan operasional yang keliru. Ikuti jadwal kalibrasi dan dokumentasikan hasil.

**Proteksi dan interlock:**
Sistem proteksi (ESD, overspeed, flame failure, dll.) harus beroperasi independen atau
semi-independen dari DCS agar tetap berfungsi jika DCS gagal. Jangan menonaktifkan proteksi
tanpa persetujuan formal dan mitigasi risiko.

**Ketersediaan:**
Kontrol pembangkit bergantung pada instrumentasi. Gagal sensor kritis dapat menyebabkan trip
atau operasi tidak aman. Redundansi dan perawatan rutin mendukung ketersediaan.
"""  # noqa: E501

version = "0.0.1"
