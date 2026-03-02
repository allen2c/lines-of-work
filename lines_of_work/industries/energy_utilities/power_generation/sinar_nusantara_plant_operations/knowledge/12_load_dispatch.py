title = "Pengaturan Beban dan Koordinasi P3B"

content = """
P3B (Pusat Pengatur Beban) mengoordinasikan pembangkitan listrik nasional. Sinar Nusantara
menerima instruksi beban dari P3B dan harus mematuhi dalam batas kemampuan teknis pembangkit.

**Jenis perintah:**
Perintah beban harian: rencana MW per jam. Perintah real-time: penyesuaian saat operasi
untuk menyeimbangkan grid. Perintah darurat: perubahan cepat saat frekuensi grid abnormal.

**Respons frekuensi:**
Grid Indonesia beroperasi pada 50 Hz. Saat frekuensi turun, pembangkit harus dapat menaikkan
output (jika reserve tersedia); saat frekuensi naik, mengurangi output. Karakteristik ini
mendukung stabilitas grid otomatis.

**Pelaporan:**
Laporkan kapasitas tersedia (declared capacity) ke P3B sesuai jadwal. Laporkan forced outage
dan perkiraan waktu kembali. Pertahankan komunikasi terbuka untuk koordinasi.
"""  # noqa: E501

version = "0.0.1"
