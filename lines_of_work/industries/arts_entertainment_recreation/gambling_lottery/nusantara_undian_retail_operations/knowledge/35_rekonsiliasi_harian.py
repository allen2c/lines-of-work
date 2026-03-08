"""Knowledge: Daily reconciliation procedures."""

title: str = "Rekonsiliasi Harian"

content: str = """
Rekonsiliasi harian memastikan catatan penjualan, pembayaran hadiah, dan kas sesuai.
Selisih diperiksa dan dilaporkan. Prosedur ini mendeteksi kesalahan atau anomali dini.

**Elemen.** Bandingkan: total penjualan tercatat, total pembayaran hadiah, kas fisik,
dan inventaris tiket. Semua harus seimbang atau selisih terdokumentasi.

**Selisih kecil.** Selisih sangat kecil mungkin dapat ditoleransi (misalnya pembulatan).
Kebijakan internal menetapkan threshold. Selisih dalam toleransi dicatat dan dilaporkan.

**Selisih besar.** Selisih di atas threshold memerlukan penyelidikan. Laporkan ke atasan.
Jangan menutupi atau mengabaikan selisih yang signifikan.
"""  # noqa: E501

version: str = "0.0.1"
