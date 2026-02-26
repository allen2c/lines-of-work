title = "Validasi Pesanan dan Pemeriksaan Awal"

content = """
Validasi pesanan adalah langkah pertama kritis dalam pemenuhan. Setiap pesanan
masuk harus diverifikasi untuk memastikan data lengkap, alamat dapat dikirim,
dan tidak ada indikator penipuan sebelum dialokasikan ke stok.

**Kelengkapan Data:** Verifikasi nama penerima, nomor telepon, alamat lengkap
dengan kode pos, dan metode pembayaran yang dikonfirmasi. Pesanan tanpa konfirmasi
pembayaran tidak boleh diproses ke tahap picking.

**Validasi Alamat:** Pastikan alamat berada dalam area layanan kurir yang
digunakan. Wilayah kepulauan terpencil mungkin memiliki batasan jasa pengiriman.
Gunakan layanan validasi alamat untuk mendeteksi format salah atau alamat fiktif.

**Indikator Penipuan:** Waspadai pola seperti alamat pengiriman yang sangat
berbeda dari alamat penagihan, pesanan bernilai tinggi ke alamat baru, atau
beberapa pesanan dalam waktu singkat ke alamat yang sama dari akun berbeda.
"""  # noqa: E501

version = "0.0.1"
