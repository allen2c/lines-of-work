"""Fabric inspection scheduling."""

title = "Jadwal Inspeksi Kain"

content = """
Inspeksi kain harus selesai sebelum kain masuk ke proses cutting. Perencana
menjadwalkan inspeksi agar tidak menjadi bottleneck.

**Lead time inspeksi:** Setiap meter kain memerlukan waktu inspeksi. Kapasitas
inspeksi harian membatasi jumlah kain yang dapat diproses. Perencana memastikan
kain tiba dan terinspeksi sebelum tanggal cutting direncanakan.

**Prioritas:** Order dengan deadline ketat mendapat prioritas inspeksi. Kain
dengan riwayat reject tinggi dapat memerlukan inspeksi lebih ketat dan waktu
lebih lama.

**Koordinasi dengan penerimaan:** Jadwal penerimaan barang dari pemasok
dikoordinasikan dengan kapasitas inspeksi agar tidak terjadi penumpukan.
"""  # noqa: E501

version = "0.0.1"
