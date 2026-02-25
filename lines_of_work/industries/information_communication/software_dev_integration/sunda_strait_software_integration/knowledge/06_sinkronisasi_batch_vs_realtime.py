title = "Sinkronisasi Batch vs Real-time"

content = """
Pemilihan model sinkronisasi mempengaruhi latensi, beban sistem, dan kompleksitas. Pahami
trade-off untuk memilih pendekatan yang sesuai dengan kebutuhan bisnis.

**Batch:** Data ditransfer dalam periode terjadwal (misalnya setiap jam, setiap malam).
Cocok untuk data yang tidak membutuhkan kesegaran instan — laporan, analitik, backup.
Keuntungan: prediktabel, efisien untuk volume besar, mengurangi beban puncak. Kerugian:
data bisa usang hingga periode berikutnya.

**Real-time (atau Near Real-time):** Event atau perubahan diproses segera setelah terjadi.
Cocok untuk transaksi, notifikasi, inventori live. Keuntungan: data segar, pengalaman
pengguna lebih baik. Kerugian: kompleksitas lebih tinggi, beban terus-menerus, perlu
strategi backpressure dan graceful degradation.

**Hybrid:** Kombinasikan keduanya — real-time untuk operasi kritis, batch untuk agregasi
dan analitik. Pastikan konsistensi eventual jelas dan dapat diterima oleh bisnis.
"""  # noqa: E501

version = "0.0.1"
