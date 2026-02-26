title = "Konfirmasi Pembayaran dan Hold Stock"

content = """
Pesanan hanya boleh diproses ke tahap picking setelah pembayaran dikonfirmasi.
Tanpa konfirmasi, risiko overselling dan pengiriman tanpa bayar tinggi.

**Gateway Pembayaran:** Transfer bank, e-wallet, kartu kredit mengirim
callback atau webhook ke sistem ketika pembayaran berhasil. Sistem
memperbarui status pesanan menjadi "paid" dan melepaskan hold (jika ada)
atau mengalokasikan stok.

**Reconciliation:** Terkadang pembayaran tertunda atau callback gagal.
Prosedur rekonsiliasi harian membandingkan pesanan "menunggu pembayaran"
dengan dana yang masuk. Jika ada pembayaran yang tidak terkonfirmasi,
proses manual atau hubungi payment provider.

**Hold Stock:** Beberapa platform menahan stok untuk keranjang checkout
dalam waktu singkat (mis. 15–30 menit). Jika tidak checkout, stok
dilepaskan. Pastikan mekanisme hold tidak menahan stok terlalu lama.
"""  # noqa: E501

version = "0.0.1"
