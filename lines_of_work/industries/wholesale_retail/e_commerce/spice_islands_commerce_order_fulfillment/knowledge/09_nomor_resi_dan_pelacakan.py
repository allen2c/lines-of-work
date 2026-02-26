title = "Nomor Resi dan Pelacakan Pengiriman"

content = """
Nomor resi (airway bill atau tracking number) adalah identifikasi unik untuk
setiap paket. Pelanggan menggunakannya untuk melacak status pengiriman secara
real-time.

**Pembuatan Resi:** Setelah paket dipacking dan ditimbang, sistem memanggil API
kurir untuk menghasilkan nomor resi. Label pengiriman dicetak dan ditempel
pada paket. Resi harus segera diunggah ke sistem pesanan dan dikirimkan ke
pelanggan melalui email atau notifikasi aplikasi.

**Update Status:** Kurir memberikan webhook atau polling untuk update status:
diterima di gudang, dalam perjalanan, sampai di hub, keluar untuk pengantaran,
dan delivered. Perbarui status pesanan di sistem dan beri notifikasi pelanggan
pada milestone penting.

**Pelacakan Pelanggan:** Sediakan link pelacakan yang mengarah ke halaman
kurir. Beberapa marketplace menyediakan pelacakan terpusat di dalam aplikasi.
"""  # noqa: E501

version = "0.0.1"
