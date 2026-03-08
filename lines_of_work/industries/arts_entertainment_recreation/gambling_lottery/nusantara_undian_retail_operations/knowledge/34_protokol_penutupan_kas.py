"""Knowledge: Cash closing protocol."""

title: str = "Protokol Penutupan Kas"

content: str = """
Penutupan kas di akhir shift meliputi penghitungan, rekonsiliasi, dan penyimpanan
yang aman. Prosedur harus diikuti tepat untuk memastikan akurasi dan keamanan.

**Penghitungan.** Hitung semua denominasi tunai. Pisahkan kas yang akan disetor dari
kas float untuk shift berikutnya. Catat total di formulir penutupan.

**Rekonsiliasi.** Bandingkan total kas dengan penjualan minus pembayaran hadiah.
Selisih harus dijelaskan. Selisih besar dilaporkan ke atasan segera.

**Penyimpanan.** Simpan kas dalam pouch atau brankas sesuai prosedur. Serahkan ke
petugas bank-in atau amankan di brankas sesuai jadwal. Dua orang hadir bila prosedur
menghendaki.
"""  # noqa: E501

version: str = "0.0.1"
